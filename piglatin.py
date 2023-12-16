#thabang sambo
#28 march 2019


def to_pig_latin(sentence):
    i = 0
    while i < (len(sentence)-1): #length of sentence changes!!! use while
        if sentence[i] in {'a','e','i','o','u'} and (i == 0 or sentence[i-1] ==' '):
            while sentence[i] != ' ' and i < (len(sentence)-1):
                i +=1
            if i == len(sentence) -1:
                sentence = sentence[:i+1] + 'way' + sentence[i+2:]
            else:
                sentence = sentence[:i] + 'way ' + sentence[i+1:]
        elif sentence[i] not in {'a','e','i','o','u'} and (i == 0 or sentence[i-1] ==' '):
            x =''
            while (sentence[i] != ' ' and sentence[i] not in {'a','e','i','o','u'}) and i < (len(sentence)-1):
                x += sentence[i]
                sentence = sentence = sentence[:i] + '' + sentence[i+1:]
            while sentence[i] != ' '  and i < (len(sentence)-1):
                i += 1
            if i == len(sentence) -1:
                sentence = sentence[:i+1] + 'a' + x + 'ay' + sentence[i+2:]
            else:
                sentence = sentence[:i] + 'a' + x + 'ay '+ sentence[i+1:]
        i +=1#length of sentence changes!!!!
    return sentence

def to_english(s):
    s = s.split(" ")
    english = ""
    for word in s:
            
            if word[:len(word) - 4:-1] == 'yaw':
                    english += word[:len(word) - 3] + " "
                
            else:
                    index = -3
                    # count consonent between two last a
                    for letter in reversed(word[:-3]):
                            if letter is not 'a':
                                    index-=1
                            else:
                                    break
                                    
                            
                    english +=  word[index:-2] + word[:index-1] + " "               
        
    return english     
    
     