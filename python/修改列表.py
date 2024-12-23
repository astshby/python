a={}
a['x']=[0,2,5]
a['y']=[6,5,8]
print(a)
# bb=a.keys()
# for b in range(len(bb)): 键值不可变
#     bb[b]='0'      
for aa in a.keys():
    for i in range(len(a[aa])):#值可以变，用for也可以实现
        a[aa][i]='0'
print(a)