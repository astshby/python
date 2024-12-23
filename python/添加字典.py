a={}
flag=1
while flag:
    n=input('what\n')
    m=input('where\n')
    a[m]=n#a['name']=n 这样写只会导致a['name']一直被赋值
    # mm=input('other where\n')
    # a[mm]=int(n)              int不可转字符串或字符
    k=input("again or no\n")#注意：如果不写'\n'，在输入k时不能写空格，要连着写（否则读入空格）
    if k=='no':
        flag=0
print(a)