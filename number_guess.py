import os
from random import seed,randint

gold_value=randint(1,101)
max_input_count=6
count=1

def again():
    os.system('cls') if os.name=='nt' else os.system('clear')
    global gold_value
    global count
    gold_value=randint(1,101)
    count=1

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
    count +=1
    if count > max_input_count:
        print("You Lose !! My number was {}".format(gold_value))
        playagain=input('Do you want play again? [y/n]').lower()
        if playagain == 'y':
            again()
            continue
        else:
            break

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
            again()
        else:
            break
