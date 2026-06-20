# to remove the duplicate elements from list and print the updated list
k=[1,2,2,3,3,4,4,5]
updated=[]
for i in range(8):
    for j in range(i):
        if k[i]==k[j]:
            break
    else:
       updated.append(k[i])

print(updated)



