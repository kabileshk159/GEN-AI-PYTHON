
# to sort the strings in the list in alphabetical order

strings=['Python','C','Java','AI','ML']

for i in range (len(strings)):
    for j in range(i+1,(len(strings))):
        if strings[i]>strings[j]:
            temp=strings[i]
            strings[i]= strings[j]
            strings[j]= temp

print(strings)
