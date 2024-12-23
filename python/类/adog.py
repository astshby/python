import dog
#from dog import Dog 不用写dog. 仅导入Dog不用写
#from dog import * 不用写dog. 导入所有且自动为地址，但不好
a=dog.Dog('sbb',4)
b=dog.assDog('hby',15,10000)#导入整个模时要写明模块名

a.lizheng()
a.bye()
a.death.bye()
#b.
b.lizheng()
b.shit()
