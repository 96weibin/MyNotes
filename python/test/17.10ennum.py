
from enum import Enum, unique

status = Enum('status123', ('success', 'fild', 'pandding'))

print(status.success.value)     # 1
print(status.success.name)      # success
print(status(1))                # status.success

@unique
class Weekday(Enum):
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = '周五'
    Sat = 6
    Sun = 7
    Sun = 11
    pass

print(Weekday.Fri.name)     # Fri
print(Weekday.Fri.value)    # '周五'