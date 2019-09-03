def removeduplicatedwords(lst):
    final_list = []
    for words in lst:
        if words not in final_list:
            final_list.append(words)
    return final_list

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
i = 0

for line in fh:
    line = line.rstrip()
    partlist = line.split()
    for i in range(len(partlist)):
        lst.extend(partlist)
        i = i+1
        break

lst.sort()

print(removeduplicatedwords(lst))
