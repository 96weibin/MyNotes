class Student():
    _scores = 0
    def __init__(self, name) -> None:
        self.name = name
    @property
    def scores(self):
        return self._scores

    @scores.setter
    def scores(self, value):
        if value > 100 or value < 0:
            raise ValueError('error score')
        else:
            self._scores = value

xiaoming = Student('xiaoming1')
print(xiaoming.scores)
xiaoming.scores = 99
print(xiaoming.scores)
xiaoming.scores = 101
