# ###time
# import time

# # print(time.time())
# # ###calculate time spend
# # def calcProd():
# #     product = 1
# #     for i in range(1, 100000):
# #         product = product * i
# #     return product

# # startTime = time.time()
# # prod = calcProd()
# # endTime = time.time()
# # print('The result is {} digits long'.format(len(str(prod))))
# # print('Take {} seconds to calculate'.format(endTime - startTime))

# ###time.sleep()
# # for i in range(3):
# #     print('Trick')
# #     time.sleep(1)
# #     print('Trick')
# #     time.sleep(3)

# ###print style
# # now = time.time()
# # print(now)
# # print(round(now))
# # print(round(now, 2))
# # print(round(now, 4))

# ###stopwatch progress
# print('Press Enter to begin. Afterwards, press ENTER to click the stopwatch'
# 'Press Ctrl-C(Windows) Command_F2(Mac) to quit.')

# input()
# print('Started.')
# startTime = time.time()
# lastTime = startTime
# lapNum = 1

# try:
#     while True:
#         input()
#         lapTime = round(time.time() - lastTime, 2)
#         totalTime = round(time.time() - startTime, 2)
#         print('Lap #{}: {} ({})'.format(lapNum, totalTime, lapTime), end='')
#         lapNum += 1
#         lastTime = time.time()
# except KeyboardInterrupt:
#     ###Handle the Command_F2 or Crtl-C exceptopn to keep its error message
#     print('\nDone.')

import datetime
import time

print(time.time())
print(datetime.datetime.fromtimestamp(time.time()))

dn = datetime.datetime.now()

print(dn)
print('year:{}, month:{}, day:{}, '
'hour:{}, minute:{}, second:{}'.format(dn.year,dn.month,dn.day,dn.hour,dn.minute,dn.second))

dt = datetime.datetime(2017, 12, 20, 19, 16, 0)
print('year:{}, month:{}, day:{}, '
'hour:{}, minute:{}, second:{}'.format(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second))

###creat a timedelta object(which is duration of time)
delta = datetime.timedelta(weeks=1, days=11, hours=10, minutes=9, seconds=8)
print(delta.days,delta.microseconds)
print(str(delta))

dt = datetime.datetime.now()
thousandsDays = datetime.timedelta(days=1000)
print(dt + thousandsDays)
print(dt - thousandsDays)

###定时程序
# newYear2018 = datetime.datetime(2018, 1, 1)
# while datetime.datetime.now() < newYear2018:
#     time.sleep(1)

oct21st = datetime.datetime(2018, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of %y"))

print(datetime.datetime.strptime('October of 21, 2015', '%B of %d, %Y'))