class A:
    def __init__(self):

        print("A")

class B:
    def __init__(self):
        print("B")

class C(A,B):
    def __init__(self):

        print("C")
        super(A,self).__init__()
        super(B,self).__init__()


cl1 = C()