import random
import operator
import string
import math

#FUNCTION
# def g(xs):
#   z = g.pop(I) or list[I:I]
#   z.append(S) or z.extend(S) or list add


def rand_list(size):
    i = random.randint(0, len(string.ascii_letters) - size)
    xs = []
    for j in range(size):
        xs.append(string.ascii_letters[i + j])
    return xs


def rand_int_list(size):
    i = random.randint(0, 5)
    xs = []
    for j in range(size):
        xs.append(i + j)
    return xs


def slice_wrapper(lst, index):
    lst.pop(-1)
    return lst[index]


def perform_op(lst, **kwargs):
    z = kwargs.get("op1")(lst, kwargs.get("param1"))
    if kwargs.get("op2") == list.insert:
        kwargs.get("op2")(lst, kwargs.get("param2"), z)
    else:
        kwargs.get("op2")(lst, z)
    return lst


def gen_list_1():
    xs = rand_list(3)
    func = "def g(xs):\n"

    i = random.randint(0, 1)
    if i == 0:
        op1 = list.pop
        param1 = random.randint(0, 1)
        func += f"    z = xs.pop({param1})\n"

        op2 = random.choice([list.extend, list.append])
        param2 = 0
        op2_strs = {list.extend: "xs.extend(z)", list.append: "xs.append(z)"}
        func += "    " + op2_strs[op2] + "\n"
    else:
        op1 = list.pop
        param1 = -1
        func += f"    z = xs.pop(-1)\n"

        op2 = list.insert
        param2 = random.randint(0, 1)
        func += f"    xs.insert({param2}, z)\n"

    func += "    return xs\n"

    opts = [xs[:]]

    ys = xs[:]
    perform_op(ys, op1=op1, op2=op2, param1=param1, param2=param2)
    opts.append(ys)

    ys = xs[:]
    perform_op(ys, op1=op1, op2=op2, param1=param1, param2=param2)
    zs = perform_op(ys[:], op1=op1, op2=op2, param1=param1, param2=param2)
    ys.extend(zs)
    opts.append(ys)

    ys = xs[:]
    perform_op(ys, op1=op1, op2=op2, param1=param1, param2=param2)
    zs = perform_op(ys, op1=op1, op2=op2, param1=param1, param2=param2)
    ys.extend(zs)
    opts.append(ys)

    assign = "y = " + str(xs) + "\n"
    rand = random.randint(0, 3)
    if rand == 0:
        code = "g(y[:]).extend(g(y[:]))\n"
    elif rand == 1:
        code = "g(y[:]).extend(g(y))\n"
    elif rand == 2:
        code = "g(y).extend(g(y[:]))\n"
    else:
        code = "g(y).extend(g(y)[:])\n"

    question = "Consider the following function definition: \n\n" + func + \
               "\nWhat is the value of y after the following is evaluated?\n\n" + assign + code
    answer = opts[rand]

    return question, str(answer), [str(i) for i in opts] + ["Error"]


def gen_list_2():
    func = "def f(x, y):\n    y = y + [x]\n    return y\n\n"
    xs = rand_int_list(2)
    y = xs[-1] + 1
    code = f"w = {xs}\nw = f({y}, w) + w\n"
    ans = (xs[:] + [y]) + xs[:]
    opts = [ans, (xs[:] + [y]) + (xs[:] + [y]), xs[:] + (xs[:] + [y]), (xs[:] + [y]) + [xs[:]]]

    question = "What is the value of w after the following is evaluated?\n\n" + func + code

    return question, str(ans), [str(i) for i in opts] + ["None of the above"]


def gen_list_3():
    func = "def f(x, y):\n    y.append(x)\n    return y\n\n"
    xs = rand_int_list(2)
    y = xs[-1] + 1
    code = f"w = {xs}\nw = f({y}, w) + w\n"
    ans = (xs[:] + [y]) + (xs[:] + [y])
    opts = [ans, (xs[:] + [y]) + xs[:], xs[:] + (xs[:] + [y]), (xs[:] + [y]) + [xs[:]]]

    question = "What is the value of w after the following is evaluated?\n\n" + func + code

    return question, str(ans), [str(i) for i in opts] + ["None of the above"]


# append, count, extend, index, pop, remove, reverse, sort, insert

# list.append(S)/extend(S).fn
# list.index(list.pop(I)) without second
# list.index(list.pop(I)) with second
# list.index(list.remove(S)) without None
# list.index(list.remove(S)) with None
# list.insert(list.count(I)/min(list), len(list)/sum(list))

def gen_list_7():
    xs = []
    for i in range(5):
        xs.append(random.randint(0, 4))
    code = f"y = {xs}\ny.insert("
    r1 = random.randint(0, 1)
    r2 = random.randint(0, 1)
    if r1 == 0:
        rand = random.choice(xs)
        code += f"y.count({rand})"
        index = xs.count(rand)
    else:
        code += "min(y)"
        index = min(xs)
    if r2 == 0:
        code += ", len(y))\n"
        item = len(xs)
    else:
        code += ", sum(y))\n"
        item = sum(xs)

    if index != item:
        alt = index
    else:
        alt = index - 1

    ans = xs[:]
    ans.insert(index, item)
    opts = [ans, "Error"]

    ys = xs[:]
    ys.insert(index, alt)
    opts.append(ys)

    ys = xs[:]
    zs = xs[:]
    if index == len(xs):
        ys.insert(0, alt)
        zs.insert(0, item)
    else:
        ys.append(alt)
        zs.append(item)
    opts.append(ys)
    opts.append(zs)

    question = "What is the value of y after the following is evaluated?\n\n" + code
    return question, str(ans), [str(k) for k in opts]


def gen_list_6():
    xs = rand_list(4)
    random.shuffle(xs)
    choice = xs[random.randint(0, len(xs) - 3)]
    i = random.randint(0, 1)
    if i == 0:
        xs.pop(-1)
        xs.pop(-1)
        xs.insert(random.randint(0, len(xs) - 1), None)
        xs.insert(random.randint(0, len(xs) - 1), None)
    code = f"y = {xs}\nz = y.index(y.remove('{choice}'))"
    opts = []
    try:
        ys = xs[:]
        ans = ys.index(ys.remove(choice))
        opts.append(ans)
        opts.append("ValueError")
        for j in range(4):
            if j != ans:
                opts.append(j)
    except ValueError:
        ans = "ValueError"
        opts.append(ans)
        for j in range(4):
            opts.append(j)

    question = "What is the value of z after the following is evaluated?\n"\
               "Recall that lst.index(obj) returns the lowest index in lst that obj appears, " \
               "and throws a ValueError if obj is not in the list\n\n" + code
    return question, str(ans), [str(k) for k in opts]


def gen_list_5():
    xs = rand_int_list(4)
    random.shuffle(xs)
    i = random.randint(0, 1)
    pop_index = random.randint(0, len(xs) - 1)
    if i == 0:
        xs.remove(random.choice(xs))
        xs.insert(pop_index, random.choice(xs))
    code = f"y = {xs}\nz = y.index(y.pop({pop_index}))\n"
    opts = []
    try:
        ys = xs[:]
        ans = ys.index(ys.pop(pop_index))
        opts.append(ans)
        opts.append("ValueError")
        for j in range(4):
            if j != ans:
                opts.append(j)
    except ValueError:
        ans = "ValueError"
        opts.append(ans)
        for j in range(4):
            opts.append(j)

    question = "What is the value of z after the following is evaluated?\n" \
               "Recall that lst.index(obj) returns the lowest index in lst that obj appears, " \
               "and throws a ValueError if obj is not in the list\n\n" + code
    return question, str(ans), [str(k) for k in opts]


NO_ARG_FUNCS = [list.reverse, list.sort]
ONE_ARG_FUNCS = [list.append, list.count, list.index]


def gen_list_4():
    xs = rand_list(4)
    xs.append(xs.pop(0))
    code = f"y = {xs}\n"
    i = random.randint(0, 1)
    if i == 0:
        code += "y.append('A')"
    else:
        code += "y.extend('A')"

    j = random.randint(0, 1)
    opts = []
    xs.append('A')
    if j == 0:
        fn = random.choice(NO_ARG_FUNCS)
        code += f".{fn.__name__}()\n"

        ys = xs[:]
        ys.reverse()
        opts.append(str(ys))

        ys = xs[:]
        ys.sort()
        opts.append(str(ys))

        ys = xs[:]
        ys.reverse()
        ys.append(ys.pop(0))
        opts.append(str(ys))

        ys = xs[:]
        ys.sort()
        ys.append(ys.pop(0))
        opts.append(str(ys))
    else:
        fn = random.choice(ONE_ARG_FUNCS)
        elem = random.choice(xs)
        code += f".{fn.__name__}('{elem}')\n"

        ys = xs[:]
        ys.append(elem)
        opts.append(str(ys))

        index = xs.index(elem)
        opts.append(index)
        opts.append(index - 1)
        opts.append('None')

    opts.append("Error")
    ans = "Error"
    question = "What is the value of y after the following is evaluated?\n\n" + code
    return question, ans, opts

FUNCS = [gen_list_1, gen_list_1, gen_list_2, gen_list_3, gen_list_4, gen_list_5, gen_list_6, gen_list_7, gen_list_7]


def gen_list():
    func = random.choice(FUNCS)
    return func()


for i in gen_list():
    print(i)

