#thabang sambo
#22 march 2019



a = eval(input("Enter the minimum number of feet (not less than 0):\n"))
b = eval(input('Enter the maximum number of feet (not more than 99):\n'))

if ( a>=0 and a<99) and (b>=0 and b<99):
    for i in range(a,b+1):
        meters = i*0.3048
        print("{0:4}".format(i),end='')
        print("'",end=' ')
        print("|",end='   ')
        print("{0:1.2f}".format(meters),end='')
        print("m")
        
    











         