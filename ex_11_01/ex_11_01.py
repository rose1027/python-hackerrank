import re
name = input('Enter file name: ')
if len(name) < 1: name = 'regex_sum_149911.txt'
handle = open(name)
numberlist = list()
counts = 0

for line in handle:
    line = line.rstrip()
    words = re.findall('([0-9]+)', line)
    if len(words)<1: continue
    #print("number*******")
    #print(words)
    numberlist.extend(words)
    #print ('*****whole list of string*****')

for index, item in enumerate(numberlist):
    numberlist[index] = int(item)
#print(numberlist)
print(sum(numberlist))
