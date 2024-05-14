
def oldRead(path):
    try:
        f = open('./a.txt', 'r', encoding='utf-8')  # encoding  设置字符集
        print(f.read())
    finally:
        if f:
            f.close()

# oldRead('./a.txt')

def withRead(path):     # with 写法不需要手动 close()
    with open(path, 'r',  encoding='utf-8') as f:
        print(f.read())

# withRead('./a.txt')


def loopRead(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip() + '1234')

# loopRead('./a.txt')

def byteRead(path):
    with open(path, 'rb') as f:     # 读取二进制文件
        print(f.read())

# byteRead('./a.png')


def writeFile(path):
    with open(path,'w', encoding='utf-8') as f:
        f.write('整的挺不错')


writeFile('./a.txt')
withRead('./a.txt')

