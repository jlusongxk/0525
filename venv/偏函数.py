#print(int("123", base=10)) #将123作为十进制数处理
# print(int("10101", base = 2))#将10101作为二进制数处理
#
# # 偏函数
# def int2(str, base = 2):
#     return int(str, base)
#
# print(int2("10101"))
import functools

# 把一个参数固定住，形成一个新的函数
int3 = functools.partial(int, base = 2)

