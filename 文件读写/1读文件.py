"""
1、打开文件
open(path, flag[, encoding][, errors])
path:要打开文件的路径
flag:打开方式
r:  以只读的方式打开文件，文件的描述符放在文件的开头
rb:   二进制                                  开头
r+:   打开一个文件用于读写                     开头
w:    打开一个文件用于写入，如果文件已经存在会覆盖，
      不存在就创建新文件
wb:     二进制
w+:     打开一个文件用于读写。如果该文件已存在则打开文件，
        并从开头开始编辑，即原有内容会被删除。
        如果该文件不存在，创建新文件
a:      追加  如果文件存在，文件描述符将会放在文件末尾
        如果不存在将创建新文件
a+:     追加，读写                               末尾
encoding:编码方式
errors:错误处理 "ignore"为忽略错误
"""