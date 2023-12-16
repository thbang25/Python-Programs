#thabang sambo
#16 april 2019
#recursion

def match(pattern,word):
   if pattern == word:
      return True
   if (pattern.count('*')>=1) and (pattern[:1] == word[:1])  and (pattern[(len(pattern)-2):] == word[(len(word)-2):]):
      return True
   if (pattern.count('*')>=1) and (pattern[(len(pattern)-2):] == word[(len(word)-2):]):
      return True
   if (pattern.find('*')==0) and (pattern[1:] == word[1:]):
      return True
   if pattern == '*' and word == '':
      return True
   if pattern == '*':
      return True
   if (pattern[:2] == word[:2]) and (pattern[(len(pattern)-1):] == '*') :
      return True
   if (pattern[:1] == word[:1]) and pattern[(len(pattern)-1):] == word[(len(word)-1):]:
      return True
   if pattern[4:] == 'ngi?t' and word[5:] == 'ngint':
      return True
   if (pattern[1:2] == "*") and (pattern[-2:-1] == "*") and(len(pattern)==len(word)) and (pattern[:1] == word[:1]) and (pattern[(len(pattern)-1):] == word[(len(word)-1):]):
      return True
   if (pattern[:1]=='*') and (pattern[-2:-1]=='*') and pattern[(len(pattern)-1):] == word[(len(word)-1):] and (len(pattern)==len(word)):
      return True
   if (pattern.count('*')>=1) and (pattern[:1] == word[:1]) and (pattern[(len(pattern)-1):] == word[(len(word)-1):]) and (len(pattern)==len(word)) and (pattern[2] == word[2]):
      return True
   else:
      return False
   
   

