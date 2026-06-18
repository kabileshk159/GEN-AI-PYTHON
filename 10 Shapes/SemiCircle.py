semi_circle1 = [(3,4), (3,5), (3,6), (4,2), (4,8), (6,1), (6,9), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8), (7,9)]
def shape_semi_circle():
    print('SEMI CIRCLE')
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in semi_circle1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
shape_semi_circle()
