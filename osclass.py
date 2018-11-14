import os

def clear():
    if os.name == 'nt':
        os.system('CLS')

    else:
        os.system('clear')



def save():
    if os.name == 'nt':
        os.system('git add --all')
        # os.system('git commit -am 'print(sys.argv[1])') 이거 문자열에 넣는거는 포맷을 이용해서 넣으면 된다 포맷 안이용하면 계속 오류남
        os.system('git push -u origin master')
    else:
        os.system('python')
