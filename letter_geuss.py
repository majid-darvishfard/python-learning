
from random import randrange,randint,choice
import os

words={'banana':'is an fruit',
        'perspolis':'iranian Footbal team',
        'python':'is programming Language',
        'purple':"it's color",
        'Pakistan':' is a country in South Asia',
        'tiger':' is the largest cat species',
        'amazon':' is a multinational technology company focusing in e-commerce'}

selected_word=choice(list(words))
current_life=0
max_life=5
input_list = []
guess_word = '-'*len(selected_word)
 
def select_new_word():
    selected_word=choice(list(words))
    return selected_word

def reset_couner():
    current_life=0
    input_list = []
    return current_life,input_list

def clear():
    os.system('cls') if os.name=='nt' else os.system('clear') 

while True:
    clear()
    print('Strikes:  {}/{}'.format(current_life, max_life))
    print()
    print('Word Description: {}'.format(words[selected_word]))
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
                selected_word=select_new_word()
                guess_word = '-'*len(selected_word)
                current_life,input_list = reset_couner()

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
            selected_word=select_new_word()
            guess_word = '-'*len(selected_word)
            current_life,input_list = reset_couner()
        else:
            break        

