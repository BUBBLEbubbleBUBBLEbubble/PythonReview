# 1--------------------------------------------------------------------------------
# 猜年龄小游戏，有三点需求
# 1.允许用户最多尝试3次
# 2.每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y， 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
# 3.如何猜对了，就直接退出
# 目的：演练while的使用和if使用  综合运用

# times=0
# count=3
# while times<=3:
#     age=int(input('请输入您要猜的年龄...'))
#     if age==25:
#         print('恭喜您猜对了....')
#         break #直接中断循环
#         pass
#     elif age>25:
#         print('猜大了,请在试试')
#         pass
#     else:
#         print("猜小了,请在试试'")
#         pass
#     times+=1
#     if times==3:
#         choose=input('想不想继续猜呢 Y/N？')
#         if choose=='Y' or choose=='y':
#             times=0 #重置为初始值
#             pass
#         elif choose=='N' or choose=='n':
#             times==4
#             pass
#         else:
#             print('请输入正确的标记...谢谢配合')
#     pass


# 2--------------------------------------------------------------------------------
# 小王身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小王计算他的BMI指数，并根据BMI指数：
# 低于18.5
# 过轻18.5-25：
# 正常25-28：
# 过重28-32：
# 肥胖高于32：
# 严重肥胖
#演练目的： 用if-elif判断并打印结果

# height=1.75
# weight=80.5
# BMI=weight/(height**2)
# print("BMI的数据是%d"%BMI)
# if BMI<18.5:
#     print('小王啊 不行啊，需要加强营养 加强锻炼')
#     pass
# elif 18.5<=BMI<25:
#     print('标准体重')
#     pass
# elif 25<=BMI<28:
#     print('有点微胖')
#     pass
# elif 28<=BMI<32:
#     print('体重肥胖...')
#     pass
# else:
#     print('严重肥胖 马上减肥....')





