# 求三组连续自然数的和：求出1到10、20到30和35到45的三个和
# 100个和尚吃100个馒头，大和尚一人吃3个馒头，小和尚三人吃1个馒头。请问大小和尚各多少人？
# 指定一个列表，列表里含有唯一一个只出现过一次的数字。写程序找出这个“独一无二”的数字

def sumRange(m,n):
    '''
    求从m到n的连续自然数的综总和
    :param m: 开始值 int
    :param n: 结束值 int
    :return:
    '''
    return sum(range(m,n+1))
    pass
print(sumRange(1,10))
print(sumRange(20,30))

def personCount():
    '''
    计算有多少个和尚
    假设大和尚a个，小和尚b个(100-a
    :return:
    '''
    for a in range(1,100):
        if a*3 + (100-a)*(1/3) == 100:
            return (a,100-a)
        pass
    pass
rs = personCount()
print('大和尚{}人，小和尚{}人'.format(rs[0],rs[1]))


li = [1,2,3,4,5,6,7,8,9,10,8,7,6,5,4,3,2,1]
set1 = set(li)  # 去重之后
print('去重之后的集合：{}'.format(set1))
for i in set1:
    li.remove(i)  # 去掉去重之后的不重复集合
    pass
print('有重复的部分：{}'.format(li))
set2 = set(li)  # 这剩下的是重复的部分
# set3 = set1-set2
# print('只出现一次的数字：{}'.format(set3))
for i in set1:
    if i not in set2:
        print(i)
        pass
    pass
