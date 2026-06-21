# to find the given string is anagrams or not

a= str(input('enter a string:'))
b= str(input('enter a string:'))

if len(a) != len(b):
    print('not a anagram')
else:
    count=0
    for i in range (len(a)):
       for j in range (len(b)):
          if a[i]==b[j]:
              count= count+1
              break
    if count== (len(a)):
        print('the given strings are anagrams')
    else:
        print('not an anagrams')

a= str(input('enter a string:'))
b= str(input('enter a string:'))

if len(a) != len(b):
    print('not a anagram')
else:
    count=0
    for i in range (len(a)):
       for j in range (len(b)):
          if a[i]==b[j]:
              count= count+1
              break
    if count== (len(a)):
        print('the given strings are anagrams')
    else:
        print('not an anagrams')
