trapezoid1 = [(2,3), (2,4), (2,5), (2,6), (2,7), (3,2), (3,8), (4,1), (4,9), (5,0),(5,1), (5,2), (5,3), (5,4),
              (5,5), (5,6), (5,7), (5,8), (5,9),(5,10)]
def shape_trapezoid():
    print('TRAPEZOID')
    for i in range(0, 11):
        for j in range(0, 11):
            if (i, j) in trapezoid1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
shape_trapezoid()
