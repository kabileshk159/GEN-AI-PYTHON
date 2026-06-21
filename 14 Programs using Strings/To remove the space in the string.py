# to remove the space in the string

string= 'k a bile sh'
temp=''
for i in range (len(string)):
    if (string[i]==' '):
        pass
    else:
        temp= temp+string[i]
print(temp)
