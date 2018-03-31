import random
import operator
import string
import math
from flask import Flask, request

PM = ["+", "-"]
DM = ["//", "%"]
OP = {"+": operator.add, "-": operator.sub, "//": operator.floordiv, "%": operator.mod,
      "*": operator.mul, "**": operator.pow}

STRS = ["cat", "dog", "mouse", "fish", "bird", "fred", "bob", "bill", "joe", "jim", "abc", "xyz"]

def rand(start, end):
    r = 0
    while -1 <= r <= 1:
        r = random.randint(start, end)
    return r


# E -> ((-)I +or- I) ** 2
# E -> ((-)I * (-)I) //or% I
# E -> (-)F +or- (-)I * (-)I
# E -> F //or% (I +or- I)
# E -> I //or% I +or- C

def gen_exp_1():
    op = random.choice(PM)
    int1 = 100
    int2 = 0
    while not (-10 <= OP[op](int1, int2) <= 10):
        int1 = rand(-10, 10)
        int2 = rand(2, 10)
    result = f"({int1} {op} {int2}) ** 2"
    answer = (OP[op](int1, int2))**2

    opts = []
    times = (OP[op](int1, int2))*2
    if times != answer:
        opts.append(times)
    elif answer != 0:
        opts.append(-answer)
    else:
        opts.append(answer + rand(-10, 10))
    opts.append(answer + rand(-20, 20))
    opts.append(answer + rand(-answer + 1, answer - 1))
    opts.append("TypeError")

    return result, answer, opts


def gen_exp_2():
    op = random.choice(DM)
    int1 = 1
    int2 = 1
    int3 = 2
    while int1 * int2 <= 1 or abs(int1 * int2) < abs(int3):
        int1 = rand(-8, 8)
        int2 = rand(-8, 8)
        int3 = rand(3, 7)
    result = f"({int1} * {int2}) {op} {int3}"
    answer = OP[op]((int1 * int2), int3)

    opts = []
    div = (int1 * int2) / int3
    if len(str(div).rsplit('.')[-1]) <= 2:
        opts.append(div)
    else:
        opts.append(-answer)
    if float(answer) != div:
        opts.append(float(answer))
    else:
        opts.append(answer + rand(-10, 10))
    opts.append(math.floor(div + 1))
    opts.append("TypeError")

    return result, answer, opts


def gen_exp_3():
    ft = float(rand(-20, 20)/2)
    op = random.choice(PM)
    int1 = rand(-5, 5)
    int2 = rand(-5, 5)
    result = f"{ft} {op} {int1} * {int2}"
    answer = OP[op](ft, (int1 * int2))

    alt = OP[op](ft, int1) * int2
    opts = [int(answer), alt, int(alt), "TypeError"]
    return result, answer, opts


def gen_exp_4():
    op1 = random.choice(DM)
    op2 = random.choice(PM)
    int1 = 2
    int2 = 1
    ft = 0
    while OP[op2](int1, int2) <= 0 or abs(ft) < abs(OP[op2](int1, int2)):
        op2 = random.choice(PM)
        int1 = rand(2, 10)
        int2 = rand(2, 10)
        ft = float(rand(-20, 20))
    result = f"{ft} {op1} ({int1} {op2} {int2})"
    answer = OP[op1](ft, OP[op2](int1, int2))

    opts = []
    div = ft / OP[op2](int1, int2)
    if len(str(div).rsplit('.')[-1]) <= 2 and div != result:
        opts.append(div)
        opts.append(int(div))
    else:
        opts.append(-answer)
        opts.append(int(-answer))
    opts.append(int(answer))
    opts.append("TypeError")

    return result, answer, opts


def gen_exp_5():
    op1 = random.choice(DM)
    op2 = random.choice(PM)
    int1 = rand(2, 10)
    int2 = rand(2, 10)
    int3 = rand(2, 10)
    result = f"{int1} {op1} {int2} {op2} '{int3}'"
    answer = "TypeError"

    alt1 = OP[op1](int1, OP[op2](int2, int3))
    alt2 = OP[op2](OP[op1](int1, int2), int3)
    if alt1 == alt2:
        opts = [alt1, random.randint(1, 20), random.randint(-10, 10)]
    else:
        opts = [alt1, alt2, random.randint(1, 10), random.randint(-10, 10)]

    return result, answer, opts


# E -> list(str(I)) + [C, C]
# E -> [I, I] + I
# E -> [I, I] + [[I]]
# E -> (I, I) + ((I))
# E -> S + S*I
# E -> S - C


def gen_exp_6():
    int1 = random.randint(2, 5)
    char1 = random.choice(string.ascii_uppercase)
    char2 = random.choice(string.ascii_lowercase)
    result = f"list(str({int1})) + ['{char1}', '{char2}']"
    answer = str(list(str(int1)) + [char1, char2])

    opts = [
        str([char1, char2, str(int1)]),
        str([int1, char1, char2]),
        str([char1, char2, int1]),
        "TypeError"
    ]
    return result, answer, opts


def gen_exp_7():
    int1 = random.randint(1, 5)
    int2 = random.randint(6, 10)
    int3 = random.randint(11, 15)
    result = f"[{int1}, {int2}] + {int3}"
    answer = "TypeError"

    opts = [
        str([int1, int2, int3]),
        str([int1 + int3, int2 + int3]),
        str([int1 + int3, int2]),
        str([int1, int2 + int3])
    ]
    return result, answer, opts


def gen_exp_8():
    int1 = random.randint(1, 5)
    int2 = random.randint(6, 10)
    int3 = random.randint(11, 15)
    result = f"[{int1}, {int2}] + [[{int3}]]"
    answer = str([int1, int2] + [[int3]])

    opts = [
        str([int1, int2, int3]),
        str([[int1, int2, int3]]),
        str([int1 + int3, int2 + int3]),
        "TypeError"
    ]
    return result, answer, opts


def gen_exp_9():
    int1 = random.randint(1, 5)
    int2 = random.randint(6, 10)
    int3 = random.randint(11, 15)
    result = f"({int1}, {int2}) + (({int3}))"
    answer = "TypeError"

    opts = [
        str((int1, int2, int3)),
        f"({int1}, {int2}, ({int3},)",
        f"({int1}, {int2}, ({int3}))",
        str((int1 + int3, int2 + int3)),
    ]
    return result, answer, opts


def gen_exp_10():
    str1 = random.choice(STRS)
    str2 = random.choice(STRS)
    mult = random.randint(2, 3)
    result = f"'{str1}' + '{str2}'*{mult}"
    answer = str1 + str2*mult

    new = ""
    for i in str2:
        new += i*mult
    opts = [
        f"'{str1 + str2}'",
        f"'{str1 + new}'",
        f"['{str1}', '{str2}']",
        "TypeError"
    ]
    return result, answer, opts


def gen_exp_11():
    str1 = random.choice(STRS)
    char = random.choice(str1)
    result = f"'{str1}' - '{char}'"
    answer = "TypeError"

    repl = str1.replace(char, "")
    opts = [
        f"'{repl}'",
        f"'{str1 + char}'",
        "''",
        f"'{str1} - {char}'"
    ]
    return result, answer, opts


EXPS = [gen_exp_1, gen_exp_2, gen_exp_3, gen_exp_4, gen_exp_4, gen_exp_5,
                gen_exp_6, gen_exp_7, gen_exp_8, gen_exp_9, gen_exp_10, gen_exp_11]


def gen_exp():
    chosen_exp = random.choice(EXPS)
    while True:
        try:
            exp, answer, opts = chosen_exp()
            opts.append(answer)
            opts = [str(i) for i in opts]
            if len(set(opts)) == 5:
                break
        except ZeroDivisionError:
            continue
    opts = sorted(opts)
    for i in opts:
        if "ERROR" in i.upper():
            opts.remove(i)
            opts.append(i)
            break
    return exp

####################################################################################################

app = Flask(__name__)

@app.route('/')
def execute():
    return "yes"

@app.route('/stuff')
def execute_2():
    return "no"

if __name__ == "__main__":
    app.run()