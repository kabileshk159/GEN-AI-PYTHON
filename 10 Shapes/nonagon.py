
nonagon1 = [(1,5), (2,3), (2,7), (4,1), (4,9), (6,1), (6,9), (8,2), (8,8), (9,4), (9,5), (9,6)]
def shape_nonagon():
    print('NONAGON')
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in nonagon1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
shape_nonagon()
