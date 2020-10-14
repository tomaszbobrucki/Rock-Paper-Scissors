# read test.txt
cdd = open("test.txt", "r")
for line in cdd:
    print(line[0])
cdd.close()
