from datetime import datetime

now = datetime.now()

# dt = datetime(2024, 7, 32, 25,61,61)    # can out range
dt = datetime(2024, 5, 5, 17, 40, 33)
print(now, dt)

# timestamp 

nowStamp = now.timestamp() # 距1970  秒
print(nowStamp)

