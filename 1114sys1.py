import sys

print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])


from osclass import clear
clear()
# from osclass import save
# save()



def print_sys_vars():
    for i in [sys.version, sys.copyright, sys.path, sys.platform]:
        print("----",i)

sa=sys.argv
if len(sa)<2:
    print_sys_vars()
    sys.exit()


# with open(sa[1], "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())
