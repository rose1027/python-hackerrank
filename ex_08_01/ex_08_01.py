fname = input("Enter file name: ")
# function to remove all repeated words.
def removeduplicatedwords(lst):
    final_list = []
    for words in lst:
        if words not in final_list:
            final_list.append(words)
    return final_list


fh = open(fname)
lst = list()

i = 0
# transfer string to a list using split, but that list(L) doesn't hold all the string so need a new list
#to  put all the numbers in newlist using extend not append
for line in fh:
    line = line.rstrip()
    L = line.split()
    for i in range(len(L)):
        lst.extend(L)
        i = i+1
        #break just jump out of innerloop!!
        break

lst.sort()

print(removeduplicatedwords(lst))
