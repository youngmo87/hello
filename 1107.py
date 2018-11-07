
cmd = input("Input(usage: 이름,나이,성별)>>")
print(cmd)

#1. 값이 존재여부 체크
if cmd = '':
    print("디질래?")
    exit()

#2. 콤마의 존재여부
if ',' not in cmd:
    print("디질래?")
    exit()
#2. 콤마의 존재여부(모범답안)
if ',' not in com:
    print(error_msg)
    exit()

if cmd.find(',')

#3.3개의 값이 있는지
cmds = cmd.split(',')
if cmds[2]  False:
    print("디질래?")
    exit()
#3.3개의 값이 있는지
if len(cmds) != 3:
    print("디질래?")
    exit()

outmsg="당신의 이름은 {}, 나이는 {}, 성별은 {} 입니다"
cmds = cmd.split(',')

#outmsg=("당신의 이름은 {}, 나이는 {}, 성별은 {} 입니다".format(cmds[0], cmds[1], cmds[2]))
#괄호의 유무 언제 써야할까?

print(outmsg.format(cmds[0], cmds[1], cmds[2]))

