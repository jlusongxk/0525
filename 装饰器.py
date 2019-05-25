"""
概念：是一个闭包，把一个函数当成参数，返回一个替代版的函数
    本质上就是一个返回函数的函数
"""


# 简单的装饰器
def func1():
    print("sun is a good man")


def outer(func):
    def inner():
        print("*****")
        func()
    return inner


f = outer(func1)
f()


# 复杂一点的装饰器
def say(age):
    print("He is %s years old" % age)


def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner


say = outer(say)
say(-10)


# 通用装饰器
def outer(func):
    def inner(*args, **kwargs): # 不定长参数，关键字
        # 添加修饰的功能
        print("************")
    return inner
