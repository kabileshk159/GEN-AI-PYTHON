
# to find the common element in  between two lists
a= [1,77,6,9,6,345,3,5,5,5,5,4,22]
b= [3,4,22,77]
com=[]
for i in range (len(a)):
    for j in range(len(b)):
       if a[i]==b[j]:
           com.append(a[i])
print(com)
