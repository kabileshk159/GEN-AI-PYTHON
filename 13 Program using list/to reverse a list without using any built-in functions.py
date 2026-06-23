# to reverse a list without using any built-in functions
b=[2,3,4,5,6,7,8,77]
rev_list=[]
for i in range (len(b),0,-1):
    rev_list.append(b[i-1])
print(rev_list)
