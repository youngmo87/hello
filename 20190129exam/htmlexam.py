from bs4 import BeautifulSoup
import requests
import json
import re

html_artist = '''
    <dl>
        <dt>국적</dt>
        <dd>대한민국</dd>

        <dt>활동장르</dt>
        <dd>Dance, Ballad, Drama</dd>
    
        <dt>데뷔</dt>
        <dd class="debut_song">
            <span class="ellipsis">
                2016.05.05
                <span class="bar">
                    TTT
                </span>
                <a href="#">TTTTTTTTTTTTT</a>
            </span>
        </dd>
        
        <dt>수상이력</dt>
        <dd class="awarded">
            <span class="ellipsis">
                2018 하이원 서울가요대상
                <span class="bar">|</span>본상
            </span>
        </dd>
    </dl>
'''

soup = BeautifulSoup(html_artist, 'html.parser')

print(soup.dd.next_sibiling)
exit()
data_artist_dl = soup.select_one('dl > dd.awarded > .ellipsis').text.strip()
print(data_artist_dl)
exit()


data_artist_dt = soup.select('dt')
data_artist_dd = soup.select('dd')

info_dic={}
temp_list_h=[]
temp_list_c=[]

col_dic={"국적" : "nation", "활동장르" : 'genre', '데뷔' : 'debut', "수상이력" : "award"}

for j, info in enumerate(data_artist_dt):
    temp_list_h.append(col_dic[info.text])

for k, info in enumerate(data_artist_dd):     
    if k == 2:
        content = info.select_one('.ellipsis').next.strip()
        temp_list_c.append(content)

    elif k ==3:
        content1 = info.select_one('.ellipsis').next.strip()
        content2 = info.select_one('.ellipsis').next.next.next
        content3 = info.select_one('.ellipsis').next.next.next.next.strip()
        content=content1 + content2 + content3
        temp_list_c.append(content)
        
    else:
        content=info.text
        temp_list_c.append(content)

for num in range(len(temp_list_h)): 
        info_dic[temp_list_h[num]]=temp_list_c[num]    

f1 = tuple(info_dic.keys())
f2 = tuple(info_dic.values())

print("insert into Singer{} values{}".format(f1, f2))