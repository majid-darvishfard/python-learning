import os
from random import seed,randint

gold_value=randint(1,101)
max_input_count=6
count=1

while True:
    print("")
    input_value=int(input('Guess a number between {} to {} [remmaning chance {}/{}]: '.format('1','100',count,max_input_count)))
    print()
    count +=1
    if count > max_input_count:
        print("You Lose !! My number was {}".format(gold_value))
        playagain=input('Do you want play again? [y/n]')
        if playagain == 'y' or playagain == 'Y':
            os.system('cls') if os.name=='nt' else os.system('clear')
            gold_value=randint(1,101)
            count=1
            continue
        else:
            break

    
    if input_value > gold_value:
        print("---> My number is lower than {} ".format(input_value))
    elif input_value < gold_value:
        print("---> My number is bigger than {} ".format(input_value))
    else:
        print(" You Win.")
        playagain=input('Do you want play again? [y/n]')
        if playagain == 'y' or playagain == 'Y':
            os.system('cls') if os.name=='nt' else os.system('clear')
            gold_value=randint(1,101)
            count=1
        else:
            break

