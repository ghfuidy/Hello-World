myCatList = ['Garfiled','orange','fat']
myCat = {'name':'Garfiled','color':'orange','size':'fat'}
#字典没有顺序，而列表有顺序（方法：变换列表和字典中的项目顺序，并与变换之前的列表与字典做等价判断
yourCatList = ['Garfiled','fat','orange']
yourCat = {'name':'Garfiled','size':'fat','color':'orange'}

print(myCatList == yourCatList, myCat == yourCat)

print("My cat's name is :",myCatList[0])
print('My cat\'s name is :',myCat['name'])

myCat['citys'] = 'xiamen'

myCat['color'] = 'orange tabby'

print(myCat)
print(myCat.values())
print("字典的各个属性")
for v in myCat.values():
    print(v, end = '，')
print()

for v in myCat.keys():
    print(v, end = '，')
print()

for v in myCat.items():
    print(v, end = '，')
print()

print(myCat.get("name","not here"))

del myCat['citys']
print(myCat)

myCat.clear()
print(myCat)

myCat.setdefault('citys','noway')
print(myCat)

picnicItems  = {'apple':5, 'cup':10}
print('We have {} apples and {} eggs'.format(picnicItems.get('apple', 0),picnicItems.get('eggs',0)))

#记录生日
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
print(birthdays)

# while True:
#     name = input("Enter a name(blank to quit): ")
#     if name == '':
#         break
#     elif name in birthdays:
#         print('{} is the birthday of {}'.format(birthdays[name],name))
#     else:
#         print('I do not have birthday information for ', name)
#         bday = input('What is the birthday? ')
#         birthdays[name] = bday
#         print('birthday database updated')

# print(birthdays)

#批量发邮件
customers = []

while True:
    createEntry = input("Enter customer(yes/no)? ")
    createEntry = createEntry[0].lower()
    if createEntry == 'n':
        break
    else:
        fName, lName, gender = input('enter customer\'s name&gender:').split()
        customers.append({'fName':fName,'lName':lName,'gender':gender})

for cust in customers:
    if cust['gender'] =='male':
        title = 'Mr ' + cust['lName']
    else:
        title = 'Ms ' + cust['lName'] 
    print('''dear {}，
    As our distinguished customer,your ...
    '''.format(title))