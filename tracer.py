#thabang sambo
#08 May 2019
#files
#Tracer
debugging='"""DEBUG"""'
def detecting(x):
    return len(x)>0 and x[0].startswith(debugging)    

def retrieve_name(line):
    return line.split(' ')[1].split('(')[0]
    
    
def initiate_program(file_name):
    file=open(file_name, 'r')
    x=file.readlines()
    file.close()
    return x
    
def save_program(x, file_name):
    file=open(file_name, 'w')
    for line in x:
        print(line, file=file, end='')
    file.close()

def get_indentation(x, location):
    while len(x[location].strip())==0:
        location+=1
    
    index=0
    while x[location][index].isspace():
        index+=1
    return x[location][:index]

def insertin(x):
    print('Inserting...', end='')
    x.insert(0, debugging+'\n')
    index=1
    while index<len(x):
        if x[index].startswith('def'):
            function_name=retrieve_name(x[index])
            index+=1
            indentation=get_indentation(x, index)
            x.insert(index, indentation+debugging+';print(\''+function_name+'\')'+'\n')
        index+=1
    print('Done')
        
def removing(x):
    print('Removing...', end='')
    del x[0]
    index=0
    while index<len(x):
        if debugging in x[index]:
            del x[index]
        else:
            index+=1
    print('Done')


def main():
    print('***** Program Trace Utility *****')
    file_name=input('Enter the name of the program file: ')
    x=initiate_program(file_name)
    if detecting(x):
        print('Program contains trace statements')
        removing(x)
    else:
        insertin(x)
    save_program(x, file_name)
    
main()