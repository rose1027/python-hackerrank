# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fh = open('words.txt')
count = 0
sumary = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        leftpos = line.find('0')
        number = line[leftpos:]
        #print(number)
        num = float(number)
        #print (num)
        count = count + 1
        sumary = sumary + num
        #print ('count =', count)
        avg = sumary / count
        #format the average, keep 12 digit
        #print('{:.12f}' .format(avg).rstrip("0"))-works!!!
print('{:.12f}'.format(avg).rstrip())
    #print('total = ', sumary)
    #print('average = ', avg)
