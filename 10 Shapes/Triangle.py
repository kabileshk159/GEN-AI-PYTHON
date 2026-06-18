def shape_triangle():
    print('TRIANGLE')
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in triangle1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
shape_triangle()
