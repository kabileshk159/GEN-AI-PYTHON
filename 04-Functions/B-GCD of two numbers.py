def gcd(a,b):
    facta=[]
    factb=[]
    print('GCD of',a,',',b,'is')
    for i in range(a+1):
        if(a%(i+1)== 0): 
          facta.append(i+1)
          print(i+1,end=' ')
    print()
    for j in range(b+1):
        if(b%(j+1)== 0):
           factb.append(j+1)
           print(j+1,end=' ')
    print()
    common= []
    for k in facta:
        if k in factb:
           common.append(k)
    print('common factor is',max(common))
    
gcd(10,25)
