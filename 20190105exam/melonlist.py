from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint as pp

url = "https://www.melon.com/chart/index.htm"

headers = {
    'Referer' : 'https://www.melon.com/index.htm',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
} 

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')

datanocnt = soup.select('#frm > div > table > tbody > tr')

dic = {}

for i in datanocnt:
    songsnum = []
    data_song_no = i.attrs['data-song-no']
    songsnum.append(data_song_no)
    rank = i.select_one('div.wrap.t_center').text.strip()
    songname = i.select_one('div.ellipsis.rank01').text.strip()
    singername = i.select_one('span.checkEllipsis').text.strip()
    tempDic = {"CONTSID": data_song_no, "rank" : rank, "songname" : songname, "singername" : singername, "likecnt" : 0} 
    dic[data_song_no]= tempDic
    
    # print(data_song_no)
# print(dic["31399795"])

urljson = "https://www.melon.com/commonlike/getSongLike.json"

params = {
    'contsIds' : ','.join(songsnum)
}

htmlcnt = requests.get(urljson, params=params, headers=headers).text
jsonData = json.loads(htmlcnt)
strJson = json.dumps(jsonData, ensure_ascii=False, indent=2)

for j in jsonData['contsLike']:
    # print("jjj=", j)
    k = str(j['CONTSID'])
    # print(dic[k])
    dic[k]['likecnt'] = j['SUMMCNT']
    
print("===============================")
pp(dic)

    # print("노래번호:순위: {}\t 제목: {}\t\t\t\t\t\t 가수: {}".format(rank.text, songname.text.strip(), singername.text.strip()))

# songinfos=soup.select('div.ellipsis.rank01')
# for songinfo in songinfos:
#     songname = songinfo.text
#     print(songname.strip())
    
# singerinfos=soup.select('span.checkEllipsis')
# for singerinfo in singerinfos:
#     singername = singerinfo.text
#     print(singername)




# songinfos=soup.select('div.ellipsis.rank01')
# for songinfo in songinfos:
#     songname = songinfo.text
#     print(songname.strip())
    
# singerinfos=soup.select('span.checkEllipsis')
# for singerinfo in singerinfos:
#     singername = singerinfo.text
#     print(singername)



# for tr in trs:
    # tds = tr.select('td')
    # rank = tds[1]
    # song_name = tds[5]
    # song_name = tds[5].a.attrs['href']

    # print(song_name.text)
    # print(song_name.text.strip())

    # like_cnt = tds[7].div.button.span.cnt
    
    # song_name = tds[5].div.div.div.ellipsis.rank01.span.a.text
    # print(like_cnt.text)
    # print(rank.text)

    # rate = tds[1]
    # diff = toFloat(tds[2]) - toFloat(tds[3])

    # print("{}, {}, {}".format(tit.strip(), rate.text, diff))

