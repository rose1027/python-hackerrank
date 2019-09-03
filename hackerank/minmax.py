
# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    l = []
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    for j in range(len(arr)):
        temp = sum
        temp -= arr[j]
        l.append(temp)
    return min(l), max(l)

a,b = miniMaxSum([1,2,3,4,5])
print(a,b)



