import pickle   # 数据持久性模块


# 写文件时会造成乱码
mylist = [1, 2, 3, 4, 5, 6, 7, "songxk"]
path = r"C:\Users\宋兴可\Desktop\算法与数据结构\0430\test1.txt"
f = open(path, "wb")
pickle.dump(mylist, f)
f.close()

f1 = open(path, "rb")
tempList = pickle.load(f1)
print(tempList)
f1.close()


