# convert a list of integers to single integer
c=[22,3,44,3]
d=''
for i in range (len(c)):
    d=d+str(c[i])
d=int(d)
print(int(d))
