import random
import operator
import string
import math
import re

NONE = "None of the above"


def count_tabs(line):
    count = 0
    for i in range(len(line)):
        if line[i] != '\t':
            return count
        else:
            count += 1


def gen_io_1():
    funcs = []
    with open("fileio/file1.py", "r") as f:
        fun = ""
        for line in f:
            if line.startswith("#"):
                funcs.append((fun, line.strip().split(":")[1]))
                fun = ""
            elif line != "\n":
                fun += line.replace("    ", "\t")

    choice = random.choice(funcs)

    opts = [
        "The function will always terminate without errors or resource leaks",
        "The function may not always terminate",
        "The function may throw an error",
        "The function will always terminate without errors but may cause resource leaks",
        "None of the above"
    ]
    if choice[1] == "Good":
        ans = opts[0]
    elif choice[1] == "Loop":
        ans = opts[1]
    elif choice[1] == "Error":
        ans = opts[2]
    elif choice[1] == "Leak":
        ans = opts[3]
    else:
        ans = opts[4]

    question = f"Consider the following function:\n\n{choice[0]}\n" \
               f"Assuming the file can be successfully opened, which of the following is true?\n"

    return question, ans, opts


def gen_io_2():
    funcs = []
    with open("fileio/file2.py", "r") as f:
        fun = ""
        for line in f:
            if line.startswith("#"):
                funcs.append((fun, line[1:].strip()))
                fun = ""
            elif line != "\n":
                fun += line.replace("    ", "\t")

    choice = random.choice(funcs)

    lsts = [[random.randint(1, 8) for i in range(random.randint(2, 5))] for i in range(3)]
    file = ""
    for i in lsts:
        for j in i:
            file += str(j) + ","
        file = file[:-1]
        file += "\n"

    if choice[1] == "sum":
        ans = ",".join([str(sum(i)) for i in lsts])
    elif choice[1] == "len":
        ans = ",".join([str(len(i)) for i in lsts])
    elif choice[1] == "max":
        ans = ",".join([str(max(i)) for i in lsts])
    elif choice[1] == "min":
        ans = ",".join([str(min(i)) for i in lsts])
    else:
        ans = ""

    question = f"Consider the following function:\n\n{choice[0]}\n" \
               f"Assume the file input.csv contains the following data:\n\n{file}\n" \
               f"After the function call fn('input.csv', 'output.csv'), what will be stored in the file output.csv?"
    opts = []
    while len(set(opts)) < 5:
        spl = ans.split(",")
        rand = [str(random.randint(1, 10)) for i in range(3)]
        opts = [ans,
                ",".join([spl[0], spl[1], str(random.randint(1, 10))]),
                ",".join(rand),
                ",".join([rand[0], str(random.randint(1, 10)), str(random.randint(1, 10))]),
                "Error"]

    return question, ans, opts


def gen_io_3():
    funcs = []
    with open("fileio/file3.py", "r") as f:
        fun = ""
        for line in f:
            if line.startswith("#"):
                funcs.append((fun, int(line[1:].strip())))
                fun = ""
            else:
                fun += line.replace("    ", "\t")

    choice = random.choice(funcs)
    line_no = random.randint(1, choice[1])
    i = 0
    ans = None
    opts = None
    final = ""
    for line in choice[0].split('\n'):
        if "#" in line:
            i += 1
        if i == line_no:
            final += count_tabs(line)*"\t" + "#####" + "\n"
            ans = line.partition("#")[0].strip()
            opts = line.partition("#")[2].split("/")
            opts.append(NONE)
            opts.append(ans)
            i += 1
        else:
            final += line.partition("#")[0] + "\n"

    question = f"Consider the following function:\n\n{final}\n" \
               f"Which of the following lines of code should replace ##### " \
               f"so that the function's docstring is satisfied?"

    return question, ans, opts


FUNCS = [gen_io_1, gen_io_2, gen_io_3]


def gen_io():
    return random.choice(FUNCS)()
