class Regtrangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def paragic(self):
        return 2 * (self.a + self.b)
    def makeres(self):
        return  self.a * self.b


Reg_1 = Regtrangle(15, 15)
print(Reg_1.paragic(), Reg_1.makeres())

