import os

def clear():
    if os.name == 'nt':
        os.system('CLS')

    else:
        os.system('clear')

def save():
    if os.name == 'nt':
        os.system('git add --all')
        os.system('git commit -am "1114trythis')
        os.system('git push -u origin master')
    else:
        os.system('python')
