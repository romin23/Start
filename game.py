import csv
    
import gfunc


with open('test.csv','r') as f:
    reader = csv.reader(f)     
    fruit_list = list(reader)
    fruit_list = fruit_list[0]

    word = gfunc.chose_rand_word(fruit_list)
    word_lst = [letter for letter in word]

    with open('Hints.csv','r') as h:
        read = csv.reader(h)
        hint_list = list(read)

        gfunc.display_hint(hint_list, fruit_list.index(word))

    while True:
        no_of_attempt = input('Enter no. of attempts you want,(3 to 20): ')

        try:
            no_of_attempt = int(no_of_attempt)

            if no_of_attempt<3:
                raise gfunc.ValueSmall
            
            if no_of_attempt>25:
                raise gfunc.ValueLarge
            break
            
            
        except gfunc.ValueLarge:
            print('Enetr The Value Less Than 25')
            continue


        except  gfunc.ValueSmall:
            print('Enetr The Value Greater Than 3')
            continue

        except:
            print('Please Enter a Integer')
            continue


    gfunc.check(word_lst,no_of_attempt,word)


