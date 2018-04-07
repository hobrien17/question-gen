import random
import string
import re

NONE = "None of the above"
MORE = "More than one of the above is correct"

CLASSES = ["classes/class1.py", "classes/class2.py", "classes/class3.py", "classes/class4.py",
           "classes/class5.py", "classes/class6.py"]
Q_CLASSES = ["classes/qclass1.py", "classes/qclass2.py", "classes/qclass3.py", "classes/qclass4.py",
             "classes/qclass5.py", "classes/qclass6.py"]


NAMES = ["Fred", "Joe", "Bill", "Bob", "Sam", "Rob", "Mike", "Matt", "Charlie", "James", "Jim", "Pete", "Trevor"]
MONSTERS = ["Vampire", "Ghost", "Troll", "Alien", "Demogorgon", "Zombie", "Gremlin", "Banshee", "Cyclops"]
CLUBS = ["Chess Club", "Computer Club", "Sports Club", "Science Club", "Book Club", "Movie Club"]
COUNTRIES = ["Australia", "New Zealand", "USA", "China", "Japan", "France", "England", "Germany", "Canada", "Egypt"]
CARS = ["Toyota", "VW", "BMW", "Mercedes", "Porche", "Jaguar", "Nissan", "Honda", "Holden", "Ford", "Opal"]


def load_class(classes):
    content = []
    class_file = random.choice(classes)
    with open(class_file, "r") as file:
        for line in file:
            content.append(line.replace("    ", "\t").rstrip())
    return content


def strip_lst(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] != '':
            return lst[:i+1]


def count_tabs(line):
    count = 0
    for i in range(len(line)):
        if line[i] != '\t':
            return count
        else:
            count += 1


def get_var(line):
    _, _, rest = line.partition("self.")
    var = re.split(r"[ .)]", rest)[0]
    return var


def replace_ops(line):
    if " < " in line:
        return line.replace("<", "<=")
    elif " <= " in line:
        return line.replace("<=", "<")
    elif " >= " in line:
        return line.replace(">=", ">")
    elif " > " in line:
        return line.replace(">", ">=")
    elif " != " in line:
        return line.replace("!=", "!==")
    elif " == " in line:
        return line.replace("==", "=")
    elif ".isdigit() " in line:
        return line.replace(".isdigit()", ".isnumber()")
    elif ".isalpha() " in line:
        return line.replace(".isalpha()", ".isstring()")
    return ""


def gen_class_1():
    base = []
    method = []

    content = load_class(CLASSES)
    length = int(content[0][1])
    chosen = random.randint(1, length)
    for line in content[1:]:
        if line.endswith("#"):
            if int(line[-3]) == chosen:
                method.append(line)
        else:
            base.append(line)

    ans = None
    opts = [MORE]

    for i, line in enumerate(method):
        if line[-2] != "X":
            stripped = line[:-4].strip()
            ans = stripped
            opts.append(ans)
            var = get_var(line)
            if line[-2] == "R":
                opts.append(stripped.replace(var, var[1:]))
                opts.append(stripped.replace("return ", "print(") + ")")
                opts.append(stripped.replace(var, var[1:]).replace("return ", "print(") + ")")
            elif line[-2] == "O":
                opts.append(stripped.replace(var, var[1:]))
                opts.append(stripped.replace("self." + var, var[1:]))
                opts.append(stripped.replace("self." + var, var))
            elif line[-2] == "B":
                opts.append(stripped.replace("self." + var, var[1:]))
                opts.append(stripped.replace("self." + var, var[1:]).replace("return", "return if"))
                opts.append(stripped.replace("return", "return if"))
            method[i] = count_tabs(line)*"\t" + "#####"
        else:
            method[i] = line[:-4].rstrip()

    class_body = "\n".join(strip_lst(base)) + "\n\n" + "\n".join(strip_lst(method))
    question = f"Consider the following class: \n\n{class_body}\n\n" \
               f"What line of code should replace ##### so that the method satisfies the docstring?\n"
    return question, ans, opts


def gen_vars():
    flt = round(random.uniform(1, 50), 2)
    negflt = round(random.uniform(-50, -1), 2)
    lowfloat = round(random.uniform(1, 19), 2)
    highfloat = round(random.uniform(20, 50), 2)
    return {"var": random.choice(["w", "x", "y", "z"]), "name": random.choice(NAMES),
            "float": flt, "negfloat": negflt, "posnegfloat": negflt*-1, "monster": random.choice(MONSTERS),
            "highfloat": highfloat, "nonhighfloat": lowfloat, "lowfloat": lowfloat, "nonlowfloat": highfloat,
            "club": random.choice(CLUBS), "country": random.choice(COUNTRIES), "car": random.choice(CARS)}


def gen_class_2():

    base = []
    lines = []
    gen = gen_vars()

    content = load_class(Q_CLASSES)
    for line in content:
        if line.endswith("#"):
            lines.append(line)
        else:
            base.append(line)

    chosen = random.choice(lines)
    code = chosen.split("#")[0].strip()
    orig = code
    question = chosen.split("#")[1]
    for i, j in gen.items():
        code = code.replace("{" + i + "}", str(j))
        question = question.replace("{" + i + "}", str(j))

    if chosen[-2] == "I":
        ans = gen["var"] + " = " + code
        class_body = "\n".join(strip_lst(base))
        question = f"Consider the following class:\n\n{class_body}\n\n" \
                   f"Which of the following {question.rstrip()}?\n"

        part = code.partition("(")
        alt1 = part[0] + "(" + gen["var"] + ", " + part[2]
        alt2 = gen["var"] + " = " + part[0] + "(" + gen["var"] + ", " + part[2]
        alt3 = gen["var"] + " = " + part[0] + "(self, " + part[2]
        opts = [ans, alt1, alt2, alt3, NONE]

        return question, ans, opts

    elif chosen[-2] == "M":
        ans = gen["var"] + "." + code
        class_body = "\n".join(strip_lst(base))
        question = f"Consider the following class:\n\n{class_body}\n\n" \
                   f"Which of the following {question.rstrip()}?\n"

        part = code.partition("(")
        variable = part[2][:-1]
        alt1 = part[0] + "(" + gen["var"] + ", " + part[2]
        alt2 = part[0] + "(" + gen["var"] + ")" + " += " + variable
        alt3 = gen["var"] + "." + part[0] + "()" + " += " + variable
        opts = [ans, alt1, alt2, alt3, NONE]

        return question, ans, opts

    elif chosen[-2] == "B":
        ans = gen["var"] + " = " + code
        class_body = "\n".join(strip_lst(base))
        question = f"Consider the following class:\n\n{class_body}\n\n" \
                   f"Which of the following {question.rstrip()}?\n"

        part = orig.partition("(")
        variables = part[2][:-1].split(", ")
        alt1 = gen["var"] + " = " + part[0] + "(" + str(gen[variables[1].strip('{}"')]) + ', "' + \
               str(gen[variables[0].strip('{}"')]) + '")'
        alt2 = gen["var"] + " = " + part[0] + '("' + str(gen[variables[0].strip('{}"')]) + '", ' + \
               str(gen["non" + variables[1].strip('{}"')]) + ")"
        alt3 = gen["var"] + " = " + part[0] + "(" + str(gen["non" + variables[1].strip('{}"')]) + ', "' + \
               str(gen[variables[0].strip('{}"')]) + '")'
        opts = [ans, alt1, alt2, alt3, NONE]

        return question, ans, opts

    return None


FUNCS = [gen_class_1, gen_class_2]


def gen_class():
    fn = random.choice(FUNCS)
    return fn()
