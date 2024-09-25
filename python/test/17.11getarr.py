from typing import Any


class Student():
    def __init__(self) -> None:
        self.name = "weibin"
    def __getattribute__(self, name: str) -> Any:
        if(name == 'score'):
            return 88       # 这里可以调用函数，以及类本身 用法丰富
    
s1 = Student()
print(s1.score)