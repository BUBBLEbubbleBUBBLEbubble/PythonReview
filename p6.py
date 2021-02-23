""" 内置函数 """

'''
# 简介：
  内置函数就是python安装后就自带有的函数。
'''

'''
** 常用的数学运算函数--------------------------------------------------------------

-- abs() 求绝对值函数
# 描述: abs() 函数返回数字的绝对值
# 语法: abs( x )
# 参数: x -- 数值表达式
# 返回值: 函数返回x（数字）的绝对值

-- round() 四舍五入取整
# 描述: round() 方法对浮点数进行近似取值，保留几位小数
# 语法: round( x [, n]  )
# 参数: 
  x -- 数值表达式
  n -- 数值表达式
# 返回值: 返回浮点数x的近似值
# 注意：这里不完全是按照四舍五入或者四舍六入五成双来进行取值的，取值和python的版本有关，还和浮点数的精度有关

-- pow() 求指数
# 描述: pow()方法返回(x的y次方)的值语法: pow(x, y[,z])
# 参数:
  x--数值表达式   
  y--数值表达式   
  z--数值表达式
# 返回值: 返回(x的y次方)的值。如果 z 在存在，则再对结果进行取模，其结果等效于 pow(x,y) % z 。

-- divmod() 求商和余数
# 语法: divmod(a, b)
# 参数: 
  a: 数字
  b: 数字
# 返回值: 一个包含商和余数的元组(a // b, a % b)

-- max() 求最大值
# 描述: max() 方法返回给定参数的最大值，参数可以为序列
# 语法: max( x, y, z, .... )
# 参数: 
  x -- 数值表达式
  y -- 数值表达式
  z -- 数值表达式
# 返回值:返回给定参数的最大值

-- min() 求最小值
# 描述: min() 方法返回给定参数的最小值，参数可以为序列
# 语法: min( x, y, z, .... )
# 参数: 
  x -- 数值表达式
  y -- 数值表达式
  z -- 数值表达式
# 返回值: 返回给定参数的最小值

-- sum()求和
# 描述: sum() 方法对系列进行求和计算
# 语法: sum(iterable[, start])
# 参数: 
  iterable -- 可迭代对象，如：列表、 元组、集合。
  start -- 指定相加的参数，如果没有设置这个值，默认为0
# 返回值: 返回计算结果

-- eval()执行字符串表达式
# 描述: eval() 函数用来执行一个字符串表达式，并返回表达式的值
# 语法: eval(expression[, globals[, locals]])
# 参数: 
  expression -- 表达式
  globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象
  locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象
# 返回值: 返回表达式计算结果
'''

'''
# 类型转换函数------------------------------------------------------------

-- int() 转为整型
# 描述: int() 函数用于将一个字符串或数字转换为整型
# 语法: class int(x, base=10)
# 参数: 
  x -- 字符串或数字
  base -- 进制数，默认十进制
# 返回值: 返回整型数据

-- float() 转换成浮点数
# 描述: float() 函数用于将整数和字符串转换成浮点数
# 语法: class float([x])
# 参数: x -- 整数或字符串
# 返回值:返回浮点数

-- str()转化为字符串
# 描述: str() 函数将对象转化为适于人阅读的形式
# 语法: class str(object='')
# 参数: object -- 对象
# 返回值:返回一个对象的string格式

-- ord()字符转数字
# 描述: ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
       如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常
# 语法: ord(c)
# 参数: c -- 字符
# 返回值:返回值是对应的十进制整数

-- chr()数字转字符
# 描述: chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
# 语法: chr(i)
# 参数: i -- 可以是10进制也可以是16进制的形式的数字
# 返回值:返回值是当前整数对应的ascii字符

-- bool()转为布尔型
# 描述: bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False 
# 语法: class bool([x])
# 参数: x -- 要进行转换的参数
# 返回值:返回 Ture 或 False
# ps: 下列对象都相当于False：[],(),{},0, None, 0.0, ''

-- bin()转为二进制
# 描述: bin() 返回一个整数 int 或者长整数 long int 的二进制表示
# 语法: bin(x) 
# 参数: x -- int 或者 long int 数字
# 返回值:字符串

-- hex()转为十六进制
# 描述: hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
# 语法: hex(x)
# 参数: x -- 10进制整数
# 返回值:返回16进制数，以字符串形式表示

-- oct()转为八进制
# 描述: oct() 函数将一个整数转换成8进制字符串
# 语法: oct(x)
# 参数: x -- 整数
# 返回值:返回8进制字符串

-- list()元组转换为列表
# 描述: list() 方法用于将元组转换为列表
# 语法: list( tup )
# 参数: tup -- 要转换为列表的元组
# 返回值:返回列表

-- tuple()列表转换元组
# 描述: tuple()函数将列表转换为元组
# 语法: tuple(seq)
# 参数: seq -- 要转换为元组的序列
# 返回值: 返回元组

-- dict()创建字典
# 描述: dict() 函数用于创建一个字典
# 语法: 
  class dict(**kwarg)
  class dict(mapping, **kwarg)
  class dict(iterable, **kwarg)
# 参数: 
  **kwargs -- 关键字
  mapping -- 元素的容器
  iterable -- 可迭代对象
# 返回值: 返回一个字典

-- bytes()转为字节数组
# 描述: bytes()方法返回一个新字节数组，这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256
# 语法: class bytearray([source[, encoding[, errors]]])
# 参数: 
  source 为整数，则返回一个长度为 source 的初始化数组；
  source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
  source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
  source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytes
# 如果没有输入任何参数，默认就是初始化数组为0个元素
# 返回值:返回新字节数组
'''

'''
# 序列操作函数------------------------------------------------------------------------

-- all() 
# 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False元素除了是 0、空、FALSE 外都算 TRUE
# 函数等价于：
def all(iterable):   
    for element in iterable:        
        if not element:           
            return False    
    return True
# 语法: all(iterable)
# 参数: iterable -- 元组或列表
# 返回值:如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；
# 注意：空元组、空列表返回值为True，这里要特别注意

-- any() 
# 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True
# 注意： 元素除了是 0、空、FALSE 外都算 TRUE
# 函数等价于：
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
# 语法: any(iterable)
# 参数: iterable -- 元组或列表
# 返回值: 如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true

--sorted() 
# 函数对所有可迭代的对象进行排序操作
# sort与sorted 区别：
  sort是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作,
  list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作
# 语法: sorted(iterable[, cmp[, key[, reverse]]])
# 参数: 
  iterable -- 可迭代对象
  cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0
  key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序
  reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）
# 返回值:返回重新排序的列表

-- reverse() 
# 函数用于反向列表中元素
# 语法: list.reverse()
# 返回值:该方法没有返回值，但是会对列表的元素进行反向排序

-- range() 
# 函数可创建一个整数列表，一般用在 for 循环中
# 语法: range(start, stop[, step])
# 参数: 
  start: 计数从 start 开始默认是从 0 开始例如range（5）等价于range（0， 5）;
  stop: 计数到 stop 结束，但不包括 stop例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
  step：步长，默认为1例如：range（0， 5） 等价于 range(0, 5, 1)

-- zip() 
# 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表
# 语法: zip([iterable, ...])
# 参数: iterabl -- 一个或多个迭代器;
# 返回值:返回元组列表
# 注意：如果可迭代对象的元素个数不一样，那么按照最少的那个迭代压缩最少元素进行可迭代对象结束后退出

-- enumerate()
# 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
# 语法: enumerate(sequence, [start=0])
# 参数: 
  sequence -- 一个序列、迭代器或其他支持迭代对象
  start -- 下标起始位置
# 返回值:返回 enumerate(枚举) 对象
'''

'''
** set集合--------------------------------------------------------------------------

-- set（集合） 
# 是python中的一种数据类型，是一个'无序'且'不重复'的元素集合
# 特点：
  1. 不支持索引和切片，是一个无序且不重复的容器
  2. 类似字典，但是只有key，没有value
# 创建集合方式：
  第一种方式
  set1 = {"1","2"}
  第二种方式
  list1 = ['1','5','4','3']
  set2 = set(list1)
# 集合操作函数:
-- add() 添加一个元素
-- clear() 清空集合的元素
-- difference() 两个集合的差集，a中存在，b中不存在
-- intersection() 两个集合的交集，a中存在，b中也存在的
-- union() 并集，包含a中的元素，也包含b中的元素
-- pop() 集合pop随机移除某个元素并且获取那个参数,集合pop没有参数
-- discard() 移除指定元素
-- update() 更新集合
'''

'''
** 小结--------------------------------------------------------------------------
数学运算
abs() 、 round() 、pow() 、divmod() 、max() 、min() sum() 、eval()
类型转换
int()、float()、str()、ord()、chr()、bool()、bin()、hex()、oct()、list()、tuple()、dict()、bytes()
序列操作
all()、any()、sorted()、reverse()、range()、zip()、enumerate()
集合
add()、clear()、difference()、intersection()、union()、pop()、discard()、update()
'''

'''
******************************************************************************************************************
'''

# ------------------------------------------------------常用的数学运算函数
# 取绝对值
print(abs(-56))
print(abs(1 - 8))

# round  取近似值
print(round(2.66))
print(round(2.6655, 1))  # 第二个参数意为保留一位小数
print(round(2.6655, 2))  # 第二个参数意为保留两位小数

# pow 求次方
print(pow(3, 3))
print(3 ** 3)

# max 求最大值
print(max([23, 45, 98, 156, 5]))
print(max(2, 8, 5, 9, 45))

# sum 使用
print(sum(range(50)))
print(sum([2, 4, 5, 7, 8]))
print(sum(range(3), 10))

# eval 执行表达式
a, b, c = 1, 2, 3
print('动态执行的函数={}'.format(eval('a*b+c-10')))


def TestFun():
    print("我执行了吗？")
    pass


eval('TestFun')  # 没执行
eval('TestFun()')  # 可以调用函数执行

# ------------------------------------------------------类型转换函数

# 类型转换函数
print(bin(10))  # 转换二进制
print(hex(23))  # 转换十六进制

# 元组转换为列表
tup = (1, 2, 3, 4, 5)
print(type(tup))  # 元组
li = list(tup)  # list强制转换为列表
print(type(li))  # 列表
li.append('强制转换成功')  # 列表可以修改，元组不可以
print(li)

# 列表转换元组
tupl = tuple(li)
print(type(tupl))

# 字典操作 dict()
dic = dict()
print(type(dic))
dic['name'] = '小明'  # 追加内容
dic['age'] = 28
print(dic)

dic2 = dict(name='小红', age=28)  # 创建时就添加内容
print(dic2)

# bytes 转换
print(bytes('啊啦啦啦', encoding='utf-8'))  # 第二个参数是指定转换成什么
print(bytes('中', encoding='utf-8'))

# ------------------------------------------------------序列操作
# 序列操作
# 序列：str、 元组、 list

# all()  result:bool  对象中的元素除了是0、空、FALSE外都算TRUE, 所有的元素都为True--结果才为True
print(all([]))  # 空列表-true
print(all(( )))  # 空元组-true
print(all([1, 2, 4]))
print(all((1, 2, 3)))

print(all([1, 2, '']))  # 有空-FALSE
print(all([1, 2, None]))  # 有空-FALSE
print(all([1, [], 2]))  # 有空-FALSE
print(all([1, 2, 4, False]))  # 有False-FALSE
print(all((3, 4, 0)))  # 有0-FALSE

# any  result:bool  类似于逻辑运算符or的判断，只要有一个元素为True--结果就为True
print(any(('', False, 0)))  # 全为空/False/0才为False，否则为True
print(any((1, '')))
print(any([1, 2, 3]))


# sort 和 sorted ----------------------------------------
# sort方法只能用于列表，因为sort是直接修改原对象。而元组是不可变的，一旦创建无法改变，所以sort不能用于元组
# sorted可以用于元组，因为sorted是生成新的对象，在新对象上进行排序；或者说排完之后把数据弄到新对象里，与原对象就无关了。

li = [2, 15, 61, 23, 10]
li.sort()  # list排序方法，直接修改的是原始对象。改变地址上的数值
print(li)  # 打印原始对象

li = [2, 15, 61, 23, 10]
print('原对象排序之前：{}'.format(li))
newli1 = sorted(li)
newli2 = sorted(li, reverse=True)
print('原对象排序之后：{}'.format(li))  # 原始对象没变化
print('新对象排序之后：{}'.format(newli1))
print('新对象排序之后/降序排序：{}'.format(newli2))

# 元组
tup = (2, 45, 1, 67, 23, 10)
newtup1 = sorted(tup)
newtup2 = sorted(tup, reverse=True)
print(newtup1)
print(newtup2)

# range
for i in range(1, 11, 2):
    print(i)
    pass
print(range(1, 11, 1))
print(range(1, 11, 3))


# zip():  就是用来打包的，会把序列中对应的索引位置的元素存储为一个元组---------------------
s1 = ['a','b','c']
s2 = ['你','我','他']
# 压缩一个列表
print(zip(s1))
print(list(zip(s1)))  # 转换成列表展示里面的数据。里面每个元素都是一个元组（'a',）
# 压缩两个列表，不同序列相同索引的元素打包在一起储存成一个元组
zipList = zip(s1,s2)
print(zipList)
print(list(zipList))   # 转换成列表展示里面的数据

# 如果可迭代对象的元素个数不一样，那么按照最少的那个迭代压缩最少元素进行可迭代对象结束后退出
s3 = ['你','我','他','哈哈','呼呼']
print(zip(s2,s3))
print(list(zip(s2,s3)))

# 图书管理的函数 -----------------------------------------
def printBookInfo():
    books = []  # 存储所有图书信息
    id = input('请输入编号：（每个项以空格分割）')  # str
    name = input('请输入书名：（每个项以空格分割）')  # str
    pos = input('请输入位置：（每个项以空格分割）')  # str
    idList = id.split(' ')  # 以空格分割输入的数据成list
    nameList = name.split(' ')
    posList = pos.split(' ')

    bookInfo = zip(idList, nameList, posList)
    # print(type(bookInfo))
    # print(bookInfo)
    # print(list(bookInfo))

    for i in bookInfo:
        '''
        遍历图书信息进行存储
        '''
        dictInfo = {'编号': i[0], '书名': i[1], '位置': i[2]}
        books.append(dictInfo)  # 将字典对象添加到list容器中
        pass
    for item in books:
        print(item)
        pass

    pass

# 调用函数
printBookInfo()


# enumerate 枚举/列举 函数用于将一个可遍历的数据对象 -------------------------------------------
# (如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
# 一般用在 for 循环当中
# 能接收序列、字典。。。
listObj = ['a', 'b', 'c']
for item in enumerate(listObj):  # 结果是给之前的元素列表每一个元素加了一个索引，默认情况下与下标一致
    print(item)  # 每个item是元组类型

listObj = ['a', 'b', 'c']
for index, i in enumerate(listObj):
    print(index, i)

listObj = ['a', 'b', 'c']
for item in enumerate(listObj, 5):  # 第二个参数指索引从5开始
    print(item)

# 遍历字典
dic = {}
dic['name'] = 'ab'
dic['age'] = 28
dic['hobby'] = 'sing'
for item in enumerate(dic):  # item是个元组
    print(item)
for item in enumerate(dic.items(), 1):  # 字典.items()获取元组
    print(item)


# ------------------------------------------------------set集合
# 创建集合:
set1 = {'1', '2'}
set2 = {1, 2, 3}
set3 = {()}  # 空集合
print(type(set1))
print(type(set2))
print(type(set3))

dic = {}  # 空字典
print(type(dic))

# 集合是不重复的
set1 = {1, 2, 5, 3, 2, 1, 4, 1, 2, 1, 2}  # 纯数字：去重，正序排序
print(set1)  # {1, 2, 4, 5}

set2 = {3, 2.1, 2, 5}  # 若无重复的数字：不会排序，按照原顺序
print(set2)

set3 = {3,2,1,'嘿','啦','4','qq'}  # 数字和非数字参杂：随机顺序。（但大概率数字被排序
print(set3)

# 添加操作
set1.add('88')
print(set1)

# 清空操作
set1.clear()
print(set1)

# 取差集
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(a.difference(b))  # a中存在而b中不存在的
print(b.difference(a))  # b中存在而a中不存在的
print(a-b)
print(b-a)

# 取交集
print(a.intersection(b))
print(a&b)

# 并集
print(a.union(b))
print(a | b)

# pop 从集合中拿出数据并且删除 ----------------
# 集合里只有数字：
set1 = {5, 2, 1, -9}
s1 = set1.pop()  # 元素是数字时, 删除非负的最小的数字, 剩余数字升序排列
print('拿出：{}'.format(s1))  # 拿出的是非负的最小数值
print('剩下：{}'.format(set1))  # 并给剩下的元素从小到大排序

set2 = {'你', '我', '他'}  # 集合里无数字
s2 = set2.pop()   # 元素非数字时, 随机删除一个元素, 其余元素随机排序
print('拿出：{}'.format(s2))  # 随机拿出一个
print('剩下：{}'.format(set2))   # 剩余的元素随机排序

set3 = {3, 2, 1, '你', '我', '他'}  # 集合里既有数字又有非数字
s3 = set3.pop()   # 元素既有数字又含非数字时, 可能删除数字/非数字。如果删除的是数字, 则一定删最小的, 否则随机删除一个非数字元素
print('拿出：{}'.format(s3))  # 随机拿出一个。如果删除的是数字, 则一定删最小的, 否则随机删除一个非数字元素
print('剩下：{}'.format(set3))   # 剩余的元素随机排序

# 指定移除元素
set1 = {5, 2, 1, -9}
set1.discard(5)
print(set1)

# 更新 update
set1 = {5, 2, 1, -9}
set2 = {1, 2, 3, 4}
set1.update(set2)
print(set1)
# 与并集相似但有不同：并集set1不变，将两集合的并集写道新的集合中； 更新则是将改变set1，将set1变成两集合的并集。

