hexagon1 = [(1,4),(1,5),(1,6),(1,7),(2,3),(2,8),(3,2),(3,9),(4,3),(4,8),(5,4),(5,5),(5,6),(5,7)]
def shape_hexagon():
    print('HEXAGON')
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in hexagon1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
shape_hexagon()
