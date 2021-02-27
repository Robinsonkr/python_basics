#program to extract year, month, date and time using Lambda
import datetime

now = datetime.datetime.now()

print(now)

year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()


print(year(now))
print(month(now))
print(day(now))
print(t(now))

"""
2021-02-27 17:10:15.207045
2021
2
27
17:10:15.207045


"""