# 判断语句与循环控制
"""
流程：就是计算机执行代码的顺序
流程控制：对计算机代码执行的顺序进行有效的管理，只有流程控制才能实现在开发当中的业务逻辑
流程控制的分类：
	1.顺序流程:就是代码一种自上而下的执行结构，也是python默认的流程
	2.选择流程/分支流程:根据在某一步的判断，有选择的去执行相应的逻辑的一种结构
	   2.1 单分支
	   		if 条件表达式:
	   			一条条的python代码
	   			.......
	   2.2 双分支
	   		if 条件表达式:
	   			一条条的python代码
	   			.......
	   		else:
	   			一条条的python代码
	   			.......
	   2.3 多分支
			if 条件表达式:
	   			一条条的python代码
	   			.......
	   		elif 条件表达式:
	   			一条条的python代码
	   			.......
	   		elif  条件表达式:
	   			一条条的python代码
	   			.......
	   		.....
	   		else:
	   			一条条的python代码
	   			....
	   	条件表达式:比较运算符/逻辑运算符/复合的运算符

	3.循环流程：在满足一定的条件下，一直重复的去执行某段代码的逻辑【事情】

	 	while 条件表达式:
	 			一条条的python代码
	   			.......
	   	for ... in  可迭代集合对象:
	   		    一条条的python代码
	   			.......

while使用：适用于对未知的循环次数 【用于判断】
for使用：适用于已知的循环次数【可迭代对象遍历】
"""

# -----------------------------------------
'''while ******************
---语法结构
    while 条件表达式:
          代码指令
---语法特点
    1.有初始值
    2.条件表达式
    3.变量【循环体内计数变量】的自增自减, 否则会造成死循环
---使用条件：循环的次数不确定，是依靠循环条件来 结束
---目的: 为了将相似或者相同的代码操作变得更加简洁，使得代码可以重复利用
'''

'''for ******************
---语法特点: 遍历操作，依次的取集合容器中的每个值
---语法结构：
    for 临时变量 in 容器:
        执行代码块
---其他
    1.可以遍历字符串
    
---range函数：此函数可以动态的生成一个数据集合列表（集合对象）
    range(起始:结束:步长)  步长不能为0
    range默认从0开始，步长为1
'''

'''break和continue ******************
---break：代表中断结束；若满足条件直接从本层循环体中彻底跳出结束
---continue：只结束本次循环，继续的进行下次循环（当continue的条件满足的时候，本次循环剩下的语句将不再执行，后面的循环继续走
---特点：这两个关键字只能用在循环中
'''

'''for--else/while--else 特殊用法 ******************
--- 若for->else，则循环后执行else之后的代码
--- 若for->break->else，则break退出循环之后不会执行else之后的代码。利用这个特性可以做一些特殊的业务逻辑
    eg: 输入账号密码时，输错三次就提示被锁定；输入正确则不提示
'''

# ******************************************
# ---------------------------------------------------选择流程/分支流程
# 单分支******
score = 60
if score <= 60:
    print('成绩不是太理想，要继续努力')
    pass  # 表示一个空语句，‘跳过’
print("end")

score = 80
if score <= 60:
    print('成绩不是太理想，要继续努力')
    pass  # 表示一个空语句，‘跳过’
print("end")

# 双分支******
if score > 60:
    print("成绩合格")
    pass
else:
    print("成绩不合格")
    pass
print("end")

# 多分支******
score1 = int(input("请输入成绩："))  # 需要转换类型才能和数字比较
if score1 > 90:
    print("优秀A")
    pass
elif score1 >= 80:
    print("B")
    pass
elif score1 >= 70:
    print("C")
    pass
elif score1 >= 60:
    print("D")
    pass
else:
    print("不合格")
    pass
print("end")

# ---------------------------------------------------if-elif-else猜拳小游戏
import random

# 计算机 人
person = int(input("请出拳：【0：石头  1：剪刀  2：布】"))
computer = random.randint(0, 2)
if person == 0 and computer == 1:
    print("you win")
    pass
elif person == 1 and computer == 2:
    print("you win")
    pass
elif person == 2 and computer == 0:
    print("you win")
    pass
elif person == computer:
    print("break even")
    pass
else:
    print("you lost")
    pass
print("end")

# ---------------------------------------------------if-else多层嵌套
xuefen = int(input("请输入你的学分"))
if xuefen > 3:
    grade = int(input("请输入成绩"))
    if grade < 80:
        print("成绩不达标")
        pass
    else:
        print("可以升班")
        pass
    pass
else:
    print("学分不够")
    pass
print("end")


# ******************************************
# ---------------------------------------------------while循环

# 输出1-100
index = 1
while index <= 100:
    print(index)
    index += 1
    pass
print("end")

# ---------------------------------------------------猜拳小游戏改进while+if
import random
# 计算机 人
count = 1
while count <= 10:
    person = int(input("请出拳：【0：石头  1：剪刀  2：布】"))
    computer = random.randint(0, 2)
    if person == 0 and computer == 1:
        print("you win")
        pass
    elif person == 1 and computer == 2:
        print("you win")
        pass
    elif person == 2 and computer == 0:
        print("you win")
        pass
    elif person == computer:
        print("break even")
        pass
    else:
        print("you lost")
        pass
    count += 1
print("end")

# ---------------------------------------------------打印九九乘法表
# 1
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d " % (row, col, row * col), end='')  # print 默认打印完后换行，若不想让他换行就加一个参数end使其为’‘
        col += 1
        pass
    print()  # 换行
    row += 1
    pass
print("end")

# 2
row = 9
while row >= 1:
    col = 1
    while col <= row:
        print("%d * %d = %d " % (row, col, row * col), end='')
        # print默认打印完后换行，若不想让他换行就加一个参数end使其为’‘，则输出时以引号中的东西作为结尾
        col += 1
        pass
    print()  # 换行
    row -= 1
    pass
print("end")


# ---------------------------------------------------打印直角三角形
# 1
row = 1
while row <= 7:
    col = 1
    while col <= row:
        print("*", end="  ")
        col += 1
        pass
    print()
    row += 1
    pass
print("end")

# 2
row = 7
while row >= 1:
    col = 1
    while col <= row:
        print("*", end="  ")
        col += 1
        pass
    print()
    row -= 1
    pass
print("end")

# ---------------------------------------------------打印等腰三角形
row = 1
while row <= 10:
    j = 1
    while j <= 10 - row:  # 控制打印空格的个数
        print(" ", end="")
        j += 1
        pass
    col = 1
    while col <= 2 * row - 1:  # 控制打印*的个数
        print("*", end="")
        col += 1
        pass
    row += 1
    print()
    pass
print("end")


# ******************************************
# ---------------------------------------------------for遍历字符串
tags = '噜啦啦噜啦啦噜啦啦啦啦' # 字符串类型本身就是一个字符类型的集合
for item in tags:
    print(item)
    pass


# ******************************************
# ---------------------------------------------------range函数
print(type(range(1, 100)))

# ---------------------------------------------------range函数输出1-100
for data in range(1,101):  # 数据是左包含右不包含
    print(data, end=' ')   # 每个输出不换行，用空格隔开
    pass

# ---------------------------------------------------range函数求累加和1-100
sum = 0
for data in range(1, 101):
    sum += data
    pass
print("sum=%d" % sum)

# ---------------------------------------------------range函数50-200输出奇数偶数
for data in range(50, 201):
    if data % 2 == 0:
        print("%d是偶数" % data)
        pass
    else:
        print("%d是奇数" % data)
    pass

# ---------------------------------------------------for range 九九乘法表
for i in range(1,10):  # 一共9行
    for j in range(1, i+1):
        print("%d*%d=%d" % (i, j, i*j), end=" ")
        pass
    print()  # 换行
    pass


# ******************************************
# ---------------------------------------------------break 1-51求和，当和大于100时停止
sum = 0
for item in range(1, 51):
    if sum > 100:
        print("循环执行到%d时退出" % item)
        break  #退出循环体
        pass
    sum += item
    pass
print("sum=%d" % sum)

# ---------------------------------------------------continue 只输出1-100的奇数
for item in range(1, 101):
    if item % 2 == 0:
        continue
        print("在continue后面会不会执行呢")
        pass
    print(item)
    pass

# ---------------------------------------------------
for item in 'I love you':   # 若遇到e就不走后面
    if item == 'e':
        break
    print(item, end="")

for item in 'I love you':   # 若遇到e跳过继续后面的
    if item == 'e':
        continue
    print(item, end="")


# ******************************************
# ---------------------------------------------------for->else
for item in range(1, 11):
    print(item, end=' ')
    pass
else:
    print('上面循环结束后，else的代码会执行')

# ---------------------------------------------------for->break->else
for item in range(1, 11):
    print(item, end=' ')
    if item >= 5:
        break
    pass
else:
    print('就是在上面循环当中 只要是出现了break 那么else的代码将不在执行')

# ---------------------------------------------------for-break-else模拟输错三次进行警告，输入正确则不警告
account = 'wy'
pwd = '123'
for i in range(3):
    a = input('请输入账号:')
    p = input('请输入密码:')
    if account==a and pwd==p:
        print("登录成功")
        break
        pass
    pass
else:
    print("账号密码已经输入三次，被系统锁定")

# ---------------------------------------------------for->break->else
index=1
while index<=10:
    print(index)
    if index==6:
        break
    index+=1
    pass
else:
    print('else执行了吗.....')