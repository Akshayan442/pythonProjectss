class test:
    def __init__(self):
        self.m1 = 50
        self.m2 = 40
class grade(test):
    def __init__(self):
        self.total = self.m1 + self.m2
        print(self.total)