import random
import operator
import string
import math
import re

STRINGS = ["Here is a string", "Python is fun", "Some random words", "Strings and lists", "Yes no maybe",
           "One two three", "Dogs and cats", "Under the sea", "Sun and the moon", "Sky and the ocean",
           "Night and day", "Count to five", "Stringy stringed strings", "Roses are red", "Batman and Robin",
           "a b c d e"]
SHORT_STRINGS = ["cat", "dog", "pig", "bat", "owl", "cow", "abc", "xyz"]
DELIMS = [",", ":", ";", ".", "_"]

NONE = "None of the above"

# S = string
# L = list
# I = int
# x/y/z = literal
# r = result

# S => S -> capitalise, upper, lower, swapcase, title, strip
# S(L) => S -> join
# S(S) => L -> split
# S(S, S) => S -> replace
# S(S) => I -> count, find, rfind, index, rindex
# L(S) => N -> extend

# r = xS.strip().S => S
# r = xS.replace(yS, zS).S => S
# r = xS.join(yL).S(S) => I
# r = xS.split(yS) => L, r.extend(zS)
# r = xS.partition(yS).partition(zS) => T
# r = xS.join(yS.split()) => S

S_TO_S = [str.title, str.upper, str.lower, str.swapcase]
OPPOSITES = {str.title: str.upper, str.upper: str.title, str.lower: str.swapcase, str.swapcase: str.lower}
S_TO_I = [str.count, str.find, str.rfind, str.index, str.rindex]
EXPS = {
    str.count: "Recall that s.count(sub) counts how many times the substring sub appears in s.\n",
    str.find: "Recall that s.find(src) searches for the substring src in s.\n"
              "If src is found, its index will be returned, otherwise -1 is returned.\n",
    str.rfind: "Recall that s.rfind(src) searches for the substring src in s, working backwards from the end of s.\n"
               "If src is found, its index will be returned, otherwise -1 is returned.\n",
    str.index: "Recall that s.index(src) searches for the substring src in s.\n"
               "If src is found, its index will be returned, otherwise a ValueError is raised.\n",
    str.rindex: "Recall that s.rindex(src) searches for the substring src in s, working backwards from the end of s.\n"
                "If src is found, its index will be returned, otherwise a ValueError is raised.\n"
}


SINGLE_WHITESPACE = ['\t', '\n', '\f', '\r']
MULTI_WHITESPACE = ['\t\t', '\n\n', '\r\n', '\n\n\n']


def repl_whitespace(s):
    return s.replace('\t', '\\t').replace('\r', '\\r').replace('\n', '\\n').replace('\f', '\\f')


def insert_whitespace(s):
    result = ""
    count = 0
    while count > 5 or count <= 1:
        result = ""
        for char in s:
            result += char
            i = random.randint(0, 15)
            if i == 0:
                result += random.choice(MULTI_WHITESPACE + SINGLE_WHITESPACE + ['\n', '\n', '\n'])
        count = result.count('\n') + result.count('\t') + result.count('\r')
    return result


def gen_str_6():
    opts = []
    ans = None

    while len(set(opts)) < 5:
        #s = insert_whitespace(random.choice(STRINGS)) + random.choice(MULTI_WHITESPACE)
        s = "Stringy stringed str\n\n\nings\r\n"
        delim = " "
        #delim = random.choice(DELIMS)

        ans = str(delim.join(s.split()))

        opts = [ans,
                repl_whitespace(str(delim.join(s.split(" ")))),
                repl_whitespace(str(delim.join(re.split(r'\s', s)))),
                repl_whitespace(str(delim.join(s.split() + ['']))),
                NONE]

    exp = f"'{delim}'.join(x.split())"
    question = f"After the assignment x = '{repl_whitespace(s)}', what does the expression {exp} evaluate to?\n"

    return question, ans, opts


def gen_str_5():
    opener = random.choice(["(", "[", "{"])
    closer = {"(": ")", "[": "]", "{": "}"}[opener]
    s = random.choice(STRINGS)
    index1 = random.randint(1, len(s)//2)
    index2 = random.randint(index1 + 1, len(s))
    full_str = s[:index1] + opener + s[index1:index2] + closer + s[index2:]
    full_str = full_str.replace(" ", opener, 1).replace(" ", closer)

    x, y, z = full_str.partition(opener)
    ans = str(z.partition(closer))

    x1, y1, z1 = full_str.rpartition(opener)
    ans1 = str(z1.rpartition(closer))

    x2, y2, z2 = full_str.rpartition(opener)
    ans2 = str(z2.partition(closer))

    ans3 = str(tuple(full_str.split(opener)))

    opts = [ans, ans1, ans2, ans3, NONE]

    exp = f"s = '{full_str}'\nx, y, z = s.partition('{opener}')\nw = z.partition('{closer}')\n"
    question = "What is the value of w after the following is evaluated?\n\n" + exp

    return question, ans, opts


def alt_split(s, d):
    res = []
    for i in s.split(d):
        res.append(i)
        res.append(d)
    res.pop(-1)
    return res


def gen_str_4():
    delim = random.choice(DELIMS)
    s = random.choice(STRINGS).replace(" ", delim) + delim
    lst = s.split(delim)
    short = random.choice(SHORT_STRINGS)
    res = lst[:]
    res.extend(short)
    ans = str(res)

    opts = [ans, NONE]
    alt_res = lst[:]
    alt_res.append(short)
    opts.append(str(alt_res))
    alt_lst = alt_split(s, delim)
    alt_res = alt_lst[:]
    alt_res.append(short)
    opts.append(str(alt_res))
    alt_res = alt_lst[:]
    alt_res.pop(-1)
    alt_res.append(short)
    opts.append(str(alt_res))

    code = f"x = '{s}'\ny = '{short}'\nz = x.split('{delim}')\nz.extend(y)\n"
    question = "What is the value of z after the following is evaluated?\n\n" + code
    return question, ans, opts


def gen_str_3():
    lst = random.choice(STRINGS).split(" ")
    delim = random.choice(DELIMS)
    func = random.choice(S_TO_I)
    joined = delim.join(lst)

    ans = str(func(joined, delim))
    opts = []
    while len(set(opts)) < 5:
        if func == str.find or func == str.rfind:
            opts = [ans, "-1"]
        else:
            opts = [ans, "ValueError"]
        for i in range(3):
            opts.append(str(random.randint(0, len(joined))))

    exp = f"'{delim}'.join(x).{func.__name__}('{delim}')"
    question = f"After the assignment x = {lst}, what does the expression {exp} evaluate to?\n" + EXPS[func]
    return question, ans, opts


def upper_rand():
    return "".join(random.choice([k.upper(), k]) for k in random.choice(STRINGS))


def gen_str_2():
    s = upper_rand()
    s = s[:-1] + s[-1].lower()
    choice = random.choice(s)
    new = choice
    while new == choice:
        new = random.choice(s)
    func = random.choice(S_TO_S)
    res = func(s.replace(choice, new))

    ans = f"'{res}'"
    opts = [
        ans,
        f"'{func(s.replace(new, choice))}'",
        f"'{OPPOSITES[func](s.replace(new, choice))}'",
        f"'{OPPOSITES[func](s.replace(choice, new))}'",
        "None of the above"
    ]

    exp = f"z = x.replace('{choice}', '{new}').{func.__name__}()"
    question = f"After the assignment x = '{s}', what does the expression {exp} evaluate to?\n"
    return question, ans, opts


def gen_str_1():
    s = upper_rand().replace(' ', ' \n ')
    s = s[:-1] + s[-1].lower()
    s = random.choice(SINGLE_WHITESPACE) + s + random.choice(MULTI_WHITESPACE)
    func = random.choice(S_TO_S)
    res = func(s.strip())

    ans = repl_whitespace(f"'{res}'")
    s2 = res.replace(' \n ', '')
    opts = [
        ans,
        repl_whitespace(f"'{s2}'"),
        repl_whitespace(f"'{func(s.lstrip()[:-1])}'"),
        repl_whitespace(f"'{func(s.rstrip())}'"),
        "None of the above"
            ]

    exp = f"z = x.strip().{func.__name__}()"
    question = f"After the assignment x = '{repl_whitespace(s)}', what does the expression {exp} evaluate to?\n"
    return question, ans, opts


FUNCS = [gen_str_1, gen_str_2, gen_str_3, gen_str_4, gen_str_5, gen_str_6]


def gen_str():
    return random.choice(FUNCS)()