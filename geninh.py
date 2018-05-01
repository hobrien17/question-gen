import random
import operator
import string
import math
import inspect

NONE = "None of the above"


def get_source(fn, cls):
    text = inspect.getsource(fn)
    if hasattr(cls, "r"):
        text = text.replace("self.r", str(cls.r))
    if hasattr(cls, "s"):
        text = text.replace("self.s", str(cls.s))
    text = text.replace("f1", "f")
    text = text.replace("f2", "f")
    text = text.replace("f3", "f")
    text = text.replace("g1", "g")
    text = text.replace("g2", "g")
    text = text.replace("g3", "g")
    return text


class A(object):

    def __init__(self, x):
        self.x = x

    def f1(self, x):
        return self.r * x

    def f2(self, x):
        return self.r + x

    def f3(self, x):
        return self.r - x

    def g1(self, x):
        return self.f(x)

    def g2(self, x):
        return self.f(self.x)

    def g3(self, x):
        return self.f(self.x - x)

    def __str__(self):
        res = "class A(object):\n" + inspect.getsource(self.__init__) + "\n" + get_source(self.f, self) + "\n" + \
                                                                      get_source(self.g, self) + "\n"
        return res.replace("    ", "\t")


class B(A):

    def f1(self, x):
        return self.x + self.s * x

    def f2(self, x):
        return self.x - x

    def f3(self, x):
        return self.x * self.s - self.s

    def g1(self, x):
        return self.x - (self.s + x)

    def g2(self, x):
        return self.f(self.x + x)

    def g3(self, x):
        return self.f(x + self.s)

    def __str__(self):
        res = "class B(A):\n"
        if self.isf:
            res += get_source(self.f, self) + "\n"
        else:
            res += get_source(self.g, self) + "\n"
        return res.replace("    ", "\t")


class C(B):

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def f1(self, x):
        return super().f(x) + self.y

    def f2(self, x):
        return super().f(self.x) - self.y

    def f3(self, x):
        return super().f(self.x) + self.y + x

    def g1(self, x):
        return self.y - super().g(x)

    def g2(self, x):
        return self.y + super().g(self.x)

    def g3(self, x):
        return self.y * x + self.x

    def __str__(self):
        res = "class C(B):\n" + inspect.getsource(self.__init__) + "\n"
        if self.isf:
            res += get_source(self.f, self) + "\n"
        else:
            res += get_source(self.g, self) + "\n"
        return res.replace("    ", "\t")


def gen_inh_2():
    c_inp_x = random.randint(-5, 5)
    c_inp_y = random.randint(-5, 5)
    c = C(c_inp_x, c_inp_y)
    r1 = random.randint(2, 4)
    r2 = random.randint(2, 4)
    setattr(A, "r", r1)
    setattr(B, "s", r2)
    setattr(A, "f", random.choice([A.f1, A.f2, A.f3]))
    setattr(A, "g", random.choice([A.g1, A.g2, A.g3]))

    isfb = bool(random.randint(0, 1))
    isfc = bool(random.randint(0, 1))
    if isfb:
        setattr(B, "isf", isfb)
        setattr(B, "f", random.choice([B.f1, B.f2, B.f3]))
    else:
        setattr(B, "isf", isfb)
        setattr(B, "g", random.choice([B.g1, B.g2, B.g3]))
    if isfc:
        setattr(C, "isf", isfc)
        setattr(C, "f", random.choice([C.f1, C.f2, C.f3]))
    else:
        setattr(C, "isf", isfc)
        setattr(C, "g", random.choice([C.g1, C.g2, C.g3]))

    question = "Consider the following classes:\n\n" + str(A(c_inp_x)) + "\n" + str(B(c_inp_x)) + "\n" + str(c) + "\n"

    x = random.randint(1, 5)
    choice = bool(random.randint(0, 1))
    if choice:
        question += f"After the initialization c = C({c_inp_x}, {c_inp_y}), what will the method call c.f({x}) return?"
        ans = c.f(x)
    else:
        question += f"After the initialization c = C({c_inp_x}, {c_inp_y}), what will the method call c.g({x}) return?"
        ans = c.g(x)

    i = random.randint(-3, 0)
    opts = []
    for j in range(4):
        opts.append(str(ans + i))
        i += 1
    opts.append(NONE)

    return question, str(ans), opts


def gen_inh_1():
    b_inp = random.randint(-5, 5)
    b = B(b_inp)
    r1 = random.randint(2, 4)
    r2 = random.randint(2, 4)
    setattr(A, "r", r1)
    setattr(B, "r", r2)
    setattr(A, "f", random.choice([A.f1, A.f2, A.f3]))
    setattr(A, "g", random.choice([A.g1, A.g2, A.g3]))
    isf = bool(random.randint(0, 1))
    if isf:
        setattr(B, "isf", isf)
        setattr(B, "f", random.choice([B.f1, B.f2, B.f3]))
    else:
        setattr(B, "isf", isf)
        setattr(B, "g", random.choice([B.g1, B.g2, B.g3]))

    question = "Consider the following classes:\n\n" + str(A(b_inp)) + "\n" + str(b) + "\n"

    x = random.randint(1, 5)
    choice = bool(random.randint(0, 1))
    if choice:
        question += f"After the initialization b = B({b_inp}), what will the method call b.f({x}) return?"
        ans = b.f(x)
    else:
        question += f"After the initialization b = B({b_inp}), what will the method call b.g({x}) return?"
        ans = b.g(x)

    i = random.randint(-3, 0)
    opts = []
    for j in range(4):
        opts.append(str(ans + i))
        i += 1
    opts.append(NONE)

    return question, str(ans), opts


def gen_inh():
    if hasattr(A, "f"):
        del A.f
    if hasattr(A, "g"):
        del A.g
    if hasattr(B, "f"):
        del B.f
    if hasattr(B, "g"):
        del B.g
    if hasattr(C, "f"):
        del C.f
    if hasattr(C, "g"):
        del C.g
    return random.choice([gen_inh_1, gen_inh_2])()


for i in gen_inh_2():
    print(i)