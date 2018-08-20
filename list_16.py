import random
# numList = []
# for i in range(5):
#     numList.append(random.randrange(1,9))

# print(numList)
# #排序
# numList.sort()
# print(numList)

# numList.sort(reverse = True)
# print(numList)
# #相似倒排
# numList.reverse()
# print(numList)
# #序号4位置上插入10
# numList.insert(4,10)
# print(numList)
# #移除数字10
# numList.remove(10)
# print(numList)
# #移除位置2
# numList.pop(2)
# print(numList)
# #返回一个新列表sorted，对原列表无影响
# print(sorted(numList))
# print(numList)

# PI = 3.14
# tup = (9,2,3,1,3,4,5)
# print(tup)
# print(max(tup))
# s_tup = sorted(tup)
# print(s_tup)

# #随机挑选
# students = ["Tom", "Joke","郭靖","小龙女"]
# print(random.choice(students))


# nList = [i*2 for i in range(10)]
# print(nList)

# numList = [1,2,3,4,5]
# print(numList)

# pList = [pow(i,3) for i in numList]
# print(pList)


# list0fValue = [[pow(i,2),pow(i,3),pow(i,4)] for i in numList]
# print(list0fValue)

# print()
# for k in list0fValue:
#     print(k)
# print()

# print("hope" * 3)
# print([0] * 10)

# multiDList = [[0] * 10 for i in range(10)]
# for k in multiDList:
#     print(k)
# print()
# #二维数组0行1列的数值改为10
# multiDList[0][1] = 10
# for k in multiDList:
#     print(k)
listTable = [[0] * 10 for i in range(10)]
for i in range(10):
    for j in range(10):
        listTable[i][j] = i * j

for i in range(1,10):
    for j in range(1,10):
        print(listTable[i][j],end = '||')
    print()