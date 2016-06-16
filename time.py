import time
print(time.localtime())
for i in range(1, 61):
    t= time.localtime()
    year=t[0]
    month=t[1]
    day=t[2]
    hour=t[3]
    min=t[4]
    sec=t[5]
    print(year, month, day, hour,":",min,":",sec)
    time.sleep(1)