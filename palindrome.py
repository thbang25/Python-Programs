#thabang sambo
#17 april 2019
#recursion


def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return False
    
    
s=str(input("Enter a string:\n"))

if(palindrome(s)==True):
    print("Palindrome!")
else:
    print("Not a palindrome!")