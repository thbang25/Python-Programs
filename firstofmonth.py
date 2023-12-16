#thabang sambo
#22 march 2019

month = input("Enter the month: ")
b = eval(input("Enter the year: " ))

if month in ["March"]:
    m=1
elif month in ["April"]:
    m=2
elif month in ["May"]:
    m=3
elif month in ["June"]:
    m=4    
elif month in ["July"]:
    m=5
elif month in ["August"]:
    m=6
elif month in ["September"]:
    m=7
elif month in ["October"]:
    m=8
elif month in ["November"]:
    m=9
elif month in ["December"]:
    m=10
elif month in ["January"]:
    m=11
elif month in ["February"]:
    m=12
else:
    print()

if month in ["January"]:
    x=6
    if b==1900:
        x=0
        
elif month in [ "July"]:
    x=1
elif month in ["March"]:
    x=1
elif month in ["February"]:
    x =1
    if b==2000:
        x=0
elif month in ["August"]:
    x=1
elif month in ["October"]:
    x=1
elif month in ["December"]:
    x=1
elif month in ["November"]:
    x=2
elif month in ["April"]:
    x=1
elif month in ["June"]:
    x=1
elif month in ["May"]:
    x=1
elif month in ["September"]:
    x=2




w = round((x + (2.6*m-0.2) + b + (b/4) + (21/4) ) %7)
if w == 1:
    print("The 1st of",month,b,"is a Monday.")
if w == 2:
    print("The 1st of",month,b,"is a Tuesday.")
if w == 3:
    print("The 1st of",month,b,"is a Wednesday.")
if w == 4:
    print("The 1st of",month,b,"is a Thursday.")
if w == 5:
    print("The 1st of",month,b,"is a Friday.")
if w == 6:
    print('The 1st of',month,b,'is a Saturday.')
if w == 0:
    print('The 1st of',month,b,'is a Sunday.')



