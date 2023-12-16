n = eval(input("Enter the start number: "))
         
if -6<n<93:
    for i in range(n,n+7):
        a=i
        print("{0:2}".format(a),end =' ')
else:
    print()