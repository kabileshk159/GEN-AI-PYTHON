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
