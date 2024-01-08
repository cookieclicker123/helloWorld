import time

#print(time.ctime(1000000))

#print(time.time())

#print(time.ctime(time.time()))

#timeObject = time.localtime()
#print(timeObject)
#localTime = time.strftime("%B %D %Y %H: %M: %S", timeObject)
#print(localTime)

#timeString = "20 April, 2020"
#timeObject = time.strptime(timeString, "%d %B, %Y")
#print(timeObject)

timeTuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
timeString = time.asctime(timeTuple)

print(timeString)

timeTuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
timeString = time.mktime(timeTuple)

print(timeString)