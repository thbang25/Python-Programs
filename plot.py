#thabang sambo
#3 april 2019
#plotting a function f(x)


import math 
function = input("Enter a function f(x):\n")
for y in range(10,-11,-1):
  for x in range(-10,11):
    if y == round(eval(function)):
        print("*", sep="", end= "")    
    elif y == 0 and x != 0:
      print("-", sep="", end= "")
    elif y == 0 and x == 0:
      print("+", sep="", end= "")
    elif y!= 0 and x == 0:
        print("|", sep="", end= "")
    else:
      print(" ", sep="", end= "")
  print("\n",end="")