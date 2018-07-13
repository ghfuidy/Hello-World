def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        # pass
        print('代码不被接受')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


try:
    pass
except Exception:
    pass
#else and finally 接try或者except的步骤
else:
    pass
finally:
    pass

# f = open('testfile.txt')
# print(f.read())
try:
    f = open('testfile.txt')
    print(f.read())
except Exception:
    print('Sorry')

try:
    pass
except FileNotFoundError:
    print('Sorry,this file does not exists')
except Exception:
    pass

try:
    var = bad_var
except NameError as e:
    print(e)
else:
    print(var)
finally:
    print('excuting finally...')


def boxPrint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a singal character')
    if width <=2:
        raise Exception('Width must be greater than 2.')
    if height <=2:
        raise Exception('Height must be greater than 2.')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + ' ' * (width - 2) + symbol)
    
    print(symbol * width)

for sys, w, h in (('*', 4, 4),('0', 20, 5),('x', 1, 3),('zz', 3, 3)):
    try:
        boxPrint(sys, w, h)
    except Exception as err:
        print('An except happened: ' + str(err) + '\n')


#calulate n!
#阶乘
# def factorial(n):
#     total = 1
    
#     for i in range(n + 1):
#         total *= i
    
#     return total

# print(factorial(5))


import logging
#去除logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level = logging.DEBUG,format = ('%(asctime)s - %(levelname)s - %(message)s'))
logging.basicConfig(filename = 'myProgramLog.txt',level = logging.DEBUG,format = ('%(asctime)s - %(levelname)s - %(message)s'))
def factorial(n):

    logging.debug('Start of factorial({})'.format(n))

    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is {},total is {}'.format(i, total))
    
    logging.debug('End of factorial{}'.format(n))
    return total

print(factorial(5))
logging.debug("End")


# assertion
Wood_Hill = {'ns':'green', 'ew':'red'}
Stone_Scissor = {'ns':'red', 'ew':'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] ='red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    
    assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight)

switchLights(Wood_Hill)

# AssertionError: Neither light is red!{'ns':'green', 'ew':'yellow'}