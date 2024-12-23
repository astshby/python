class Dog:#父类
    """一般用来写注释"""
    def __init__(self,name,age):#必须要在定义是读入的
        self.name=name
        self.age=age
        self.race='China'
    
    def sit(self):
        print(f"{self.name} is now sitting.")
    
    def roll(self):
        print(f"{self.name} rolled over")

    def lizheng(self):
        print(f"I am a {self.race} dog.")
    
    def update_race(self,race):
        if(race==self.race):
            print("sb")
        else:
            self.race=race


a=Dog('kks',6)
b=Dog('nm',1)

print(a.name)#调用属性
a.roll()#调用方法

b.name='sb'#修改属性
b.update_race('China')
b.update_race('American')#self默认为b（定义过），不算函数调用值
a.lizheng()
b.lizheng()