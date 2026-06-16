heart = [(2,2), (2,3), (2,7), (2,8), (3,1), (3,4), (3,6), (3,9), (4,1),(4,5), (4,9), (5,2),
         (5,8), (6,3), (6,7), (7,4), (7,6), (8,5)]
def shape_heart():
    print('HEART')
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in heart:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
shape_heart()
