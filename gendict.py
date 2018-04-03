import random
import string

CARS = ["Toyota Camry", "Chevrolet Camaro", "Toyota Highlander", "Ford Escape", "Honda Civic", "Nissan Altima"]
NAMES = ["Fred", "Bob", "Joe", "Jim", "Bill", "Sue", "Kate", "Matt", "John", "Rob", "Liz", "Jenny", "Mary", "Mike"]
CITIES = ["Brisbane", "Adelaide", "Canberra", "Darwin", "Sydney", "Perth", "Cairns", "Townsville", "Newcastle"]
COUNTRIES = ["Australia", "USA", "Canada", "China", "Japan", "France", "England", "India", "Germany", "Spain", "Italy"]
FOOD = ["Apples", "Pears", "Oranges", "Bread", "Steak", "Eggs", "Potatoes", "Carrots", "Candy", "Milk", "Cream"]
COMPANIES = ["Apple", "Microsoft", "Google", "Facebook", "Amazon", "Netflix", "Atlassian", "IBM", "Intel", "HP"]
JOBS = ["Doctor", "Engineer", "Mechanic", "Lawyer", "Scientist", "Programmer", "Plumber", "Builder", "Pharmacist"]
YEARS = [i for i in range(2000, 2017)]

# {person : {age:height}}
# {person : {"occupation":job, "married":married}}
# {item : {"price":price, "quantity":quantity}}
# {city : {year:rainfall}}
# {country : {year:population}}
# {company : {year:networth}}
# {city : {"latitude":country, "longitude":city}}
# {car : {"year":year, "price":price}}


def rand_dict():
    d = {}
    name = ""
    lst = []
    rand = random.randint(0, 7)
    if rand == 0:
        lst = NAMES[:]
        for i in range(2):
            person = random.choice(lst)
            lst.remove(person)
            age1 = random.randint(2, 9)
            age2 = age1 + 1
            height1 = random.randint(100, 140)
            height2 = random.randint(height1, 150)
            d[person] = {age1: height1, age2: height2}
            name = "heights"
    elif rand == 1:
        lst = NAMES[:]
        for i in range(2):
            person = random.choice(lst)
            lst.remove(person)
            d[person] = {"occupation": random.choice(JOBS), "married": random.choice([True, False])}
            name = "people"
    elif rand == 2:
        lst = FOOD[:]
        for i in range(2):
            item = random.choice(lst)
            lst.remove(item)
            d[item] = {"price": random.randint(2, 10), "quantity": random.randint(20, 200)}
            name = "items"
    elif rand == 3:
        lst = CITIES[:]
        for i in range(2):
            city = random.choice(lst)
            lst.remove(city)
            year = random.choice(YEARS)
            d[city] = {year: round(random.random()*30, 2), year + 1: round(random.random()*30, 2)}
            name = "rainfall"
    elif rand == 4:
        lst = COUNTRIES[:]
        for i in range(2):
            country = random.choice(lst)
            lst.remove(country)
            year = random.choice(YEARS)
            pop1 = random.randint(1000000, 10000000)
            pop2 = random.randint(pop1, 15000000)
            d[country] = {year: pop1, year + 1: pop2}
            name = "population"
    elif rand == 5:
        lst = COMPANIES[:]
        for i in range(2):
            comp = random.choice(lst)
            lst.remove(comp)
            year = random.choice(YEARS)
            d[comp] = {year: random.randint(1000000000, 10000000000), year + 1: random.randint(1000000000, 10000000000)}
            name = "networth"
    elif rand == 6:
        lst = CITIES[:]
        for i in range(2):
            city = random.choice(lst)
            lst.remove(city)
            d[city] = {"latitude": round(random.uniform(-1, 1)*180, 3),
                       "longitude": round(random.uniform(-1, 1)*180, 3)}
            name = "location"
    elif rand == 7:
        lst = CARS[:]
        for i in range(2):
            car = random.choice(lst)
            lst.remove(car)
            d[car] = {"year": random.choice(YEARS), "value": random.randint(20000, 100000)}
            name = "cars"

    return d, name, lst


# d.get(k1, {k2: v}).get(k2) -> k1 in dict, k2 not in dict => None
# d.get(k1, {k2: v}).get(k2) -> k1 not in dict => v
# d.get(k1).get(k2) -> k1 not in dict => AttributeError
# d.get(k1, {}).get(k2, {}) -> k1 in dict, k2 in dict => d[k1][k2]
# d[k1].keys() -> keys in dict => []
# d[k1][k2] -> k2 not in dict => KeyError
# d[[k]] = v
# d[(k1,k2)] = v


def get_non_key(d: dict):
    keys = list(d.keys())
    while True:
        if isinstance(keys[0], int):
            new_key = random.randint(0, 10)
            if new_key not in keys:
                return new_key
        else:
            return random.choice(string.ascii_uppercase)


def add_to_dict_str(s, new_key, new_val):
    return s[:-1] + ", " + str(new_key) + ": " + str(new_val) + "}"


def fix(i):
    if isinstance(i, str):
        return f"'{i}'"
    return str(i)


def gen_dict_8():
    d, name, lst = rand_dict()
    d1 = dict(d)
    d2 = dict(d)
    d3 = {k: dict(d[k]) for k in d}
    d4 = {k: dict(d[k]) for k in d}
    k1 = list(d.keys())[0]
    k2 = list(d.keys())[1]
    k = (k1, k2)
    rand = random.randint(1, 100)
    d1[k] = rand
    d2[k1] = rand
    d2[k2] = rand
    d3[k1][k] = rand
    d4[k2][k] = rand

    ans = str(d1)
    exp = f"{name} = {d}\nd[{fix(k)}] = {rand}\n"
    question = "What is the value of d after the following is evaluated?\n\n" + exp
    opts = [
        ans, "Error", str(d2), str(d3), str(d4)
    ]
    return question, ans, opts

def gen_dict_7():
    d, name, lst = rand_dict()
    d1 = str(d)
    d2 = str(d)
    d3 = {k: dict(d[k]) for k in d}
    d4 = {k: dict(d[k]) for k in d}
    k1 = random.choice(lst)
    rand = random.randint(1, 100)
    d1 = add_to_dict_str(d1, f"[{fix(k1)}]", rand)
    d2 = add_to_dict_str(d2, fix(k1), rand)
    in1 = list(d3.keys())[0]
    in2 = list(d3.keys())[1]
    d3[in1][k1] = rand
    d4[in2][k1] = rand

    ans = "Error"
    exp = f"{name} = {d}\nd[[{fix(k1)}]] = {rand}\n"
    question = "What is the value of d after the following is evaluated?\n\n" + exp
    opts = [
        ans, str(d1).replace("{", "{{").replace("}", "}}").format("x"), str(d2), str(d3), str(d4)
    ]
    return question, ans, opts


def gen_dict_6():
    d, name, lst = rand_dict()
    i = random.randint(0, 1)
    k1, d2 = list(d.items())[i]
    k2 = get_non_key(d2)
    alt1 = list(d2.values())[0]
    alt2 = list(d2.values())[1]

    ans = "Error"
    exp = f"{name} = {d}\ny = {name}[{fix(k1)}][{fix(k2)}]\n"
    question = "What is the value of y after the following is evaluated?\n\n" + exp
    opts = [
        ans, "None", "-1", fix(alt1), fix(alt2)
    ]
    return question, ans, opts


def gen_dict_5():
    d, name, lst = rand_dict()
    i = random.randint(0, 1)
    k1, d2 = list(d.items())[i]
    keys = list(d2.keys())
    vals = list(d2.values())
    other_keys = list(list(d.values())[1 - i].keys())
    other_values = list(list(d.values())[1 - i].values())

    ans = str(keys)
    exp = f"{name} = {d}\ny = list({name}[{fix(k1)}].keys())\n"
    question = "What is the value of y after the following is evaluated?\n\n" + exp
    opts = [
        ans, str(vals), str(other_keys), str(other_values), "Error"
    ]
    return question, ans, opts


def gen_dict_4():
    d, name, lst = rand_dict()
    i = random.randint(0, 1)
    j = random.randint(0, 1)
    k1, d2 = list(d.items())[i]
    k2, v = list(d2.items())[j]
    v2 = list(list(d.values())[i].values())[1 - j]
    v3 = random.choice(list(list(d.values())[1 - i].values()))
    empty = {}

    exp = f"{name} = {d}\ny = {name}.get({fix(k1)}, {empty}).get({fix(k2)}, {empty})\n"
    question = "What is the value of y after the following is evaluated?\n\n" + exp
    ans = fix(v)
    opts = [
        ans, "{}", "Error", fix(v2), fix(v3)
    ]
    return question, ans, opts


def gen_dict_3():
    d, name, lst = rand_dict()
    k1 = random.choice(lst)
    k2 = random.choice(list(random.choice(list(d.values())).keys()))
    v1 = list(list(d.values())[0].values())[0]
    v2 = list(list(d.values())[0].values())[1]
    v3 = random.choice(list(list(d.values())[1].values()))

    exp = f"{name} = {d}\ny = {name}.get({fix(k1)}).get({fix(k2)})\n"
    question = "What is the value of y after the following is evaluated?\n\n" + exp
    ans = "Error"
    opts = [
        ans, "None", fix(v1), fix(v2), fix(v3)
    ]
    return question, ans, opts


def gen_dict_2():
    d, name, lst = rand_dict()
    k1 = random.choice(lst)
    k2 = random.choice(list(random.choice(list(d.values())).keys()))
    rand = random.randint(0, 10)
    d_alt = {k2: rand}
    v1 = random.choice(list(list(d.values())[0].values()))
    v2 = random.choice(list(list(d.values())[1].values()))

    exp = f"{name} = {d}\ny = {name}.get({fix(k1)}, {d_alt}).get({fix(k2)})\n"
    question = "What is the value of y after the following is evaluated?\n\n" + exp
    ans = f"{rand}"
    opts = [
        ans, "Error", "None", fix(v1), fix(v2)
    ]

    return question, ans, opts


def gen_dict_1():
    d, name, lst = rand_dict()
    k, d2 = random.choice(list(d.items()))
    k2 = get_non_key(d2)
    rand = random.randint(0, 10)
    d_alt = {k2: rand}

    exp = f"{name} = {d}\ny = {name}.get({fix(k)}, {d_alt}).get({fix(k2)})\n"
    question = "What is the value of y after the following is evaluated?\n\n" + exp
    ans = "None"
    opts = [
        ans, "Error", f"{rand}", fix(list(d2.values())[0]), fix(list(d2.values())[1])
    ]

    return question, ans, opts


FUNCS = [gen_dict_1, gen_dict_2, gen_dict_3, gen_dict_4, gen_dict_5, gen_dict_6, gen_dict_7, gen_dict_8]


def gen_dict():
    func = random.choice(FUNCS)
    question, ans, opts = func()
    while len(set(opts)) < 5:
        question, ans, opts = func()
    return question, ans, opts
