import pprint
message = '''
books and doors are the sanme thing.
you open them, and you go through into another world.
'''
words = message.split()
count = {}
for word in words:
    if not word[-1].isalpha():
        word = word[:-1]
    word = word.lower()
    count.setdefault(word,0)
    count[word] +=1

pprint.pprint(count)


#guest & items
def totalBrought(guests, item):
    numBrought = 0

    for v in guests.values():
        numBrought += v.get(item,0)

    return numBrought

allGuests = {'alice':{'apple': 5, 'pretzels':12},
            'bob':{'ham sandwitches':3 ,'apple': 2},
            'carol':{'cups': 3, 'apple pies': 1}}

print("Number of things being brought:\n")
# print("-Apple                     {}".format(totalBrought(allGuests,'apple')))
# print("-Cups                      {}".format(totalBrought(allGuests,'cups')))
# print("-prtzels                   {}".format(totalBrought(allGuests,'pretzels')))
# print("-ham sandwitches           {}".format(totalBrought(allGuests,'ham sandwitches')))
# print("-apple pies                {}".format(totalBrought(allGuests,'apple pies')))

foodSet = set()
for v in allGuests.values():
    foodSet |= set(v)
print(allGuests.values())
for food in foodSet:
    print("-{:20}      {}".format(food, totalBrought(allGuests, food)))


#集合
items = {"arrow","spear","arrow","arrow","rock"}
print(items)
print(len(items))

# if "rock" in items:
#     print("Rock exist")
# else:
#     print("Not found")

# pets = set()
# pets.add("cat")
# pets.add("dog")
# pets.add("gerbil")
# print(pets)
# pets.discard('cat')
# print(pets)
# pets.discard('zebra')
# #delelt删除一个不存在的条目会报错

# numbers1 = {1,2,3,4,7}
# numbers2 = {1,3,4,6}
# print(numbers1 | numbers2)
# print(numbers1 & numbers2)
# print(numbers1 - numbers2)
# numbers2.update([10,20,40,50])
# print(numbers2)

# dict1 = {"cat": 1, "dog": 2, "bird": 3}
# print(dict1)
# keys = set(dict1)
# print(keys)

# for i in set('apple'):
#     print(i, end =",")


#循环遍历嵌套字典或列表
def get_target_value(key, dic, tmp_list):
    # """
    # :param key: 目标key值
    # :param dic: JSON数据
    # :param tmp_list: 用于存储获取的数据
    # :return: list
    # """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '

    if key in dic.keys():
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
    else:
        for value in dic.values():  # 传入数据不符合则对其value值进行遍历
            if isinstance(value, dict):
                get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
            elif isinstance(value, (list, tuple)):
                _get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
    return tmp_list


def _get_value(key, val, tmp_list):
    for val_ in val:
        if isinstance(val_, dict):  
            get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            _get_value(key, val_, tmp_list)   # 传入数据的value值是列表或者元组，则调用自身