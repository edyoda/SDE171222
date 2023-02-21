import json

class ABC:

    def __init__(self):
        self.x = 0

    def fn1(self):
        self.x += 10
        return self.x
    
    def fn2(self):
        self.x *= 10

    def printx(self):
        return self.x
    
if __name__ == "__main__":
    abc = ABC()
    x1 = abc.fn1()
    x2 = abc.fn2()
    x3 = abc.printx()
    print(x3)
