'''
决战紫禁之巅有两个人物，西门吹雪以及叶孤城

属性：
name 玩家的名字
blood 玩家血量

方法：
tong() 捅对方一刀,对方掉血10滴
kanren() 砍对方一刀，对方掉血15滴
chiyao() 吃一颗药，补血10滴
__str__ 打印玩家状态。

'''

import time
# 第一步 需要先去定义一个类【角色类】
class Role:

    def __init__(self, name, hp):
        '''
        初始化构造函数
        :param name: 角色名
        :param hp: 血量
        '''
        self.name = name
        self.hp = hp
        pass

    def tong(self, enemy):
        '''
        捅对方一刀,对方掉血10滴
        :param enemy: 敌人
        :return:
        '''
        enemy.hp -= 10  # 敌人-10血
        info = '【%s】捅了【%s】一刀' % (self.name, enemy.name)
        print(info)
        pass

    def kan(self, enemy):
        '''
        砍对方一刀，对方掉血15滴
        :param enemy:
        :return:
        '''
        enemy.hp -= 15  # 敌人-15血
        info = '【%s】捅了【%s】一刀' % (self.name, enemy.name)
        print(info)
        pass

    def chiyao(self):
        '''
        吃一颗药，补血10滴
        :param enemy:
        :return:
        '''
        self.hp += 10
        info = '【%s】吃了一颗补血药 增加10滴血 ' % (self.name)
        print(info)
        pass

    def __str__(self):
        return '%s 还剩下 %s 的血量'%(self.name,self.hp)
    pass

    pass


xmcx = Role('西门吹雪', 100)
ygc = Role('叶孤城', 100)

while True:
    if xmcx.hp<=0 or ygc.hp<=0:
        # 满足条件 就退出循环
        break
    xmcx.tong(ygc) # 西门吹雪捅了叶孤城一刀
    print(ygc) # 打印对象状态
    print(xmcx)
    print('****************************')
    ygc.tong(xmcx) # 西门吹雪捅了叶孤城一刀
    print(ygc) # 打印对象状态
    print(xmcx)
    print('****************************')
    xmcx.chiyao()
    print(ygc) # 打印对象状态
    print(xmcx)
    time.sleep(1)  # 休眠暂停一秒钟
    pass

print('对战结束.....')



'''
**************************************************************************
'''

# 1、python中如何通过类创建对象，请用代码举例说明。
class Student:
    def run(self):
        print('学生每天进行2000米的跑步训练')
        pass
    pass

xiaoli=Student() #创建一个对象
xiaoli.run()
# 2、如何在类中定义一个方法，请用代码举例说明。
# 参考上述demo
# 3、定义一个水果类，然后通过水果类，创建苹果对象、橘子对象、西瓜对象并分别添加上颜色属性
class  SgClass:
    def __init__(self,name,color):
        '''
        :param name:
        :param color:
        '''
        self.color=color
        self.name=name
        pass
    def __str__(self):
        return '%s 的颜色是【%s】'%(self.name,self.color)
    pass
pg=SgClass('苹果','红色')
pg.zj=10 #通过对象添加对象属性
print(pg)
print('*'*40)
jz=SgClass('橘子','橙色')
print(jz)
print('*'*40)
xg=SgClass('西瓜','黑皮')
print(xg)
# 4、请编写代码，验证self就是实例本身。
class Person:
    def weight(self):
        print('self=%s'%id(self))
    pass

# liming=Person()
# liming.weight()
# print(id(liming))

# 5、定义一个Animal类
# (1)、使用__init__初始化方法为对象添加初始属性。如颜色，名字，年龄。
# (2)、定义动物方法，如run，eat等方法。如调用eat方法时打印xx在吃东西就可以。
# (3)、定义一个__str__方法，输出对象的所有属性。

class Animal:
    def __init__(self,color,name,age):
        '''

        :param color:
        :param name:
        :param age:
        '''
        self.color=color
        self.name = name
        self.age = age
        pass
    def eat(self):
        print('%s 在吃东西'%self.name)
        pass
    def run(self):
        print('%s 在飞快的跑' % self.name)
        pass
    def __str__(self):
        return '%s 的颜色是:%s 今年 %d 岁了'%(self.name,self.color,self.age)
    def __del__(self):
        print('xhl')
    pass

tigger=Animal('黄色','东北虎',4)
tigger.run()
tigger.eat()
print(tigger)
# del tigger
input('ddz')
