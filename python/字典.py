a={'name':'p','num':0,'kks':list(range(10))}

b=a.keys();
print(b)
for i in a: #或者a.keys()
    print(a[i])

# for i in b[1:]:
#     print(a[i]) 不可行 dict_key  不是普通列表