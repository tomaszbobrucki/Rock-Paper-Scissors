# read sums.txt
fi = open("sums.txt", "r")
for line in fi:
    x, y = line.split()
    print(int(x) + int(y))
fi.close()
