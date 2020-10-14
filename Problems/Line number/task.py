# read sample.txt and print the number of lines
file1 = open("sample.txt", "r")
all1 = 0
for _ in file1:
    all1 += 1
print(all1)
file1.close()
