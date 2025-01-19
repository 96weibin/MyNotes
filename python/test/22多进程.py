import os

print('pid %s' % os.getpid())
childProcessId = os.fork()  # 脚本会在 主线程 和 子线程执行，   子线程 得到 0

if childProcessId == 0:
    print('here is child, os pid : %s' % os.getpid())
else:
    print('here is main os pid: %s' % os.getpid())

# pid 35027
# here is main os pid: 35027
# here is child, os pid : 35028