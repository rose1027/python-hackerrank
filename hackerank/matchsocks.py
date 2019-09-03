# n: the number of socks in the pile.ar: the colors of each sock
def sockMerchant(n, ar):
    dict = {}
    count = 0
    for c in ar:
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1
    for value in dict.values():
        pair = value // 2
        count += pair
    return count
n = sockMerchant(9,[10,20,20,10,10,30,50,10,20])
print(n)




