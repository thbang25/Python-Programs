#thabang sambo
#09 april 2019
#techsupport services


import random

def intro():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem:')

def enter_input():
    return input().lower()


def main():

    feedback = {'crashed':'Are the drivers up to date?','blue': 'Ah, the blue screen of death. And then what happened?','hacked': 'You should consider installing anti-virus software.','bluetooth':'Have you tried mouthwash?','windows': 'Ah, I think I see your problem. What version?','apple':'You do mean the computer kind?', 'spam':'You should see if your mail client can filter messages.','connection':'Contact Telkom.'}
    
    intro()    
    complaint = enter_input()
    Keywords = {'crashed','blue','hacked','bluetooth','windows','apple','spam','connection'}
    
    while (complaint !='quit'):
        QueryWords = complaint.split()
        for i in range(0,(len(QueryWords))):
            if QueryWords[i] in Keywords:
                print(feedback[QueryWords[i]])
                break
            elif i == (len(QueryWords)-1):
                print('Curious, tell me more.')  
                
     
        complaint = enter_input()    
    
if __name__=='__main__':
    main()   