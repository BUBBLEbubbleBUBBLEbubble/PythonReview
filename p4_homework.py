# 1.写函数，接收n个数字，求这些参数数字的和
# 2.写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
# 3.写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。PS:字典中的value只能是字符串或列表

# 1.-----------------------------------------------------
def sumFunc(*args):
    result = 0
    for item in args:
        result += item
        pass
    return result
# 调用
rs = sumFunc(1, 2, 3, 4, 5)  # 传列表, 变量接受
print('rs={0}'.format(rs))  # format格式化输出

def sumFunc(*args):
    result = 0
    for item in args:
        result += item
        pass
    return result
# 调用
rs = sumFunc(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # 传列表, 变量接受
print('rs=%d' % rs)



# 2.-----------------------------------------------------
def processFunc(con):
    '''
    处理接受的数据，返回奇数索引的数据
    :param con: 可变长的阐述，可以接受一个列表/元组
    :return: 新的列表对象
    '''
    print(type(con))
    listNew = []
    index = 1
    for i in con:
        if index % 2 == 1:  # 判断奇数位
            listNew.append(i)
            pass
        index += 1
        pass
    return listNew
    pass


rs3 = processFunc([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(rs3)

rs5 = processFunc(range(1, 20))
print(rs5)

rs4 = processFunc(tuple(range(1, 20)))  # 因为用range生成的并不是元组类型，所以需要强制转换成元组类型
print(rs4)


# 3.-----------------------------------------------------
def dictFunc(dictParms):  # 也可写成 **kwargs
    '''
    处理字典类型的数据，
    :param dictParm: 字典
    :return: 字典
    '''
    result = {}
    for key,value in dictParms.items():  # key-value
        if len(value) > 2:
            result[key] = value[:2]  #向结果字典添加数据
            pass
        else:
            result[key] = value
            pass
        pass
    return result
    pass
dectObj = {'name':'小王', 'hobby':['画画','唱歌','跳舞','打球'], 'pro':'中国艺术'}
print(dictFunc(dectObj))
