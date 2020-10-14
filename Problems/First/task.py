# read test_file.txt
fp = open("test_file.txt", "r", encoding='utf-16')
for line in fp:
    print(line)
    break
fp.close()
