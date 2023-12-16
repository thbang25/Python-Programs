# solving the area of a triangle
# 26 february 2019
# thabang sambo

a = eval(input("Enter the length of the first side: "))
b = eval(input("Enter the length of the second side: "))
c = eval(input("Enter the length of the third side: "))
s = (a+b+c)/2 
Area = (s*(s-a)*(s-b)*(s-c))
area = Area**0.5

print("The area of the triangle with sides of length" ,a, 'and', b, 'and' ,c ,'is', area, end = '')
print(".")
