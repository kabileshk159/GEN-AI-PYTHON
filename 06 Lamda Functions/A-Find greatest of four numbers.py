# LAMBDA FUNCTIONS TO FIND GREATEST OF FOUR NUMBERS
big= lambda a,b,c,d: a if a>b and a>c and a>d else b if b>c and b>d else c if c>d else d
big(1,3,4,5)
