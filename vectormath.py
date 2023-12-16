#thabang sambo
#09 april 2019
#vector addition,substraction and normalisation in 3D

import math

A = input("Enter vector A:\n") 
B = input("Enter vector B:\n")
A = A.split()
B = B.split()
Addition = []*len(A)
Dot = []*len(A)
SquareSumA = 0
SquareSumB = 0
NormA = 0
NormB = 0 
DotSum = 0
for i in range(0,len(A)):
    Addition.append(eval(A[i]) + eval(B[i]))
    Dot.append(eval(A[i]) * eval(B[i]))
    DotSum += (eval(A[i]) * eval(B[i]))
    SquareSumA += eval(A[i])**2
    SquareSumB += eval(B[i])**2
NormA = math.sqrt(SquareSumA)
NormB = math.sqrt(SquareSumB)
print("A+B = " + str(Addition))
print("A.B = " + str(DotSum))
print("|A| = " + str("{:.2f}".format(NormA)))
print("|B| = " + str("{:.2f}".format(NormB)))