import requests, json
from bs4 import BeautifulSoup
from pprint import pprint as pp
from naverAPI_SQL import save, get_conn

url = "https://openapi.naver.com/v1/search/blog.json"

title = "캄보디아"
params = {
    "query": title,
    "display": 100,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "oWaeXA0nme3FmIVx1h6o",
    "X-Naver-Client-Secret": "alfHVYo8xy"
}

result = requests.get(url, params=params, headers=headers).text

jsonData = json.loads(result)

print(jsonData)

exit()

Blogger_sql = [] 
BlogPost = []

# bloggerID bloggername, bloggerlink, 
for item in jsonData['items']: 
    b_id=item['bloggerlink']
    if "naver" in b_id:
        b_id = item['bloggerlink'].replace("http://blog.naver.com/", "")
    elif "http://" in b_id:
        b_id = item['bloggerlink'].replace("http://", "")
    else:
        b_id = item['bloggerlink'].replace("https://", "")     
    
    Blogger_sql.append([b_id, item['bloggername'], item['bloggerlink']])
    BlogPost.append([item['title'], item['link'], b_id, item['postdate']])

sql_truncate_B = "delete from Blogger"
sql_insert_B = "insert into Blogger(bloggerID, bloggername, bloggerlink) values(%s,%s,%s)"
save(sql_truncate_B, sql_insert_B, Blogger_sql)

sql_truncate_BP = "delete from BlogPost"
sql_insert_BP = "insert into BlogPost(title, link, bloggerID, postdate) values(%s,%s,%s,%s)"
save(sql_truncate_BP, sql_insert_BP, BlogPost)




