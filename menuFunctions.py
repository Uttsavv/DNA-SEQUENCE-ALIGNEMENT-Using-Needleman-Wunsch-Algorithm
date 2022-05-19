import os

def seqSelectMenu():
    print('\n Please select sequences from the following choices :-\n')
    i=1
    for filename in os.listdir("sequences"):
        seqName = filename.split('.')[0]
        print(f' {i}.{seqName}')
        i+=1

    firstSeqNumber= int(input('\n Please enter the first sequence number :'))
    secondSeqNumber= int(input('\n Please enter the second sequence number :'))

    return firstSeqNumber,secondSeqNumber

def mainMenu():
    option = -1
    while(option !=2):
        print('\n Welcome to the Sequence Alignment Tool')
        print('\n 1.Select sequences for Alignment.')
        print(' 2.Close.\n\n')
        
        # Taking the input from user and checking if it is a valid input
        option = input(' Please select your option: ')
        while(True):
            if(option.isnumeric()):
                option = int(option)
                break
            else :
                option = input(" Please Enter a valid input number :")
        
        if(option == 1):
            return seqSelectMenu()
            

        elif(option == 2):
            os.system('cls')
            quit()