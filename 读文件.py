# coding: utf-8


path = r"C:\Users\宋兴可\Desktop\算法与数据结构\0430\test.txt"
f = open(path, "a")
# 将文件写入缓冲区
f.write("Mr.song is a good man\n")
# 直接把内部缓冲区的数据立刻写入文件
# 而不是被动的等待关闭文件时自动刷新缓冲区写入
f.flush()

f.close()