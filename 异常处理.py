"""
try……except……else
格式：
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
except 错误码 as e:
    语句3
else:
    语句e
finally:
    语句f

作用：用于检测try语句块中的错误，
        从而让except语句捕获错误语句并处理
注意：else语句可有可无
逻辑：当程序执行到try-except-else语句时
如果try“语句t”执行出错，会逐个第一个错误码

"""
# try:
#     print(3 / 0)
# except ZeroDivisionError as e:
#     print("除数不能为0")
#
# # 使用except而不使用任何的错误类型
# try:
#     print(4/0)
# except:
#     print("程序出现异常")
#
#
# # 使用except处理多种异常
# try:
#     pass
# except (NameError, ZeroDivisionError):
#     print("出现了NameError或ZeroDivisionError错误")

# try:
#     print(5/0)
# except BaseException as e:
#     print(e)

# 2、跨越多层调用
# def func1(num):
#     print(1/num)
# def func2(num):
#     func1(num)
# def main():
#     func2(0)
#
# try:
#     main()
# except ZeroDivisionError as e:
#     print("***")


# 断言
def func(num, div):
    assert (div != 0), "div 不能为 0"
    return num / div


print(func(10, 0))

