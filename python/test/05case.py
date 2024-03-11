source = input("source: ")

match source:
    case "A":
        print("hello A")
    case '11' | '12' | '13':    # | 或
        print("hello tean")
    case x if int(x) > 50:      # if 条件
        print("hello old man")
    case _:                     # default
        print('hello any one')

args = ['gcc', 'hello.c', 'world.c', 'I','like you']
# args = ['gcc', 'hello.c']
# args = ['clean']
# args = ['clean', 123]     # invalid
# args = ['gcc']
match args:
    case ['gcc']:           # 只有 gcc的数组
        print('missing options')
    case ['gcc', file1,  *files]:   # 第一位 gcc, 第二位 作为变量 file1, 多位可选变量作为 files
        print('gcc pompile: ' + file1 + ','  + ','.join(files))
    case ['clean']:
        print("clean")
    case _:
        print('invalid command.')