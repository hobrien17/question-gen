class E(Exception):
    
    def __init__(self, msg):
        super().__init__(msg)
        self._var = 0

    def a(self, v):
        self._var += v

    def b(self):
        if self._var < 1:
            raise E("2")
        return self

    def c(self):
        if self._var > 1:
            raise self
        return E("3")

class F(Exception):
    
    def x(self): #E is thrown with message '1'#1#
        e = E("1")
        e.a(2)
        return e.b()

    def x(self): #E is thrown with message '2'#2#
        e = E("1")
        e.a(-2)
        return e.b()

    def x(self): #E is thrown with message '1'#3#
        e = E("1")
        e.a(2)
        return e.c()

    def x(self): #E is thrown with message '3'#4#
        e = E("1")
        e.a(-2)
        return e.c()

    def x(self): #F is thrown#5#
        e = E("1")
        e.a(2)
        try:
            return e.c()
        except E:
            return self

    def x(self): #E is thrown with message '3'#6#
        e = E("1")
        e.a(-2)
        try:
            return e.c()
        except E:
            return self

    def x(self): #E is thrown with message '1'#7#
        e = E("1")
        e.a(2)
        try:
            return e.b()
        except E:
            print(F()) 

    def x(self): #A TypeError is thrown#8#
        e = E("1")
        e.a(-2)
        try:
            return e.b()
        except E:
            print(F())

    def x(self): #A TypeError is thrown#9#
        e = E()
        e.a(2)
        return e.b()

    def x(self): #F is thrown#0#
        raise self
        raise E("1")
        raise E("2")
        return E("3")


raise F().x()
