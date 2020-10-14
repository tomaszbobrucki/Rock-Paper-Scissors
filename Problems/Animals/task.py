# read animals.txt
# and write animals_new.txt
file1 = open("animals.txt", "r")
file2 = open("animals_new.txt", "w")
animals = file1.readlines()
ani2 = []

for line in animals:
    ani2.append(line.rstrip())

ani = " ".join(ani2)
file2.write(ani)
file1.close()
file2.close()
