import itertools

# """
# 排列（无重复）
# 4 - 3  -  24
# 4 - 2  -  12
# m - n  -  m!/(m-n)!
# """
# mylist1 = list(itertools.permutations([1, 2, 3, 4], 3))
# print(mylist1)
# print(len(mylist1))
#
# """
# 组合（无重复）
# 4 - 3  -  24
# 4 - 2  -  12
# """
# mylist2 = list(itertools.combinations([1, 2, 3, 4], 3))
# print(mylist2)
# print(len(mylist2))

"""
排列组合

"""
mylist3 = list(itertools.product([1, 2, 3, 4], repeat=4))
print(mylist3)
print(len(mylist3))


