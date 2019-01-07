
from random import randrange,randint
import os

words=('banana','student','teacher','python','canon','watch')



random_index=randint(0,len(words)-1)
selected_word=words[random_index]

current_life=0
max_life=6
input_list=[]
guess_word='_'*len(selected_word)


def again():
    random_index=randint(0,len(words)-1)
    selected_word=words[random_index]
    print(selected_word)
    current_life=0
    input_list=[]
    guess_word='_'*len(selected_word)
 

while True:
    os.system('cls') if os.name=='nt' else os.system('clear') 
    print('Strikes:  {}/{}'.format(current_life, max_life))
    print()
    print()
    print(' '.join(input_list))
    print(guess_word)
    input_letter=input('Guess a letter: ')
    if input_letter in selected_word:
        for i in range(len(selected_word)):
            if (selected_word[i] == input_letter):
                list_guess_word=list(guess_word)
                list_guess_word[i]=selected_word[i]
                guess_word=''.join(list_guess_word) 
        if '_' not in guess_word:
            print('You Win.')
            
            playagain=input('Do you want play again? [Y/N] ')
            if playagain == 'y':
                again()
        #        #os.system('cls') if os.name=='nt' else os.system('clear')
        #        random_index=randint(0,len(words)-1)
        #        selected_word=words[random_index]
        #        print(selected_word)
        #        current_life=0
        #        input_list=[]
     #        guess_word='_'*len(selected_word)
                continue
            else:
                break
    else:
        current_life +=1
        input_list.append(input_letter)


    if current_life > max_life:
        print('you lose!!')
        break

 







