largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : break
    #invalid case
    try:
        number = int(num)
    except:
        print('Invalid input')
        continue
#find smallest number in input
    if smallest is None :
        smallest = number
    elif number < smallest:
        smallest = number

# find largest number in input
    if largest is None :
        largest = number
    elif number > largest :
        largest = number
print('Maximum', largest)
print('Minimum:', smallest)
