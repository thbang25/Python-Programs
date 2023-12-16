#thabang sambo
#22 march 2019
a = eval(input("Enter the minimum number of inches (not less than 0):\n"))
b = eval(input('Enter the maximum number of inches (not greater than 11):\n'))
print('Inches:',end = ' ')
if ( a>0 and a<=11) and (b>0 and b<=11):
    for i in range(a,b+1):
        print("{0:4}".format(i),end =' ')
    else:
            print()

print('Metres:',end=' ')
for i in range(a,b+1):
    a= i*0.0254
    b= (round(a,2))
    print("{0:3.2f}".format(b),end=' ')
   
    
        

         
    
            
            
             

           
            
            
        
        
        
    
        
        
        
         
         
    