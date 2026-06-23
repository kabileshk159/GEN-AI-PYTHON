# to count the no of vowels in the given string 
a=str(input('enter a string:'))
a=a.lower()
count=0
for i in range(len(a)):
    if a[i]=='a' or  a[i]=='e'or a[i]=='i' or a[i]=='o'or a[i]=='u':
        count= count+1

if count>0:
    print(count)
else:
    print('no vowels')




           
        
