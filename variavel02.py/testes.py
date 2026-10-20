import os
os.system("cls")

v=int(input())
a=int(input())
f=int(input())
p=int(input())

if (a+f+p <=v):
    print('paga 3')
elif (a+f<=v) or (f+p<=v) or (a+p<v):
    print('2')
elif (a<=v) or (p<=v) or (f <=v):
    print('1')
else:
    print('0')
    
    
    
    
    
 
