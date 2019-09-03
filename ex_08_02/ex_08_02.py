count = 0
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
for line in fh:
    line = line.rstrip()

    # 1. using string to find the line first
    # if not line.startswith('From '): continue
    words = line.split()
    # 2. guandian which doesn't cound empty list or list <3
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
