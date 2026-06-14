#LAMBDA FUNCTION TO FIND CUBEROOT VALUE
a=(8,27,64,125)
cuberoot= list(map(lambda a: a**(1/3),a))
print(cuberoot)
