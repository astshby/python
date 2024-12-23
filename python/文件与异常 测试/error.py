# a=input('first\n')
# b=input('last\n')
# try:
#     answer=int(a)/int(b)#理解为先试试，尝试成功，执行else
# except ZeroDivisionError:
#     print("0 is fenmu")
# else:
#     print(answer)

from pathlib import Path
path=Path('alice.txt')
try:
    contents=path.read_text()
except FileNotFoundError:
    print(f"{path} cant be found\n")