
def ratnumrow():
    f= open('pattern.txt','w+')
    f.write('RIGHT ANGLED TRIANGLE NUM ROW\n')
    for i in range(0,7):
        for j in range(0,i):
            f.write(str(i))
            f.write(' ')
        f.write('\n')
    f.close()
ratnumrow()

def ratnumcol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('RIGHT ANGLED TRIANGLE NUM COL\n')
    for i in range(0,7):
        for j in range(0,i):
            f.write(str(j))
            f.write(' ')
        f.write('\n')
    f.close()
ratnumcol()

def ratalpharow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('RIGHT ANGLED TRIANGLE ALPHA ROW\n')
    for i in range(0,7):
        for j in range(0,i):
            f.write(chr(i+64+32))
            f.write(' ')
        f.write('\n')
    f.close()
ratalpharow()

def ratalphacol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('RIGHT ANGLED TRIANGLE ALPHA COL\n')
    for i in range(0,7):
        for j in range(0,i):
            f.write(chr(j+65+32))
            f.write(' ')
        f.write('\n')
    f.close()
ratalphacol()


def ratalphaupperrow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('RIGHT ANGLED TRIANGLE ALPHA UPPER ROW\n')
    for i in range(0,7):
        for j in range(0,i):
            f.write(chr(i+64))
            f.write(' ')
        f.write('\n')
    f.close()
ratalphaupperrow()

def ratalphauppercol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('RIGHT ANGLED TRIANGLE ALPHA UPPER COL\n')
    for i in range(0,7):
        for j in range(0,i):
            f.write(chr(j+65))
            f.write(' ')
        f.write('\n')
    f.close()
ratalphauppercol()


def ratstar():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('RIGHT ANGLED TRIANGLE STAR\n')
    for i in range(0,7):
        for j in range(0,i):
            f.write('*')
            f.write(' ')
        f.write('\n')
    f.close()
ratstar()


def iratnumrow():
    f= open('pattern.txt','a+')
    f.write('INVERTED RIGHT ANGLED TRIANGLE NUM ROW\n')
    for i in range(7,0,-1):
        for j in range(0,i):
            f.write(str(i))
            f.write(' ')
        f.write('\n')
    f.close()
iratnumrow()

def iratnumcol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED RIGHT ANGLED TRIANGLE NUM COL\n')
    for i in range(7,0,-1):
        for j in range(0,i):
            f.write(str(j))
            f.write(' ')
        f.write('\n')
    f.close()
iratnumcol()

def iratalpharow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED RIGHT ANGLED TRIANGLE ALPHA ROW\n')
    for i in range(7,0,-1):
        for j in range(0,i):
            f.write(chr(i+64+32))
            f.write(' ')
        f.write('\n')
    f.close()
iratalpharow()

def iratalphacol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED RIGHT ANGLED TRIANGLE ALPHA COL\n')
    for i in range(7,0,-1):
        for j in range(0,i):
            f.write(chr(j+65+32))
            f.write(' ')
        f.write('\n')
    f.close()
iratalphacol()


def iratalphaupperrow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED RIGHT ANGLED TRIANGLE ALPHA UPPER ROW\n')
    for i in range(7,0,-1):
        for j in range(0,i):
            f.write(chr(i+64))
            f.write(' ')
        f.write('\n')
    f.close()
iratalphaupperrow()

def iratalphauppercol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED RIGHT ANGLED TRIANGLE ALPHA UPPER COL\n')
    for i in range(7,0,-1):
        for j in range(0,i):
            f.write(chr(j+65))
            f.write(' ')
        f.write('\n')
    f.close()
iratalphauppercol()


def iratstar():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED RIGHT ANGLED TRIANGLE STAR\n')
    for i in range(7,0,-1):
        for j in range(0,i):
            f.write('*')
            f.write(' ')
        f.write('\n')
    f.close()
iratstar()

def latnumrow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('LEFT ANGLED TRIANGLE NUM ROW\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i))
            
        f.write('\n')
    f.close()
latnumrow()

def latnumcol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('LEFT ANGLED TRIANGLE NUM COL\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(k))
            
        f.write('\n')
    f.close()
latnumcol()

def latalpharow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('LEFT ANGLED TRIANGLE ALPHA ROW\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64+32))
            
        f.write('\n')
    f.close()
latalpharow()

def latalphacol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('LEFT ANGLED TRIANGLE ALPHA COL\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(k+65+32))
        f.write('\n')
    f.close()
latalphacol()

def latalphaupperrow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('LEFT ANGLED TRIANGLE ALPHA UPPER ROW\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64))
            
        f.write('\n')
    f.close()
latalphaupperrow()

def latalphauppercol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('LEFT ANGLED TRIANGLE ALPHA UPPER COL\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(k+65))
        f.write('\n')
    f.close()
latalphauppercol()


def latstar():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('LEFT ANGLED TRIANGLE STAR\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()
latstar()

def ilatnumrow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED LEFT ANGLED TRIANGLE NUM ROW\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i))
            
        f.write('\n')
    f.close()
ilatnumrow()

def ilatnumcol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED LEFT ANGLED TRIANGLE NUM COL\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(k))
            
        f.write('\n')
    f.close()
ilatnumcol()

def ilatalpharow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED LEFT ANGLED TRIANGLE ALPHA ROW\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64+32))
            
        f.write('\n')
    f.close()
ilatalpharow()

def ilatalphacol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED LEFT ANGLED TRIANGLE ALPHA COL\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(k+65+32))
        f.write('\n')
    f.close()
ilatalphacol()

def ilatalphaupperrow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED LEFT ANGLED TRIANGLE ALPHA UPPER ROW\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64))
            
        f.write('\n')
    f.close()
ilatalphaupperrow()

def ilatalphauppercol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED LEFT ANGLED TRIANGLE ALPHA UPPER COL\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(k+65))
        f.write('\n')
    f.close()
ilatalphauppercol()


def ilatstar():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED LEFT ANGLED TRIANGLE STAR\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()
ilatstar()


def pyramidnumrow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('PYRAMID NUM ROW\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i))
            f.write(' ')
        f.write('\n')
    f.close()
pyramidnumrow()

def pyramidnumcol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('PYRAMID NUM COL\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(k))
            f.write(' ')
        f.write('\n')
    f.close()
pyramidnumcol()

def pyramidalpharow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('PYRAMID ALPHA ROW\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64+32))
            f.write(' ')
        f.write('\n')
    f.close()
pyramidalpharow()

def pyramidalphacol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('PYRAMID ALPHACOL\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(k+65+32))
            f.write(' ')
        f.write('\n')
    f.close()
pyramidalphacol()


def pyramidalphaupperrow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('PYRAMID ALPHA UPPER ROW\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64))
            f.write(' ')
        f.write('\n')
    f.close()
pyramidalphaupperrow()


def pyramidalphauppercol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('PYRAMID ALPHA UPPER COL\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(k+65))
            f.write(' ')
        f.write('\n')
    f.close()
pyramidalphauppercol()

def pyramidstar():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('PYRAMID STAR\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write('*')
            f.write(' ')
        f.write('\n')
    f.close()
pyramidstar()




def ipyramidnumrow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED PYRAMID NUM ROW\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i))
            f.write(' ')
        f.write('\n')
    f.close()
ipyramidnumrow()

def ipyramidnumcol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED PYRAMID NUM COL\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(k))
            f.write(' ')
        f.write('\n')
    f.close()
ipyramidnumcol()


def ipyramidalpharow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED PYRAMID ALPHA ROW\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64+32))
            f.write(' ')
        f.write('\n')
    f.close()
ipyramidalpharow()

def ipyramidalphacol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED PYRAMID ALPHACOL\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(k+65+32))
            f.write(' ')
        f.write('\n')
    f.close()
ipyramidalphacol()



def ipyramidalphaupperrow():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED PYRAMID ALPHA UPPER ROW\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64))
            f.write(' ')
        f.write('\n')
    f.close()
ipyramidalphaupperrow()


def ipyramidalphauppercol():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED PYRAMID ALPHA UPPER COL\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(k+65))
            f.write(' ')
        f.write('\n')
    f.close()
ipyramidalphauppercol()

def ipyramidstar():
    f= open('pattern.txt','a+')
    f.write('\n')
    f.write('INVERTED PYRAMID STAR\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write('*')
            f.write(' ')
        f.write('\n')
    f.close()
ipyramidstar()







            
            
    
