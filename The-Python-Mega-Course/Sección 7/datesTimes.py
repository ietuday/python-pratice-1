'''
to obtain the day, and the time we use the now() method.
i.e: datetime.datetime.now()

strftime.org
to get more information about what else can we get from a datetime object

import time.
we use time to, for example, hold the program for a certain amount of time
time.sleep(1)

the programs stops for a second 
'''
import datetime

now  = datetime.datetime.now() #takes datetime from the system
yest = datetime.datetime(2016,11,19,11,0,0,0) #manually

delta=now-yest
days = delta.days
seconds = delta.total_seconds()


print(delta) #this is a timeDelta
print(days)
