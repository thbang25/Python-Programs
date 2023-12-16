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

def search(word, file):
    anagram=[]
    for fw in file:
        fw=fw.rstrip('\n').lower()
        if check(fw, word):
            anagram.append(fw)
    if word in anagram:
        anagram.remove(word)
        anagram.sort()
    return anagram

def main():
    print('***** Anagram Finder *****')
    try:
        file=open(file1, 'r')        
        start(file)

        word=input('Enter a word: ').lower()
        anagram=search(word, file)
        file.close()
        
        if len(anagram)==0:
            print("Sorry, anagrams of '"+word+"' could not be found.")
        else:
            print(anagram)
    except FileNotFoundError:
        print('Sorry, could not find file \'{}\'.'.format(file1))

if __name__=='__main__':
    main()