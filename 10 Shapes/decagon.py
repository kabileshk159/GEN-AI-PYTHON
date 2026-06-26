decagon1 = [(1,4), (1,5), (1,6), (3,2), (3,8), (5,1), (5,9), (7,2), (7,8), (9,4), (9,5), (9,6)]
def shape_decagon():
    print('DECAGON')
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in decagon1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
shape_decagon()
