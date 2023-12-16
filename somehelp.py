#thabang sambo
#09 april 2019
#somehelp technical support

import random

def intro():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem:')

def enter_input():
    return input().lower()


def main():

    feedback = ['Have you tried it on a different operating system?','Did you reboot it?','What colour is it?','You should consider installing anti-virus software.','Contact Telkom.','I should get that looked at if I were you.']

    
    intro()    
    complaint = enter_input()
    
    while ( complaint!='quit'):
        print(feedback[random.randint(0,5)])

        complaint = enter_input()    
    
if __name__=='__main__':
    main()   

