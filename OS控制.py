import os


"""
包含了普遍的操作系统的功能
"""

# 获取操作系统的类型(Window:nt   Linux,Unix,Mac OS:posix)
# print(os.name)
#
# # 打印操作系统的详细信息，Windows不支持
# # print(os.uname())
#
# # 获取操作系统所有的环境变量
# print(os.environ)
#
# # 获取指定环境变量
# print(os.environ.get("APPDATA"))
#
# # 获得当前目录
# print(os.curdir)
#
# # 获取当前工作目录，即当前python脚本所在的目录
# print(os.getcwd())
#
# # 以列表形式返回指定目录下的所有文件
# print(os.listdir(r"C:\Users\宋兴可\Desktop\算法与数据结构"))
#
# # 在当前目录下创建/删除新目录
# os.mkdir("songxk")
# os.rmdir("songxk")
#
# # 获取文件属性
# print(os.stat("test.txt"))
#
# # 重命名
# os.rename("test.txt", "abc")
#
# # 删除普通文件
# os.remove("test.txt")

# 运行shell命令
os.system("notepad")


