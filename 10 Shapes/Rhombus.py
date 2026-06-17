rhombus1 = [(1,3), (1,4), (1,5), (1,6), (1,7), (3,2), (3,6), (5,1), (5,2), (5,3), (5,4), (5,5)]
def shape_rhombus():
    print('RHOMBUS')
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in rhombus1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
shape_rhombus()
