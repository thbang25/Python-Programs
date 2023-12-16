# Thabang sambo
# 4 may 2019
# files
# anagrams
file1='EnglishWords.txt'        
def start(file):
    for line in file:
        line=line.rstrip('\n')
        if line=='START':
            return
        
def retrieve_words(wordlen, file):    
    sets=[]
    for line in file:
        word=line.rstrip('\n')
        if len(word)==wordlen:
            sets.append(word)
    return sets

def dect(word):
    dic = {}
    for letter in word:
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] = 1
    return dic

def check(word_one, word_two):
    return dect(word_one)==dect(word_two)

def delete(word, words):
    sets=[]
    index=0
    while index<len(words):
        if check(word, words[index]):
            sets.append(words[index])
            words.pop(index)
        else:
            index+=1
    return sets
        
def search(wordlen, file):
    words = retrieve_words(wordlen, file)
    
    sets=[]
    print('Searching...')   
    while not words==[]:
        word = words.pop(0)
        anagrams = delete(word, words)
        if not anagrams==[]:
            anagrams.append(word)
            anagrams.sort()
            sets.append(anagrams)
    return sets


def main():
    file=open(file1, 'r')
    start(file)
    
    wordlen = int(input('Enter word length:\n'))
    sets = search(wordlen, file)
    file.close()
    sets.sort()
    file=open(input('Enter file name:\n'), 'w')
    for set1 in sets:
        file.write(str(set1))
        file.write('\n')
    file.close()


if __name__=='__main__':
    main()