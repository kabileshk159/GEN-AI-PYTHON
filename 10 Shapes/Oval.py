oval1 = [(3,4), (3,5), (3,6), (4,2), (4,8), (5,1), (5,9), (6,1), (6,9), (7,2), (7,8), (8,4), (8,5), (8,6)]
def shape_oval():
    print('OVAL')
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in oval1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
shape_oval()
