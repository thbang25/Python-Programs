a = eval(input('Enter the start point N:\n'))
b = eval(input('Enter the end point M:\n'))
print('The palindromic primes are:')
for n in range(a+1, b):
 if str(n) == str(n)[::-1] and (2**n-1)%n == 1:
  print(n)
  