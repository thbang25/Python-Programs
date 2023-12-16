#thabang sambo
#17 april 2019
#recursion

def match(pattern, word):    
    if (len(pattern)==len(word)) and (pattern[:1]==word[:1]) and (pattern[(len(pattern)-2):]== word[(len(word)-2):]):
        return True
    if (len(pattern)==len(word)) and (pattern[:1]==word[:1]) and (pattern[(len(pattern)-1):]== word[(len(word)-1):]):
        return True
    if (pattern == '?' and word[1:] == ''):
        return True
    if (len(pattern)==len(word)) and (pattern[:2]==word[:2]) and (pattern[(len(pattern)-1):]== '?'):
        return True
    if pattern == word:
        return True
    if (pattern[:1]=='?') and  (pattern[(len(pattern)-2):]== word[(len(word)-2):]) and (len(pattern)==len(word)):
        return True
    if (pattern[(len(pattern)-2):]=='???') and (len(pattern)==len(word)):
        return True
    if (pattern.count('?')==5) and (pattern[(len(pattern)-3):]=='???') and (len(pattern)==len(word)) and (pattern[:1]==word[:1]):
        return True
    else:
        return False
    
    
  