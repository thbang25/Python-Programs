a = eval(input("Enter the first year:\n"))
b = eval(input("Enter the second year:\n"))

for i in range(a,b+1):
    num1 = (1 + 5*((i - 1)%4))
    num2 = 4*((i - 1)%100)
    num3 = 6*((i - 1)%400)
    num4 = num1 + num2 + num3
    day = num4 %7
    if day == 0:
        print('The 1st of January', i,'falls on a Sunday.')
    if day == 1:
        print('The 1st of January', i,'falls on a Monday.')
    if  day == 2:
        print('The 1st of January', i,"falls on a Tuesday.")
    if day == 3:
        print('The 1st of January', i,"falls on a Wednesday.")
    if day == 4:
        print('The 1st of January', i,'falls on a Thursday.')
    if day == 5:
        print('The 1st of January',i ,'falls on a Friday.')
    if day == 6:
        print('The 1st of January',i , 'falls on a Saturday.')
        
        
        
    
 
    
    
    
    
    
        
    


