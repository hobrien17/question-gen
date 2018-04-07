def fn(in_file, out_file):
    inp = open(in_file, "r")
    out = open(out_file, "w")

    output = []
    for line in inp:
        parts = line.strip().split(",")
        x = 0
        for part in parts:
            x += int(part)
        output.append(str(x))
    out.write(",".join(output))

    inp.close()
    out.close()
#sum

def fn(in_file, out_file):
    inp = open(in_file, "r")
    out = open(out_file, "w")

    output = []
    for line in inp:
        parts = line.strip().split(",")
        x = None
        for part in parts:
            if x is None:
                x = int(part)
            elif int(part) > x:
                x = int(part)
        output.append(str(x))
    out.write(",".join(output))

    inp.close()
    out.close()
#max

def fn(in_file, out_file):
    inp = open(in_file, "r")
    out = open(out_file, "w")

    output = []
    for line in inp:
        parts = line.strip().split(",")
        x = None
        for part in parts:
            if x is None:
                x = int(part)
            elif int(part) < x:
                x = int(part)
        output.append(str(x))
    out.write(",".join(output))

    inp.close()
    out.close()
#min

def fn(in_file, out_file):
    inp = open(in_file, "r")
    out = open(out_file, "w")

    output = []
    for line in inp:
        parts = line.strip().split(",")
        x = 0
        for part in parts:
            x += 1
        output.append(str(x))
    out.write(",".join(output))

    inp.close()
    out.close()
#len