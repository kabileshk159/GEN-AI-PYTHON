rectangle1 = [(1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (2,2), (2,9), (3,2), (3,9),
              (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9)]
def shape_rectangle():
    print('RECTANGLE')
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in rectangle1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
shape_rectangle()
