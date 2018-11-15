import os
import sys
import datetime

from osclass import clear
# from osclass import save
# save()


def print_sys_vars():
    for i in [sys.version, sys.copyright, sys.path, sys.platform]:
        print("----",i)

# if len(sa)<2:

print_sys_vars()
clear()

sa=sys.argv
time = datetime.datetime.now()
default_msg = "{} 강의".format(time.strftime('%Y-%m-%d'))
commit_msg = default_msg
has_msg = len(sa) >= 2


if has_msg:
    commit_msg = sa[1]

else:
    input_msg = input("뭘로저장하카마씀? (날짜로는 그냥 Enter 혹은 어떻게 commit 할지 입력하세요 > ")
    if input_msg != '':
        commit_msg = input_msg

if os.name == 'nt':
        os.system('git add --all')
        os.system('git commit -am "{}"'.format(commit_msg)) 
        os.system('git push -u origin master')
    else:
        os.system('python')


save()
sys.exit()

# with open(sa[1], "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())
