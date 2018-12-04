import re
# line = """Beautiful is better than ugly 
# 못 생김은 아름다움에 비할 것이 못 된다.
# 설명은. 최대한. 간단해야. 하고
# 설명하지 못하는 경우가 있다면,
# 좋지 못한 아이디어라고 생각하자"""

# matches =re.findall("된", line)
# print(matches)

# matches2=re.findall("beautiful", line, re.IGNORECASE)    
# print(matches2)


# m = re.findall("^못", line, re.MULTILINE)
# m2 = re.findall("\ ", line, re.MULTILINE)
# m22 = re.findall("설..", line, re.MULTILINE)
# m3 = re.findall("..,$", line, re.MULTILINE)
# print(m, m2, m22, m3)


# m4 = re.findall("경[우다]가", line, re.MULTILINE)
# print(m4)


# m5 = re.findall("못[^한]", line, re.MULTILINE)
# print(m5)

trythis = """Beautiful is better than ugly. 
Explicit is better than implicit.
Simple is better than complex. 
Complex is better than complicated.
Flat is better than nested. 
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless
you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad
idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

question1 = re.findall("(.*) is.?? better than (.*)", trythis, re.MULTILINE)
print(question1)
# pattern = re.compile("(.*)") 
# mm=re.findall(pattern, question1)
# print(mm)   

# zen2 = """Although never is often better than * right * now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea - - let's do more of those!"""

# m = re.findall("^If", zen2, re.MULTILINE)
# m2 = re.findall("idea\.", zen2, re.MULTILINE)
# m22 = re.findall("idea.", zen2, re.MULTILINE)
# m3 = re.findall("idea.$", zen2, re.MULTILINE)
# print(m, m2, m22, m3)