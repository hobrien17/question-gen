def fn(in_file):
    """Takes a file of comma-separated integers and returns a list of all unique integers that are larger than the first integer.

    Example data file (input.csv):
        3,5,2,1,3,7,7,4,5

    Example usage:
        >>> fn('input.csv')
        [5, 7, 4]
        >>>
    """
    result = []
    with open(in_file, "r") as f: #with open(in_file, "w") as f:/while open(in_file, "r") as f:/while open(in_file, "w") as f:
        line = f.readline().strip() #line = f.read().strip()/line = f.strip()/line = [i.strip() for i in f]
        first = None
        for col in line.split(","): #for col in line:/for col in line.partition(","):/for col in list(line):
            if first is None:
                first = int(col)
            else:
                if int(col) > first and int(col) not in result: #if int(col) > first and int(col) in result/if int(col) > first or int(col) not in result/if int(col) > first or int(col) in result
                    result.append(first)

    return result
#4
def fn(in_file):
    """Takes a file with two lines. The first line contains a string. The second line contains a series of comma-separated strings. 
        This function returns a list of all the second-line strings that have characters in the first string.

    Example data file (input.csv):
        puppies
        cat,cats,dog,pet,fish

    Example usage:
        >>> fn('input.csv')
        [cats, pet, fish]
        >>>
    """
    result = []
    with open(in_file, "r") as f: #with open(in_file, "w") as f:/while open(in_file, "r") as f:/while open(in_file, "w") as f:
        first = f.readline().strip()
        second = f.readline().strip()
        for string in second.split(","):
            for i in range(len(string)): #for i in second:/for i in string:/for i in range(len(second)):
                if string[i] in first: #if string in first:/if i in first:/if string[0] in first:
                    result.append(string)
                    break #continue/pass/return result

    return result
#4
def fn(in_file):
    """Takes a comma-separated-values file and returns a list whose elements are the sums of the file's columns. 
        We assume the file contains rows of integers separated by commas and each row has the same number of ints.

    Example data file (input.csv):
        3,4,3,2
        7,5,1,8
        0,0,5,5

    Example usage:
        >>> fn('input.csv')
        [10, 9, 9, 15]
        >>>
    """
    data = []
    with open(in_file, "r") as f:
        for line in f:
            data.append([])
            for val in line:
                data[-1].append(int(val)) #data.append(int(val))/data[0].append(int(val))/data.append([int(val)])

    result = []
    for i in range(len(data[0])): #for i in range(len(data))/for i in data/for i in data[0]
        total = 0
        for j in range(len(data)): #for j in range(len(data[0]))/for j in data/for j in data[0]
            total += data[j][i] #total += data[i][j]/total = data[i][j]/total = data[j][i]
        result.append(total)

    return result
#4
def fn(data):
    """Takes a list of sublists containing integers. The elements of each sublist are written to a new line of 
        output.csv, with elements separated by commas. Any negative integers or integers greater than 100 are ignored.

    Example usage:
        >>> fn([[1, 2, 3, 4], [5, 4, 5], [-2, 3, 200, 1]])
        >>>

    Example data file (output.csv) after the above execution:
        1,2,3,4
        5,4,5
        3,1
    """
    with open("output.csv", "w") as f:
        for sublist in data:
            to_write = []
            for elem in sublist:
                if elem < 0 or elem > 100: #if elem < 0 and elem > 100:/if 0 > elem > 100:/if 0 < elem < 100:
                    pass #break/continue/return
                else:
                    to_write.append(elem)
            line = ",".join(to_write) #line = to_write.join(",")/line = "\n".join(to_write)/line = to_write.join("\n")
            f.write(line + "\n") #f.writeline(line + "\n")/f.writeline(line)/f.write(line)
#4
def fn(data):
    """Takes a list of tuples of the form (i, j), where i is an int and j is a string. 
        For each tuple, a new line is written to output.csv containing i occurences of j, separated by commas.
        If i is a number less than or equal to 0, the function immediately ends, and output.csv is not modified.

    Example usage:
        >>> fn([(3, "a"), (4, "x"), (1, "q")])
        >>>

    Example data file (output.csv) after the above execution:
        a,a,a
        x,x,x,x
        q
    """
    f = open("output.csv", "w") #f = open("output.csv", "r")/f = with open("output.csv", "w")/f = with open("output.csv", "r")
    output = ""
    for pair in data:
        line = []
        if pair[0] <= 0:
            f.close()
            return #break/pass/exit
        for i in range(pair[0]): #for i in range(len(pair[0])):/for i in range(len(pair)):/for i in pair:
            line.append(pair[1])
        output += ",".join(line) + "\n" #output += ",".join(line)/output = ",".join(line)/output = ",".join(line) + "\n"
    f.write(output)
    f.close()
#4