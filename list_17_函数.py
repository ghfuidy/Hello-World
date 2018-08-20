def allotEmail(firstname,surname):
    return firstname + '.' + surname + '@pythonabc.org'

# name = input('Enter your name :')
# fName,sName = name.split()
# compEmail = allotEmail(fName,sName)

# print('your company email: \n',compEmail)


def mult_divide(num1,num2):
    return (num1*num2), (num1/num2)

# mult, divide = mult_divide(5,4)

# print('5 * 4 =', mult)
# print('5 / 4 =', divide)


# 函数内部的变量为局部变量（函数），如果在变量前加global会变成全局变量

#判断素数
def isprime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def getPrimes(numMax):
    primes = []
    for num1 in range(2, numMax):
        if isprime(num1):
            primes.append(num1)
    return primes

# maxNum = int(input('search for primes up to: '))

# listofPrimes = getPrimes(maxNum)

# for prime in listofPrimes:
#     print(prime,end = ', ')


import math

a1 = math.ceil(4.4)
a2 = math.floor(4.4)
a3 = math.fabs(-4.4)
a4 = math.factorial(4)
a5 = math.fmod(5,4)
a6 = math.trunc(4.2)
a7 = math.pow(2,3)
a8 = math.sqrt(9)
a9 = math.e
a10 = math.pi

# print(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)


def get_area(shape):
    shape = shape.lower()

    if shape == 'recatangle':
        rectangle_area()
    elif shape == 'circle':
        circle_area()
    else:
        print('please enter rectangle or circle')

def rectangle_area():
    length = float(input('enter the length'))
    width = float(input('enter the width'))
    area = length * width
    print(area)

def circle_area():
    radius = float(input('enter the radius'))
    area = math.pi * math.pow(radius, 2)
    print(area)


def mouse_area():
    pass

shape_type = input('get area for what hsape: ')

get_area(shape_type)