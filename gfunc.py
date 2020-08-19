import random

class Error(Exception):
    pass

class ValueLarge(Error):
    pass

class ValueSmall(Error):
    pass

def chose_rand_word(fruit_list):
    num = random.randint(0,len(fruit_list)-1)
    word = fruit_list[num]
    return word.lower()

def display_hint(hint_list,word_index):
    print(hint_list[word_index][0])
   

def check(word_lst,no_of_attempt,word):
    word_strs = '*'*len(word_lst)
    wrd_strs_lst = [strs for strs in word_strs]
    orig_word_list = [x for x in word_lst]
       
    while no_of_attempt > 0:
        print(word_lst)
        print('Your word: ',end='')
        for i in wrd_strs_lst: print(i,end='')
        print(f'\nYou have {no_of_attempt} wrong Guesses left')
        guess = input('Guess a letter from secret word: ')
        guess = guess.lower()
        
        if (guess in word_lst):
            print('Correct Guess!!\n\n\n')
            while True:
                if guess in word_lst:
                    wrd_strs_lst[word_lst.index(guess)] = guess
                    word_lst[word_lst.index(guess)] = '*'
                    continue
                break
            
        else:
            print('Incorrect Guess\n\n\n')
            no_of_attempt -= 1 
            
        if not '*' in wrd_strs_lst:
            print('You Won!!!!!')
            break
    else:
        print('This was your last WRONG Attempt\nYOU LOST\nBETTER LUCK NEXT TIME')


