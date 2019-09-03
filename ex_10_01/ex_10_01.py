name = input("Enter file:")
if len(name) < 1 : name = "words.txt"
handle = open(name)
newlist = list()
counts = dict()


for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    else:
        #using string to find the specific location first
        numfirst = line.find(':')
        #print(numfirst)
        #print(line[numfirst-2:numfirst+6])
        difhour = line[numfirst-2:numfirst+6]
        #extract hour out put into newlist
        words = difhour.split(':')
        #print(words[0])
        indices = [0]
        newlist = [words[i] for i in indices]
        #print(newlist)
        for word in newlist:

            if word not in counts:
                counts[word] = 1
            else:
                counts[word] = counts[word]+ 1
#print(counts)
t = list(counts.items())
#print(t)
t.sort()
#print('sorted tuple****', t)
for key, val in t:
    print(key, val)
