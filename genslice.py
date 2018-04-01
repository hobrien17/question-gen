import random
import operator
import string
import math

STRINGS = ["Dogs and cats", "Critical mass", "Monty Python", "A string", "Computer Science", "Hello world",
           "Chocolate cake", "Frozen desert", "Thunderstorm", "Roses are red", "Hot temper", "Engineering"]
MORE = "More than one of the above is correct"
NONE = "None of the above"
START_KEY = 100
END_KEY = -100

def repl(string, try_opts, ans):
    ropt = []
    for opt in try_opts:
        if isinstance(opt, str):
            ropt.append(opt)
        elif len(opt) == 1 and opt[0] not in (START_KEY, END_KEY) and string[opt[0]] == ans:
            r = random.randint(0, len(string) - 1)
            while string[r] == ans:
                r = random.randint(0, len(string) - 1)
            ropt.append((r,))
        elif ((len(opt) == 2 and string[opt[0]:opt[1]] == ans) or
                (len(opt) == 3 and string[opt[0]:opt[1]:opt[2]] == ans)) and \
                opt[0] not in (START_KEY, END_KEY) and opt[1] not in (START_KEY, END_KEY):
            r1 = random.randint(0, len(string) - 1)
            r2 = random.randint(0, len(string) - 1)
            while string[min(r1, r2):max(r1, r2)] == ans:
                r1 = random.randint(0, len(string) - 1)
                r2 = random.randint(0, len(string) - 1)
            ropt.append((r1, r2))
        else:
            ropt.append(opt)
    return ropt


# S[I] -> Single
# S[I:I] -> Single
# S[I:I] & S[-I] -> Single


def gen_slice_1():
    string = random.choice(STRINGS)
    index = 0
    letter = " "
    while letter == " ":
        index = random.randint(1, len(string) - 2)
        letter = string[index]

    try_opts = [(index + 1,), (index + 1 - len(string),), (index - 1, index), MORE]
    opts = repl(string, try_opts, letter)
    opts.append((index,))

    return string, letter, (index,), opts


def gen_slice_2():
    string = random.choice(STRINGS)
    start = 0
    stop = 0
    letter = " "
    while letter == " ":
        start = random.randint(1, len(string) - 2)
        stop = start + 1
        letter = string[start:stop]

    try_opts = [(start + 1,), (start + 1 - len(string),), (start + 2 - len(string),), MORE]
    opts = repl(string, try_opts, letter)
    opts.append((start, stop))

    return string, letter, (start, stop), opts


def gen_slice_3():
    string = random.choice(STRINGS)
    start = 0
    stop = 0
    index = 0
    letter = " "
    while letter == " ":
        start = random.randint(1, len(string) - 2)
        stop = start + 1
        index = start - len(string)
        letter = string[index]

    try_opts = [(start + 1,), (start + 1 - len(string),)]
    opts = repl(string, try_opts, letter)
    opts.append((start, stop))
    opts.append((index,))
    opts.append(MORE)

    return string, letter, MORE, opts


# S[I:I] -> Multiple
# S[-I:I] -> Multiple
# S[-I:-I] -> Multiple
# S[:I] -> Multiple
# S[I:] & S[I:I] -> Multiple


def gen_slice_4():
    string = random.choice(STRINGS)
    start = random.randint(1, len(string) - 4)
    stop = start + random.randint(3, min(len(string) - start, 4))
    res = string[start:stop]

    try_opts = [(start, stop - 1), (start + 1, stop - 1), (start + 1, stop), NONE]
    opts = repl(string, try_opts, res)
    opts.append((start, stop))

    return string, res, (start, stop), opts


def gen_slice_5():
    string = random.choice(STRINGS)
    start_old = random.randint(1, len(string) - 4)
    stop = start_old + random.randint(3, min(len(string) - start_old, 4))
    start = start_old - len(string)
    res = string[start:stop]

    try_opts = [(start_old, stop - 1), (start_old + 1, stop - 1), (start_old + 1 - len(string), stop), MORE]
    opts = repl(string, try_opts, res)
    opts.append((start, stop))

    return string, res, (start, stop), opts


def gen_slice_6():
    string = random.choice(STRINGS)
    start_old = random.randint(1, len(string) - 4)
    stop_old = start_old + random.randint(3, min(len(string) - start_old, 4))
    start = start_old - len(string)
    stop = stop_old - len(string)
    res = string[start:stop]

    try_opts = [(start_old - len(string), stop_old - len(string) - 1),
                (start_old - len(string) + 1, stop_old - len(string) - 1),
                (start_old - len(string) + 1, stop_old - len(string)),
                NONE]
    opts = repl(string, try_opts, res)
    opts.append((start, stop))

    return string, res, (start, stop), opts


def gen_slice_7():
    string = random.choice(STRINGS)
    start = START_KEY
    stop = random.randint(4, len(string) - 1)
    res = string[:stop]

    try_opts = [(1, stop), (start, stop - 1), (stop, END_KEY), MORE]
    opts = repl(string, try_opts, res)
    opts.append((start, stop))

    return string, res, (start, stop), opts


def gen_slice_8():
    string = random.choice(STRINGS)
    start = random.randint(1, len(string) - 4)
    res = string[start:]

    opts = [(start + 1, END_KEY), (START_KEY, len(string)), (start, len(string)), (start, END_KEY), MORE]
    return string, res, MORE, opts


# S[I:I:-I] -> Multiple (I = -1)
# S[I:I:-I] -> Multiple (I < -1)
# S[I:I:I] -> Multiple

def gen_slice_9():
    string = random.choice(STRINGS)
    stop = random.randint(1, len(string) - 4)
    start = stop + random.randint(3, min(len(string) - stop, 4))
    step = -1
    res = string[start:stop:step]

    try_opts = [(stop, start, 2), (start, stop, -2), (stop, start, -1), MORE]
    opts = repl(string, try_opts, res)
    opts.append((start, stop, step))

    return string, res, (start, stop, step), opts


def gen_slice_10():
    string = random.choice(STRINGS)
    stop = random.randint(1, 3)
    start = random.randint(max(stop, len(string) - 3), len(string) - 1)
    step = random.randint(-3, -2)
    res = string[start:stop:step]

    try_opts = [(stop, start, 2), (start, stop, -1), (stop, start, -1), MORE]
    opts = repl(string, try_opts, res)
    opts.append((start, stop, step))

    return string, res, (start, stop, step), opts


def gen_slice_11():
    string = random.choice(STRINGS)
    start_lst = [0, 1]
    end_lst = [len(string) - 1, len(string)]

    start = random.choice(start_lst)
    stop = random.choice(end_lst)
    start_lst.remove(start)
    nonstart = start_lst[0]
    end_lst.remove(stop)
    step = random.randint(2, 3)
    res = string[start:stop:step]

    try_opts = [(nonstart, stop, step + 1), (nonstart, stop, step), (start, stop, step + 1), NONE]
    opts = repl(string, try_opts, res)
    opts.append((start, stop, step))

    return string, res, (start, stop, step), opts


FUNCS = [gen_slice_1, gen_slice_2, gen_slice_3, gen_slice_4, gen_slice_5, gen_slice_6, gen_slice_7,
         gen_slice_8, gen_slice_9, gen_slice_10, gen_slice_11]


def to_string(opt):
    if isinstance(opt, str):
        return opt
    elif len(opt) == 1:
        return f"y = x[{opt[0]}]"
    elif len(opt) == 2:
        if opt[0] == START_KEY:
            return f"y = x[:{opt[1]}]"
        elif opt[1] == END_KEY:
            return f"y = x[{opt[0]}:]"
        else:
            return f"y = x[{opt[0]}:{opt[1]}]"
    elif len(opt) == 3:
        return f"y = x[{opt[0]}:{opt[1]}:{opt[2]}]"


def gen_slice():
    func = random.choice(FUNCS)
    string, res, index, opts = func()
    question = f"After the assignment x = '{string}', which of the following assigns '{res}' to the variable y?"
    opt_strs = []
    for opt in opts:
        opt_strs.append(to_string(opt))
    answer = to_string(index)

    return question, answer, opt_strs