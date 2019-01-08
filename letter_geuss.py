
from random import randrange,randint
import os

words=('banana','student','teacher','python','orange','Lemon')



random_index=randint(0,len(words)-1)
selected_word=words[random_index]

current_life=0
max_life=5
input_list = []
guess_word = '-'*len(selected_word)

 
def again():
    global selected_word
    global current_life
    global input_list
    global guess_word
    random_index=randint(0,len(words)-1)
    selected_word=words[random_index]
    current_life=0
    input_list = []
    guess_word = '-'*len(selected_word)

while True:
    os.system('cls') if os.name=='nt' else os.system('clear') 
    print('Strikes:  {}/{}'.format(current_life, max_life))
    print()
    print()
    print(' '.join(input_list))
    print()
    print(guess_word)
    print()
    input_letter=input('Guess a letter: ').lower()
    if input_letter in selected_word:
        for i in range(len(selected_word)):
            if (selected_word[i] == input_letter):
                list_guess_word=list(guess_word)
                list_guess_word[i]=selected_word[i]
                guess_word=''.join(list_guess_word)
                print(guess_word) 
        if '-' not in guess_word:
            print('***************************')
            print('         You Win.')
            print('***************************')
            playagain=input('Do you want play again? [Y/N] ').lower()
            if playagain == 'y':
                again()
            else:
                break
    else:
        current_life +=1
        input_list.append(input_letter)


    if current_life > max_life:
        print('***************************')
        print('         you lose!!')
        print('***************************')
        playagain=input('Do you want play again? [Y/N] ').lower()
        if playagain == 'y':
            again()
        else:
            break        

 







