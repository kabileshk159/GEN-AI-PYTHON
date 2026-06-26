
star1 = [(1,5), (2,5), (3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(4,3),(4,4),(4,5),(4,6),(4,7),(5,3),(5,4),
         (5,5),(5,6),(5,7),(6,3),(6,7),(7,2),(7,8)]
def shape_star():
    print('STAR')
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in star1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
shape_star()
