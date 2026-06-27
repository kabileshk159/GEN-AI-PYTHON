octagon1 = [(2,4), (2,5), (2,6), (4,2), (4,8), (6,2), (6,8), (8,4), (8,5), (8,6)]
def shape_octagon():
    print('OCTAGON')
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in octagon1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
shape_octagon()
