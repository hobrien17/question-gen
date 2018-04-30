import random
import operator
import string
import math
import os
import re

CHOICES = ["x = {}\nx.append({})",  # 0 str/int/dict.append(str/int/dict/list) -> AttributeError
           "x = {}\nx.sort()",  # 1 str/int/dict.sort() -> AttributeError
           "x = {}\nx.append({}, {})",  # 2 list.append(str/int/lst) -> TypeError
           "x = {}\nx.extend({})",  # 3 list.extend(int) -> TypeError
           "y = {}({})",  # 4 len/sum/max/min(int) -> TypeError
           "x = {}\ny = {} in x",  # 5 int/bool in int/bool -> TypeError
           "x = {}\ny = x[{}]",  # 6 lst/str[3+] -> IndexError
           "x = {}\nx.pop({})",  # 7 lst.pop(3+) -> IndexError
           "x = {}\ny = x[{}]",  # 8 dict[3+] -> KeyError
           "x = {}\nx.pop({})",  # 9 dict.pop(3+) -> KeyError
           "x = {}\nx.extend({})",  # 10 list.extend(list/str/dict) -> No error
           "x = {}\ny = {} in x",  # 11 str/int/dict/list in str/lst/dict -> No error
           "x = {}\nx.pop({})",  # 12 list/dict.pop(-3 to 2) -> No error
           ]

EXCEPTIONS = [TypeError, AttributeError, IndexError, KeyError]
OPPOSITES = {TypeError: AttributeError, AttributeError: TypeError, IndexError: KeyError, KeyError: IndexError}
OTHERS = {TypeError: IndexError, IndexError: TypeError, AttributeError: KeyError, KeyError: AttributeError}

NONE = "None of the above"


def rand_lst(length):
    return [random.randint(0, 10) for i in range(length)]


def rand_dict(length):
    return {i: random.randint(0, 10) for i in range(length)}


def rand_str(length):
    res = "'"
    for i in range(length):
        res += random.choice(string.ascii_letters)
    return res + "'"


def rand_int(length):
    return random.randint(0, 10)


def rand_choice():
    i = random.randint(0, 12)
    if i == 0:
        opt1 = random.choice([rand_dict, rand_str, rand_int])(3)
        opt2 = random.choice([rand_lst, rand_dict, rand_str, rand_int])(3)
        return CHOICES[i].format(opt1, opt2), AttributeError
    elif i == 1:
        opt1 = random.choice([rand_dict, rand_str, rand_int])(3)
        return CHOICES[i].format(opt1), AttributeError
    elif i == 2:
        opt1 = rand_lst(3)
        opt2 = random.choice([rand_lst, rand_dict, rand_str, rand_int])(3)
        opt3 = random.choice([rand_lst, rand_dict, rand_str, rand_int])(3)
        return CHOICES[i].format(opt1, opt2, opt3), TypeError
    elif i == 3:
        opt1 = rand_lst(3)
        opt2 = rand_int(3)
        return CHOICES[i].format(opt1, opt2), TypeError
    elif i == 4:
        opt1 = rand_int(3)
        return CHOICES[i].format(random.choice(["len", "sum", "max", "min"]), opt1), TypeError
    elif i == 5:
        opt1 = random.choice([random.randint(0, 10), bool(random.randint(0, 1))])
        opt2 = random.choice([random.randint(0, 10), bool(random.randint(0, 1))])
        return CHOICES[i].format(opt1, opt2), TypeError
    elif i == 6:
        opt1 = rand_lst(3)
        opt2 = random.randint(3, 10)
        return CHOICES[i].format(opt1, opt2), IndexError
    elif i == 7:
        opt1 = rand_lst(3)
        opt2 = random.randint(3, 10)
        return CHOICES[i].format(opt1, opt2), IndexError
    elif i == 8:
        opt1 = rand_dict(3)
        opt2 = random.randint(3, 10)
        return CHOICES[i].format(opt1, opt2), KeyError
    elif i == 9:
        opt1 = rand_dict(3)
        opt2 = random.randint(3, 10)
        return CHOICES[i].format(opt1, opt2), KeyError
    elif i == 10:
        opt1 = rand_lst(3)
        opt2 = random.choice([rand_lst, rand_str, rand_dict])(3)
        return CHOICES[i].format(opt1, opt2), None
    elif i == 11:
        opt1 = rand_lst(3)
        opt2 = random.choice([rand_str, rand_lst, rand_int, rand_dict])(3)
        return CHOICES[i].format(opt1, opt2), None
    elif i == 12:
        opt1 = random.choice([rand_lst, rand_dict])(3)
        opt2 = random.randint(-3, 2)
        return CHOICES[i].format(opt1, opt2), None


def gen_except_1():
    line, excep = rand_choice()
    line = line.replace('\n', '\n\t')
    if excep is None:
        ex = random.choice(EXCEPTIONS)
    else:
        ex = excep
    other = OPPOSITES[ex]
    exes = [ex.__name__, other.__name__]
    random.shuffle(exes)

    code = f"try:\n" \
           f"\t{line}\n" \
           f"except {exes[0]}:\n" \
           f"\tprint('a')\n" \
           f"except {exes[1]}:\n" \
           f"\tprint('b')\n" \
           f"print('c')\n"

    question = "Which option best describes the output of the following code?\n\n" + code
    choices = ["'a' will be thrown", "'b' will be thrown", "'c' will be thrown",
               f"{exes[0]} will be thrown", f"{exes[1]} will be thrown"]
    if excep is None:
        answer = "'c' will be printed"
    elif exes[0] == excep.__name__:
        answer = "'a' will be printed"
    else:
        answer = "'b' will be printed"

    return question, answer, choices


def gen_except_2():
    line, excep = rand_choice()
    line = line.replace('\n', '\n\t')
    if excep is None:
        ex = random.choice(EXCEPTIONS)
    else:
        ex = excep
    other = OTHERS[ex]
    opts = [ex.__name__, other.__name__]
    random.shuffle(opts)
    exes = [OPPOSITES[ex].__name__, OPPOSITES[other].__name__]
    random.shuffle(exes)

    code = f"try:\n" \
           f"\t{line}\n" \
           f"except {exes[0]}:\n" \
           f"\tprint('a')\n" \
           f"except {exes[1]}:\n" \
           f"\tprint('b')\n" \
           f"print('c')\n"

    question = "Which option best describes the output of the following code?\n\n" + code
    choices = ["'a' will be printed", "'b' will be printed", "'c' will be printed",
               f"{opts[0]} will be thrown", f"{opts[1]} will be thrown"]
    answer = ex.__name__ + " will be thrown"

    return question, answer, choices


def gen_except_3():
    line, excep = rand_choice()
    line = line.replace('\n', '\n\t')
    if excep is None:
        ex = random.choice(EXCEPTIONS)
    else:
        ex = excep
    choice = random.choice(EXCEPTIONS).__name__
    opposite = OPPOSITES[ex].__name__

    code = f"try:\n" \
           f"\t{line}\n" \
           f"except {choice}:\n" \
           f"\tprint('a')\n" \
           f"except Exception:\n" \
           f"\tprint('b')\n" \
           f"print('c')\n"

    question = "Which option best describes the output of the following code?\n\n" + code
    choices = ["'a' will be printed", "'b' will be printed", "'c' will be printed",
               ex.__name__ + " will be thrown", opposite + " will be thrown"]

    if excep is None:
        answer = "'c' will be printed"
    elif ex.__name__ == choice:
        answer = "'a' will be printed"
    else:
        answer = "'b' will be printed"

    return question, answer, choices


def gen_except_4():
    rand = str(random.randint(0, 9))
    file = ""
    ans = ""
    with open(os.path.join("excepts", "e1.py")) as f:
        line = f.readline().replace("    ", "\t")
        while line != "":
            if not line.strip().endswith("#"):
                file += line
            else:
                if line.strip().endswith(rand + "#"):
                    ans = line.split("#")[1]
                    line = line.split("#")[0] + "\n"
                    while line.strip() != "":
                        file += line
                        line = f.readline().replace("    ", "\t")
                else:
                    while line.strip() != "":
                        line = f.readline()
            line = f.readline().replace("    ", "\t")

    question = "Consider the following code:\n\n" + file + "\nWhich of the following best describes the output of " \
                                                           "running this block of code?\n"
    opts = ["E is thrown with message '1'", "E is thrown with message '2'", "E is thrown with message '3'",
            "F is thrown", "A TypeError is thrown"]

    return question, ans, opts


FUNCS = [gen_except_1, gen_except_2, gen_except_3, gen_except_4, gen_except_4]


def gen_except():
    return random.choice(FUNCS)()

