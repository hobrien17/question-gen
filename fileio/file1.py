def sum_up(filename):
    total = 0
    with open(filename, "r") as f:
        for line in f:
            if line.strip().isdigit():
                total += int(line)
    return total
#R:Good

def sum_up(filename):
    total = 0
    with open(filename, "w") as f:
        for line in f:
            if line.strip().isdigit():
                total += int(line)
    return total
#R:Error

def sum_up(filename):
    total = 0
    with open(filename, "r") as f:
        for line in f:
            total += int(line)
    return total
#R:Error

def sum_up(filename):
    total = 0
    with open(filename, "r") as f:
        line = f.readline()
        while line != "":
            if line.strip().isdigit():
                total += int(line)
            line = f.readline()
    return total
#R:Good

def sum_up(filename):
    total = 0
    with open(filename, "r") as f:
        line = f.readline()
        while line is not None:
            if line.strip().isdigit():
                total += int(line)
            line = f.readline()
    return total
#R:Loop

def sum_up(filename):
    total = 0
    f = open(filename, "r"):
    for line in f:
        if line.strip().isdigit():
            total += int(line)
    f.close()
    return total
#R:Good

def sum_up(filename):
    total = 0
    f = open(filename, "r"):
    for line in f:
        if line.strip().isdigit():
            total += int(line)
    return total
#R:Leak