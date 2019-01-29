from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint as pp
import re
from m_p_mysql import save, get_conn
import time
import random

pattern = re.compile('\(\'(.*)\'\)')
pattern2 = re.compile('\((.*)\)')

class Melon:
    sql_truncate_sr = "delete from SongRank"
    sql_insert_sr = "insert into SongRank(songid, likecnt, ranking) values(%s,%s,%s)"

    sql_truncate_s = "delete from Song "
    sql_insert_s = "insert into Song(songid, songtitle, singerID, albumID) values(%s,%s,%s,%s)"

    sql_truncate_m = "truncate table Meltop"
    sql_insert_m = "insert into Meltop(ranking, title, singer, likecnt) values(%s,%s,%s,%s)"
    
    #메인 딕셔너리 요소들
    top100_dic = {}
    singers_dic = {}
    singers_name_dic={}
    album_dic = {}
    song_dic = {}
    
    #메인 리스트 요소들
    songsnum = []
    album_id = []
    singers_id=[]
    
    #MYSQL 저장 테이블
    MelTop100_table = []
    Song_table=[]
    Songrank_table=[]
    def __init__(self):
        print("생성됨")
        #1. 크롤링 Main - MelonTop100
        url_top100 = "http://vlg.berryservice.net:8099/melon/list"
        html_top100 = requests.get(url_top100).text
        soup = BeautifulSoup(html_top100, 'html.parser')
        datanocnt = soup.select('#frm > div > table > tbody > tr[data-song-no]')
        #앨범아이디 가수아이디 정규식 표현
        pattern = re.compile('\(\'(.*)\'\)')
        for i in datanocnt:
            #1-1. 노래ID 와 제목
            data_song_no = i.attrs['data-song-no']
            self.songsnum.append(data_song_no)
            songname = i.select_one('div.ellipsis.rank01').text.strip()

            #1-2. 노래ID {가수ID:이름} - 딕셔너리 데이터!    
            singername_for_top100 = i.select_one('span.checkEllipsis').text.strip()
            s_artist_id = i.select('span.checkEllipsis a')
            for k in s_artist_id:
                singer_id = k.attrs['href'] 
                singer_id = re.findall(pattern, singer_id)[0]    
                singer_name = k.text
                self.singers_id.append(singer_id)
                self.singers_name_dic[singer_id]=singer_name

                if self.singers_dic.get(data_song_no) != None:
                    self.singers_dic[data_song_no][singer_id]=singer_name
                    
                else:
                    self.singers_dic[data_song_no]={singer_id:singer_name}
                    
            #1-3. 앨범ID 와 노래 ID 연결
            s_album_id = i.select_one('.wrap a').attrs['href']
            s_album_id = re.findall(pattern, s_album_id)
            self.album_id.append(s_album_id[0])
            self.albumname = i.select_one('.ellipsis.rank03 a').text.strip() 
            self.album_dic[data_song_no]=s_album_id[0]

            #1-4. rank
            rank = i.select_one('span.rank').text
            
            #MelTop100 테이블에 들어가는 데이터!!
            self.top100_dic[data_song_no]= {"rank" : int(rank), "songname" : songname, "singername" : singer_name, "likecnt" : 0, "singerid" : s_album_id[0]} 

            # 1-5 Top100의 좋아요를 위한 json 데이터 합치기!!!#############
            urljson = "http://vlg.berryservice.net:8099/melon/likejson"
            
            params = {
                'contsIds' : ','.join(self.songsnum)
                }
            
            htmlcnt = requests.get(urljson, params=params).text
            jsonData = json.loads(htmlcnt)
            strJson = json.dumps(jsonData, ensure_ascii=False, indent=2)

            for j in jsonData['contsLike']:
                k = str(j['CONTSID'])  
                if self.singers_dic.get(k) == None:
                    continue
                else:
                    self.top100_dic[k]['likecnt'] = j['SUMMCNT']
            dicbyrank = sorted(self.top100_dic.items(), key=lambda d: d[1]['rank']) #sorted 되면 튜플? list? 로 바뀌어 버림!
            
        for i, info in dicbyrank:
                self.MelTop100_table.append([info['rank'], info['songname'], info['singername'], info['likecnt']])
    
    def Mysql_meltop(self):
        print("TOP100 저장중...")
        save(self.sql_truncate_m, self.sql_insert_m, self.MelTop100_table )
        print("TOP100 저장완료!")
    
    def Mysql_song(self):
        for i in self.songsnum:
            for s_id in self.singers_dic[i]:
                    print("Song테이블 저장중....")
                    self.Song_table.append([i, self.top100_dic[i]['songname'], s_id, self.album_dic[i]])
        print("Song테이블 저장 완료")
        save(self.sql_truncate_s, self.sql_insert_s, self.Song_table)
    
    def Mysql_songrank(self):
        for i in self.songsnum:
            print("SongRank테이블 저장중....")
            self.Songrank_table.append([i, self.top100_dic[i]['likecnt'], self.top100_dic[i]['rank']])
        save(self.sql_truncate_sr, self.sql_insert_sr, self.Songrank_table)
        print("SongRank테이블 저장완료!!")

class Albuminfo(Melon):
    sql_truncate = "delete from Albumn"
    sql_insert = '''insert into Albumn(albumno, albumtitle, albumtype, likecnt, producer, issuer, issue_Date, total_p_num, genre, avg_score) 
                values( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                '''
    album_info_dic={}
    album_lst = []

    def __init__(self):
        print("앨범테이블 쓰기 준비!!")
        for i in self.album_id:
            headers = {
            'Referer' : 'http://vlg.berryservice.net:8099/melon/detail?albumId={}'.format(i),
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
            } 
            
            url_album = "http://vlg.berryservice.net:8099/melon/detail?albumId={}".format(i)

            html_album = requests.get(url_album, headers=headers).text
            soup = BeautifulSoup(html_album, 'html.parser')

            data_album_dt = soup.select('#conts > div.section_info > div > div.entry > div.meta > dl.list > dt ')
            data_album_dd = soup.select('#conts > div.section_info > div > div.entry > div.meta > dl.list > dd')
            data_album_type = soup.select('#conts > div.section_info > div > div.entry > div.info > span')
            data_album_title = soup.select('head > meta:nth-of-type(7)')
            
            for k, info in enumerate(data_album_dt):
                if self.album_info_dic.get(i) == None:
                    self.album_info_dic[i]={'likecnt' : 0}
                    self.album_info_dic[i]={'평점' : 0}
                    self.album_info_dic[i]={'사람수' : 0 }
                    self.album_info_dic[i]={info.text : data_album_dd[k].text}
                else:     
                    self.album_info_dic[i][info.text]= data_album_dd[k].text

            albumn_type = data_album_type[0].text.strip()
            albumn_title = data_album_title[0].attrs['content']

            self.album_info_dic[i]['albumtype']=albumn_type
            self.album_info_dic[i]['albumtitle']=albumn_title
            a_urljson = "http://vlg.berryservice.net:8099/melon/albumlikejson"
            grade_urljson ="http://vlg.berryservice.net:8099/melon/albumratejson"
        
            album_params = {
                'albumId' : i
                }

            a_htmlcnt = requests.get(a_urljson, params=album_params, headers=headers).text
            grade_htmlcnt = requests.get(grade_urljson, params=album_params, headers=headers).text
            
            a_jsonData = json.loads(a_htmlcnt)
            grade_jsonData = json.loads(grade_htmlcnt)

            a_strJson = json.dumps(a_jsonData, ensure_ascii=False, indent=2)
            grade_strJson = json.dumps(grade_jsonData, ensure_ascii=False, indent=2)    

            for j in a_jsonData['contsLike']:
                k = str(j['CONTSID'])
                self.album_info_dic[k]['likecnt'] = j['SUMMCNT']
            self.album_info_dic[i]['사람수'] = grade_jsonData['infoGrade']['PTCPNMPRCO']
            self.album_info_dic[i]['평점'] = grade_jsonData['infoGrade']['TOTAVRGSCORE']
    
    def Mysql_albuminfo(self):
        for i in self.album_info_dic.keys():
            self.album_lst.append( [str(i), str(self.album_info_dic[i]['albumtitle']), str(self.album_info_dic[i]['albumtype']), 
            str(self.album_info_dic[i]['likecnt']), self.album_info_dic[i]['발매사'], self.album_info_dic[i]['기획사'], 
            str(self.album_info_dic[i]['발매일']), str(self.album_info_dic[i]['사람수']), self.album_info_dic[i]['장르'], 
            str(self.album_info_dic[i]['평점']) ])
            print("앨범테이블 저장중")   
        save(self.sql_truncate, self.sql_insert, self.album_lst)
        print("앨범저장완료")

class Artistsinfo(Melon):    
    sql_truncate = "delete from Artists_info"
    sql_insert = "insert into Artists_info(songid, artists_id, artists_index) values( %s, %s, %s)"

    artists_dic_t={}
    artist_info_lst = []

    def __init__(self):
        print("아티스트테이블 쓰기 준비!!")
        for songnum in self.songsnum:
            url_song = "http://vlg.berryservice.net:8099/melon/songdetail?songId={}".format(songnum)
            html_song = requests.get(url_song).text
            soup = BeautifulSoup(html_song, 'html.parser')
            data_artists_type = soup.select('#conts > div.section_prdcr > ul > li') #셀렉터 공부 다시!!
            data_artists_name = soup.select('#conts > div.section_prdcr > ul > a')
            data_artists_id = soup.select('#conts > div.section_prdcr > ul > a')
            data_singers_id=soup.select('#downloadfrm > div > div > div.entry > div.info > div.artist > a')
            
            start_num=1
            for s in data_singers_id:
                s_id_info = s.attrs['href']
                s_id_info = re.findall(pattern, s_id_info)[0]
                
                if self.artists_dic_t.get(songnum) != None:
                    if '가수' in self.artists_dic_t[songnum].keys():
                        inner_value=len(self.artists_dic_t[songnum]['가수'].keys())
                        self.artists_dic_t[songnum]['가수'][str(inner_value+1)]= s_id_info
                    else:
                        self.artists_dic_t[songnum]['가수']={str(start_num) : s_id_info}

                else:
                    self.artists_dic_t[songnum]={'가수' : {str(start_num) : s_id_info}}

            for i in data_artists_type:
                head = i.select_one('div.meta').text.strip()
                content = i.select_one('a.artist_name').text.strip()
                a_id = i.select_one('.ellipsis.artist a').attrs['href']
                a_id = re.findall(pattern2, a_id)[0]
                
                if head not in self.artists_dic_t[songnum].keys():
                    self.artists_dic_t[songnum][head]= {str(start_num) : a_id}    
            
                else: 
                    inner_value=len(self.artists_dic_t[songnum][head].keys())
                    self.artists_dic_t[songnum][head][str(inner_value+1)]= a_id
    
    def Mysql_artists(self):         
        for id in self.artists_dic_t:
            for head in self.artists_dic_t[id]:
                for artist_id in self.artists_dic_t[id][head].values():
                    self.artist_info_lst.append([str(id), str(artist_id), str(head)])
            print("아티스트정보 저장중")        
        
        save(self.sql_truncate, self.sql_insert, self.artist_info_lst)
        print("아티스트 테이블 저장완료")

class Singersinfo(Melon):
    sql_truncate_s = "delete from Singers "

    
    artist_info_lists=[]
    singers_info_dic={}

    def __init__(self):
        for i in self.singers_id:
            artist_headers = { 
                'Referer' : 'https://www.melon.com/artist/detail.htm?artistId={}'.format(i[0]),
                # 'Referer' : 'https://www.melon.com/artist/song.htm?artistId=724619',

                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
                } 

            artist_url = 'https://www.melon.com/artist/detail.htm?artistId={}'.format(i[0])
            html_artist = requests.get(artist_url, headers=artist_headers).text
            soup = BeautifulSoup(html_artist, 'html.parser')

            data_artist_dl = soup.select('#conts > div.wrap_dtl_atist > div > div.wrap_atist_info > dl.atist_info.clfix')
            data_artist_dt = soup.select('#conts > div.wrap_dtl_atist > div > div.wrap_atist_info > dl.atist_info.clfix > dt')
            data_artist_dd = soup.select('#conts > div.wrap_dtl_atist > div > div.wrap_atist_info > dl.atist_info.clfix > dd')
            
            temp_list_h=[]
            temp_list_c=[]

            for j, info in enumerate(data_artist_dt):
                temp_list_h.append(info.text)
            
            for k, info in enumerate(data_artist_dd): 
                if k == 0 and info.select_one('span') != None:
                        content = info.select_one('span').next.strip()
                        temp_list_c.append(content)
                
                elif '더보기' in info.text:
                    content = info.select_one('span.ellipsis').text   
                    temp_list_c.append(content)

                else:
                    content=info.text
                    temp_list_c.append(content)

            for num in range(len(temp_list_h)): 
                if self.singers_info_dic.get(i) != None:
                    self.singers_info_dic[i][temp_list_h[num]]=temp_list_c[num]
                    
                else:
                    self.singers_info_dic[i]={temp_list_h[num] : temp_list_c[num]}
            
            time.sleep(random.uniform(1,4))
            
    def Mysql_singers(self):
        for i in self.singers_id:
            self.artist_info_lists=[str(i), self.singers_info_dic[i].values()]

            sql_column = self.singers_info_dic[i].keys()
            temp=sql_column
            
            for n, i in enumerate(temp):
                if i == '데뷔':
                    temp[n]='debut'
                if i == '생일':
                    temp[n]='birthdate'
                if i == '활동유형':
                    temp[n]='s_type'
                if i == '소속사':
                    temp[n]='agency'
                if i == '수상이력':
                    temp[n]='award'
                if i == '결성일':
                    temp[n]='crete'

            for i in range(0,len(temp)):
                if len(temp)== 1:
                    temp[i]=temp[i]
                elif i == 0:
                    temp[i]=temp[i]+','
                elif i == len(temp)-1:
                    temp[i]=temp[i-1]+temp[i]
                else:
                    temp[i]=temp[i-1]+temp[i]+','

            if len(temp) == 1:
                values= "%s"
            if len(temp) == 2:
                values= "%s"+","+"%s"
            if len(temp) == 3:
                values= "%s"+","+"%s"+","+"%s"
            if len(temp) == 4:
                values= "%s"+","+"%s"+","+"%s"+","+"%s"
            if len(temp)== 5:
                values= "%s"+","+"%s"+","+"%s"+","+"%s"+","+"%s"
            if len(temp)== 6:
                values= "%s"+","+"%s"+","+"%s"+","+"%s"+","+"%s"+","+"%s"

            print(temp[-1])
            sql_insert_s = "insert into Singers + ({}) values({})".format(temp[-1], values)
            # save_singers(self.sql_truncate_s, sql_insert_s, self.singers_info_dic[i].values())
            time.sleep(random.uniform(1,5))


        # sql_insert_s = "insert into Singers(singerid, debut, birthdate, s_type, agency, award ) values(%s,%s,%s,%s)"
            
            
            # self.artist_info_lists.append([str(i), self.singers_info_dic[i].values()])
            # singers_info_dic[i]['데뷔'], singers_info_dic[i]['생일'], singers_info_dic[i]['활동유형'], 
            # singers_info_dic[i]['소속사'], singers_info_dic[i]['수상이력']])



Melon = Melon()
# Melon.Mysql_meltop()
# Melon.Mysql_song()
# Melon.Mysql_songrank()

# Album=Albuminfo()
# Album.Mysql_albuminfo()

# Artists=Artistsinfo()
# Artists.Mysql_artists()

singer=Singersinfo()
singer.Mysql_singers()
