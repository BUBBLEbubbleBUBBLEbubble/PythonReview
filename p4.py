""" 函数 """

'''
--函数定义：
  def 函数名():
    代码块
  def 函数名(参数列表，参数可为0-n个):
    代码块 
--函数调用：
  函数名加()即可调用该函数
  本质上就是去执行函数定义里面的代码块，在调用函数之前必须先定义才能使用，否则会出错
  
--函数说明文档：
  函数内容的第一行可以用字符串进行函数说明
'''

'''
--函数参数：
# 参数:
  其实就是函数为了实现某项特定的功能，进而为了得到实现功能所需要的数据；即为了得到外部数据的函数所需的参数
# 参数的分类：
  必选参数、 默认参数/缺省参数、 可选参数/不定长参数、 关键字可变参数
  
# 【1】.必选参数： 形参 + 实参
     --def sum(a,b): # 定义时括号里的是 【形式参数/形参】：只是意义上的一种参数，在定义的时候是不占内存地址的
           sum=a+b
           print(sum)
           pass
     --sum(20,10)    # 调用时括号里为 【实际参数/实参】：实实在在的参数，是实际占用内存地址的
     --函数调用时，每一个必选参数是必须要赋值的
    
# 【2】.默认参数/缺省参数： 始终存在于参数列表中的尾部
     --def sum1 (a, b=40, c=90):   # 这里b,c两个参数已经给了默认值，可以在调用是不赋值；但这里a是必选参数
           print('默认参数使用=%d' % (a+b))
           pass
     --sum1(10)    # 调用函数，若未给bc参数赋值，默认用之前定义函数时的缺省值b=40, c=90。 也可以在调用函数时给重新赋值
     --!!!默认参数要放在最后!!!先写形参再写默认参数！！！

# 【3】.可选参数/可变参数： 当参数的个数不确定时使用，比较灵活
     --概念：
       一个函数有时候会处理比当初声明的参数要多，这就是不定长参数，定义函数时不用声明参数名。
       加了星号（*）的变量args会存放所有未命名的变量参数，args为元组；
       而加**的变量kwargs会存放命名参数，即形如key=value的参数，kwargs为字典。
     --def sum2(*args)
     --sum2(这里可以填可变长的参数，即参数个数可变)

# 【4】.关键字可变参数
     --定义： **
     --在函数体内，参数关键字是一个字典类型，key是一个字符串
     --def keyFunc(**kwargs):
     
# 各种参数混合使用注意事项：
1.可选参数*接受元组数据；关键字可选参数**接受字典数据
2.括号中顺序：必选参数，默认参数，可变参数，关键字参数
'''

'''
--函数返回值
# 概念：函数执行完以后会返回一个对象，如果在函数的内部有return 就可以返回实际的值,否则返回None（空）
# 类型：可以返回任意类型，返回值类型应该取决于return后面的类型
# 用途：给调用方返回数据
# 在一个函数体内可以出现多个return值：但是肯定只能返回一个return
# 如果在一个函数体内 执行了return，意味着函数就执行完成退出了，return后面的代码语句将不会执行
'''

'''
--函数的嵌套
  def fun1():
    ...
  def fun2():
    fun1
    ...
  fun2 调用fun2时会按序执行fun1
'''

'''
--函数的分类：根据函数的返回值和函数的参数
# 有参数无返回值的
# 有参数又返回值的
# 无参数又返回值的
# 无参数无返回值的
'''


'''
******************************************************************************************************************
'''

# ------------------------------------------------------函数定义
def printInfo():
    '''
    这里是对函数功能的描写，ctrl+鼠标放在函数名上时会显示这里的描述
    :return:
    '''
    print('小张的身高是%f' % 1.73)
    print('小张的体重是%f' % 120)
    print('小张的爱好是%s' % '唱歌')
    pass

# ------------------------------------------------------函数调用
printInfo()
printInfo()
printInfo()  # 每次调用都是独立的

# ------------------------------------------------------带参数的函数定义
def printInfo2(name, height, weight, hobby):
    print('%s的身高是%f' % (name, height))
    print('%s的体重是%f' % (name, weight))
    print('%s的爱好是%s' % (name, hobby))
    pass

# ------------------------------------------------------调用带参数的函数
printInfo2('小李', 180, 150, '咨询师')
printInfo2('小马', 160, 100, '画手')


# ------------------------------------------------------1.必选参数
def sum(a, b):  # 形式参数/形参
    sum = a + b
    print(sum)
    pass
sum(10, 20)  # 实参

# ------------------------------------------------------2.默认参数
def sum1(a=10, b=20):  # ab都为默认参数
    sum = a + b
    print(sum)
    pass
sum1()  # 这里默认使用定义函数时的参数值

# def sum1(a=10, b):  # 这里会报错，因为默认按顺序给参数，这个8给了a，b没有赋值
#     sum = a + b
#     print(sum)
#     pass
# sum1(8)

'''
默认参数要放在最后！！
'''

def sum2(a, b=10):  # a为形参，b为默认参数
    sum = a + b
    print(sum)
    pass
sum2(8)
sum2(1,2)

# ------------------------------------------------------3.可变参数
def getComputer(*args):  # 可变长的参数
    '''
    打印数据
    :param args: 可变长的参数类型
    :return:
    '''
    print(args)
    pass
getComputer((1, 2, 3, 4, 5))
getComputer(1)  # 当作元组类型
getComputer(1, 2, 3, 4, 5)

def getComputer(*args):
    '''
    计算累加和
    :param args: 可变长的参数类型
    :return:
    '''
    result = 0
    for item in args:
        result += item
        pass
    print(result)
    pass
getComputer(1)
getComputer(1, 2, 3)
getComputer(1, 2, 3, 4, 5, 7, 8, 9, 5)

# ------------------------------------------------------4.关键字可变参数
def keyFunc(**kwargs):
    print(kwargs)
    pass
# 调用
# keyFunc(1,2,3)  # 会报错。
dictA = {'name':'Bubble', 'age':20}
# keyFunc(dictA)  # 会报错。这样也是不行的，如果要传一个字典类型的参数的话，需要加**
keyFunc(**dictA)
keyFunc(name='Bubble', age=20)  # 通过键值对传
keyFunc()  # 不传也可以

# ------------------------------------------------------组合使用
def complexFunc(*args, **kwargs):
    '''
    函数功能描述
    :param args:
    :param kwargs:
    :return:
    '''
    print(args)
    print(kwargs)
    pass

complexFunc(1,2,3, name='刘德华')
complexFunc(age=31)

# def TestMup(**kwargs, *args):  # 报错 invalid syntax
#     pass
'''
可选参数必须放到关键字可选参数之前
'''


# ------------------------------------------------------函数返回值
#
def Sum(a,b):
    sum = a+b
    pass
Sum(1,2)  #这里没定义return，所以返回的时none

#
def Sum(a,b):
    sum = a+b
    return sum  # 将计算结果返回到调用者
    pass
print(Sum(1,3))  # 函数的返回值返回到调用的地方

rs = Sum(5,5)  # 将返回值赋给其他的变量
print(rs)  # 函数的返回值返回到调用的地方

#
def calSum(num):
    result = 0
    i = 1
    while i <= num:
        result += i
        i += 1
        pass
    return result  # 这里返回类型变为int
value = calSum(10)
print(value)
print(type(value))

#
def calSum(num):
    result = 0
    i = 1
    li = []
    while i <= num:
        result += i
        i += 1
        pass
    li.append(result)
    return li   # 这里返回类型变为list
value = calSum(10)
print(value)
print(type(value))

#
def returnTuple():
    '''
    返回元组类型的数据
    :return:
    '''
    return 1,2,3
a = returnTuple()
print(type(a))

def returnDic():
    '''
    返回字典类型的数据
    :return:
    '''
    return dict(name='a')
    #return {"name":"测试"}  # 这两种都行
a = returnDic()
print(type(a))

# ------------------------------------------------------函数嵌套
def fun1():
    print("--------------fun1 start-------------------")
    print("--------------执行代码省略-------------------")
    print("--------------fun1 end-------------------")
    pass

def fun2():
    print("--------------fun2 start-------------------")
    # 调用第一个函数
    fun1()
    print("--------------fun2 end-------------------")
    pass

fun2()  # 调用函数2
