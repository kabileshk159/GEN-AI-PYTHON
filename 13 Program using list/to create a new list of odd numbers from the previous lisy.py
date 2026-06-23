list=[2,3,4,5,6,7,8,11,15]
odd_list=[]
for i in range (((len(list)))):
    if not((list[i])%2)==0:
        odd_list.append(list[i])

print(odd_list)
