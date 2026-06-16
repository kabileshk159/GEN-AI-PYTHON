circle = [(5,1), (2,2), (1,5), (2,8), (5,9), (8,8), (9,5), (8,2)]
def shape_circle():
    print('CIRCLE')
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in circle:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
shape_circle()
