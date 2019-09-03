def kangaroo(x1, v1, x2, v2):
    '''

    :param x1,v1:integers, starting position and jump distance for kangaroo 1
    :param x2,v2:integers, starting position and jump distance for kangaroo 1
    :return: YES if they reach the same position at the same time, or NO if they don't.
    '''
    try:
        x = (v2*x1-v1*x2) % (v2-v1)
        y = (v2*x1-v1*x2) / (v2-v1)
        n1 = (y-x1) % v1
        n2 = (y-x2) % v2
        print(x,y)
        if x == 0 and n1 == 0 and n2 == 0 and y > 0 and y > x1 and y > x2:
            return 'Yes'
        else:
            return 'No'
    except:
        return 'No'
s = kangaroo(21,6, 47, 3)
print(s)