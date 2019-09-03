
name = input("Enter file:")
if len(name) < 1 : name = "words.txt"
handle = open(name)
counts = dict()
newlist = list()
bigvalue = None
bigkey = None


for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    else:
            words = line.split()
            #print('******words[1]*****')
            #print(words[1])
            #print('new list*******')
            # make me stuck forever!!!! extract emails from list using specific indice
            indices = [1]
            newlist = [words[i] for i in indices]
            #print(newlist)

            for word in newlist:

                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] = counts[word]+ 1

# find bigest count number and print out!
for key, value in counts.items():
    if bigvalue is None or value > bigvalue:
        bigvalue = value
        bigkey = key
print(bigkey, bigvalue)


#print(counts)
