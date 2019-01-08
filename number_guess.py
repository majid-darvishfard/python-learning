import os
from random import seed,randint

gold_value=randint(1,100)
max_input_count=7
count=1

def clear():
    os.system('cls') if os.name=='nt' else os.system('clear')


while True:
    print("")
    input_value=input('Guess a number between {} to {} [remmaning chance {}/{}]: '.format('1','100',count,max_input_count))
    if not input_value.isdecimal():
        print()
        print("Please Enter Number Only.")
        continue
    else:
        input_value=int(input_value)    
    print()
    
    if count >= max_input_count:
        print("You Lose !! My number was {}".format(gold_value))
        playagain=input('Do you want play again? [y/n]').lower()
        if playagain == 'y':
            clear()
            gold_value=randint(1,100)
            count=1
            continue
        else:
            break
    count +=1
    if input_value > gold_value:
        print("---> My number is lower than {} ".format(input_value))
    elif input_value < gold_value:
        print("---> My number is bigger than {} ".format(input_value))
    else:
        print("----------------------")
        print("       You Win.")
        print("----------------------")
        playagain=input('Do you want play again? [y/n]').lower()
        if playagain == 'y' :
            clear()
            gold_value=randint(1,101)
            count=1
        else:
            break
