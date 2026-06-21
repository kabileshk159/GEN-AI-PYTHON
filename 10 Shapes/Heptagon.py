
heptagon1 = [(1,5),(2,4),(2,6),(3,3),(3,7),(5,2),(5,8),(6,3),(6,7),(8,4),(8,5),(8,6)]
def shape_heptagon():
    print('HEPTAGON')
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in heptagon1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
shape_heptagon()
