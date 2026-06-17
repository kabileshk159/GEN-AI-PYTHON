square1 = [(2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8), (3,2), (3,8), (4,2), (4,8), (5,2), (5,8),
           (6,2), (6,8), (7,2), (7,8), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8)]
def shape_square():
    print('SQUARE')
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in square1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
shape_square()
