""" 函数 """

'''
-----------------------------------------------------------------------------
'''

'''
--函数的4种基本类型
1.无参数，无返回值，一般用于提示信息打印。
2.无参数，有返回值，多用在数据采集中，比如获取系统信息。 
3.有参数，无返回值，多用在设置某些不需要返回值的参数设置。
4.有参数，有返回值，一般是计算型的，需要参数，最终也要返回结果
'''

'''
--局部变量
# 在函数内部定义的变量【作用域仅仅局限在函数的内部】
# 不同的函数可以定义相同的局部变量，但是各自用各自的，不会产生影响
# 作用：为了临时的保存数据，需要在函数中定义来进行存储。函数执行完后函数内的变量等就被释放，就没有意义了
'''

'''
--全局变量
# 定义： 如果一个变量可以在函数内部调用，也可以在函数外部调用，那么这个变量就称为全局变量。
# 全局变量与局部变量重复,局部变量不会影响全局变量，函数使用局部变量。
# 当全局变量和局部变量出现重复定义的时候，程序会优先执行使用函数内部定义的变量【地头蛇】
# 如果在函数的内部要想对全局变量进行修改的话，必须使用 global 关键字进行声明，即要告诉解释器现在要修改了。
'''

'''
-----------------------------------------------------------------------------
'''

'''
--python中万物皆对象

--变量就是对象的引用，对象的操作其实是通过引用来完成的
# eg: a=1 对这个操作。解释器解释时其实做了两件事。1其实是个对象，解释器会开辟一个内存区域，把1放在这里，此时1有个唯一的地址为0x1111；
                    a相当于一个标签/名字，开辟一个栈的空间，解释器会把1的内存地址存在这个栈的某个位置，a指向这个位置，这样就将a与1联系了起来；
                    即a标签关联的是1这个区域的内存地址，访问a的时候就能通过他的内存地址直接找到这个内存地址村的数据。
      a=2 修改a的值。 此时开辟一个新的内存空间地址为0x1112，存放2这个数字；此时a标签指向2的地址了，和1无关了。
                    即数据发生改变时，内存地址会重新分配。
      a本身并没有存储任何数据，只是代表了通过内存地址的指向，通过这个内存地址找到数据。参数之间传递的并不是值而是对象的地址/引用。

--小结：
# 1.在python当中，万物皆对象，在函数调用的时候，实参传递的就是对象的引用
# 2.了解了原理之后，就可以更好的去把控 在函数内部的处理是否会影响到函数外部的数据变化
# 3.参数传递是通过对象引用来完成！！！！！
'''

'''
-----------------------------------------------------------------------------
'''

'''
--匿名函数
# 语法：
  lambda 参数1，参数2，参数3：表达式（执行代码语句）
# 特点
  1.使用lambda关键字去创建函数
  2.没有名字的函数
  3.匿名函数冒号后面的表达式有且只有一个, 注意：是表达式，而不是语句
  4.匿名函数自带return，而这个return的结果就是表达式计算后的结果
  5.只有一行
# 缺点
  1.lambda只能是单个表达式，不是一个代码块，lambda的设计就是为了满足简单函数的场景，
  2.仅仅能封装有限的逻辑，复杂逻辑实现不了，必须使用def来处理
  
--lambda与三元运算
  if a:
     b
  else:
     c
  这样的表达可以由以下等效的表达式来模拟
# b if a else c
  这样的表达式（三元运算）能够放在lambda中，它们能够在lambda函数中来实现选择逻辑
'''

'''
-----------------------------------------------------------------------------
'''

'''
--递归函数
# 定义： 如果一个函数在内部不调用其它的函数，而是自己本身的话，这个函数就是递归函数。
# 特点：
  1.自己调用自己
  2. 递归函数必须有一个结束条件，否则递归无法结束会一直递归下去，只到到达最大递归深度报错。
# 优点：
  1.逻辑简单、定义简单
  2.递归使代码看起来更加整洁、优雅
  3.可以用递归将复杂任务分解成更简单的子问题
  4.使用递归比使用一些嵌套迭代更容易
# 缺点：
  1.容易导致栈溢出，内存资源紧张，甚至内存泄漏。（因为递归是一层一层进去的，递归太多资源等不到释放）
  2.递归逻辑很难调试，递归条件处理不好容易造成程序无法结束，直到达到最大递归错误。
  3.递归占用大量内存，耗费计算机资源。

'''


'''
******************************************************************************************************************
'''


# ------------------------------------------------------局部变量&全局变量

# 以下两个是全局变量【与局部变量的区别：作用域的范围不同】
pro = '计算机信息管理'
name = '吴老师'

def printInfo():
    # name='peter' #局部变量
    print('{}.{}'.format(name, pro))
    pass

def TestMethod():
    name = '刘德华'  # 局部变量
    # 当全局变量和局部变量出现重复定义的时候，程序会优先执行使用函数内部定义的变量【地头蛇】
    print(name, pro)
    pass

def changeGlobal():
    '''
    要修改全局变量
    :return:
    '''
    global pro  # 声明全局变量 后才可以修改
    pro = '修改后的全局变量'  # 若没有上面一行，此为局部变量
    # 如果在函数的内部要想对全局变量进行修改的话，必须使用global 关键字进行声明
    pass

printInfo()

changeGlobal()
print(pro)  # 被修改了吗

TestMethod()


# ------------------------------------------------------引用

a = 1  # 不可变类型。当在其他函数内部被修改后并不影响这个本身的值，因为被修改后会开辟新的内存空间指向新的引用，就和原来这个没有关系了
def func(x):
    print('x的地址：{}'.format(id(x)))  # 1
    x = 2
    print('x值修改后的地址：{}'.format(id(x)))  # 2
    print('x的值：{}' .format(x))
    pass
func(a)
print('a的地址：{}'.format(id(a)))  # 3
print('a的值：{}' .format(a))
# 1，3 两个地址一样，说明传递的并不是值，而是对象的引用，两个引用指向同一个地址，所以地址是一样的。
# 1，2 两个地址不一样，因为当x修改值后，引用不再指向1的内存地址，而是重新开辟了一块内存空间存储修改后的2值，然后x的引用也在修改后指向新的内存空间（即存储2的内存空间）


li = []  # 可变类型，数据值可变，引用/指向地址不变
def testRenc(parms):
    print('内部的变量原地址：{}'.format(id(parms)))
    li.append([1,2,3,4,5])
    print('内部的变量修改后的地址：{}'.format(id(parms)))
    print('内部的数据值：{}'.format(parms))
    pass

print('外部的变量对象原地址：{}'.format(id(li)))
testRenc(li)
print('外部的变量对象修改后的地址：{}'.format(id(li)))
print('外部的数据值：{}'.format(li))


# ------------------------------------------------------匿名函数

def computer(x,y):
    '''
    计算数据和
    :param x:
    :param y:
    :return:
    '''
    return x+y
    pass
print(computer(10,20))

# 将上面的简单函数转换成匿名函数
M = lambda x,y: x+y  # 通过变量调用匿名函数
print(M(20,30))

# 三个数的乘法
result = lambda a, b, c: a * b * c
print(result(2,3,4))

age = 15
print('可以参军' if age>18 else '继续上学')  # 将传统的双分支用一行来替代

# 找到两个数的最大值
funcTest = lambda x,y: x if x>y else y
print(funcTest(2,3))

# 这里前半部分相当于函数，后半部分相当于传参了
rs = (lambda x,y: x if x>y else y)(5,9)
print(rs)

# 平方再+1
rs1 = lambda x: (x**2)+1
print(rs1(2))


# ------------------------------------------------------递归函数

# 求阶乘
# 循环的方式去做
def jiecheng(n):
    result = 1
    for item in range(1,n+1):
        result *= item
        pass
    return result
print('5的阶乘：{}'.format(jiecheng(5)))

# 递归的方式去实现
def diguiJc(n):
    '''
    递归实现
    :param n: 阶乘参数
    :return:
    '''
    if n == 1:   # 出口。像是去楼梯下再回来，这个终止条件就是楼梯底，从这里开始要回去了。像套娃。
        return 1
    else:        # 进递归的条件和方法
        return n*diguiJc(n-1)
    pass
# 递归调用
print('5的阶乘(递归方法)：{}'.format(diguiJc(5)))


# 递归模拟实现树形结构的遍历。 打印所有文件夹名
import os  # 引入文件操作模块
def findFile(file_Path):
    listRs = os.listdir(file_Path)  # 得到该文件路径下的所有文件夹
    for fileitem in listRs:
        full_path = os.path.join(file_Path,fileitem)  # 获取完整的文件路径
        if os.path.isdir(full_path):  # 判断是否为文件夹
            findFile(full_path)  # 如果是应该文件夹，再次递归
        else:
            print(fileitem)
            pass
        pass
    else:  # for-else: 若for后没有break则else会执行
        return
    pass
# 调用搜索文件对象
findFile('E:\\GITcode')
