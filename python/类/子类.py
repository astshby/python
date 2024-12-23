
from audioop import ratecv


class deathDog:#实例（某些重复使用的class）
    def __init__(self,time=40,lastplace='god'):
        self.time=time
        self.lastplace=lastplace
    
    def bye(self):
        print(f"last place={self.lastplace}")

class Dog:#父类
    """一般用来写注释"""
    def __init__(self,name,age):#必须要在定义是读入的
        self.name=name
        self.age=age
        self.race='China'
        self.death=deathDog()
    
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
     
    def bye(self):
        print(f"bye bye time={self.death.time}")

class assDog(Dog):#子类
    def __init__(self, name, age,asshole):
        super().__init__(name, age)
        self.asshole=asshole

    def shit(self):
        print(f"My asshole is {self.asshole} big")
        self.asshole=self.asshole+1
    
    def lizheng(self):
        print('I cant lizheng because of my ass')


c=assDog('jj',15,100)
c.shit()
c.lizheng()
c.bye()
print(c.asshole)
c.death.bye() #()很重要