# to find the sum
list = [1,2,3,4,5]
k=0
for i in range (len(list)):
    j= k+list[i]
    k=j
print(k )

# to find the max element
list= [1,77,6,9,6,345]
max= list[0]
for i in range (len(list)):
    if max<list[i]:
     max= list[i]

print(max)

#to find the min
list=[22.4,33.3,4.33,5.56,66.0,99.8,53.7,20.6]
mini= list[0]
for i in range (len(list)):
    if list[i]< mini:
        mini=list[i]
print(mini)

# to find the average of list
list = [1,2,3,4,5]
print(sum(list)/(len(list)))

# to count the no of even no in the list
list = [1,2,3,4,5,6,6]
k=0
for i in range (len(list)):
    if (list[i])%2==0:
        k=k+1
print(k )
