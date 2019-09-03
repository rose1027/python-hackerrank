
# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    '''

    :param s: integer, starting point of Sam's house location.
    :param t: integer, ending location of Sam's house location.
    :param a:integer, location of the Apple tree.
    :param b: integer, location of the Orange tree.
    :param apples:integer array, distances at which each apple falls from the tree.
    :param oranges:integer array, distances at which each orange falls from the tree.
    :it should print the number of apples and oranges that land on Sam's house, each on a separate line.
    '''
    new_app = [x+a for x in apples]
    new_org = [y+b for y in oranges]
    n_app = [c for c in new_app if c >= s and c<= t]
    n_org = [c for c in new_org if c >= s and c <= t ]
    print(len(n_app),len(n_org))

countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])