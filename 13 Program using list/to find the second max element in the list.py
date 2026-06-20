# to find the second max element
list= [1,77,6,9,6,345]
firstmax= list[0]
secondmax= list[0]
for i in range (len(list)):
    if firstmax<list[i]:
        secondmax= firstmax
        firstmax= list[i]
    elif list[i]>secondmax and list[i]!= firstmax:
        secondmax = i
print('second max is', secondmax)
