print('program to print the grades of the subjects using elif statements')
print('------------------------------------------------------------------')
subjects=['tamil','english','maths','science','social']
tamil=int(input('enter tamil mark:'))
english=int(input('enter english mark:'))
maths=int(input('enter maths mark:'))
science=int(input('enter science mark:'))
social=int(input('enter social mark:'))
mark=[tamil,english,maths,science,social]

for i in range(5):
    if mark[i]>= 91 and mark[i]<= 100:   
        print(subjects[i],'grade is','S')
    elif mark[i]>= 81 and mark[i]<= 90:  
        print(subjects[i],'grade is','A')
    elif mark[i]>= 71 and mark[i]<= 80:
        print(subjects[i],'grade is','B')
    elif mark[i]>= 61 and mark[i]<= 70:
        print(subjects[i],'grade is','C')
    elif mark[i]>= 51 and mark[i]<= 60:
        print(subjects[i],'grade is','D')
    elif mark[i] == 50:
        print(subjects[i],'grade is','E')
    elif mark[i]>= 0 and mark[i]<= 49:
        print(subjects[i],'fail')
    else:
        print('enter the correct number')
              
        
    
 
        

