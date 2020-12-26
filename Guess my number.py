#!/usr/bin/env python
# coding: utf-8

# 

# In[2]:




from random import randint


number = randint(1,51)

all_guess = [0]

print("LET'S PLAY GUESS MY NUMBER!")
while True:
    
    guess = input('\nGuess a number between 1 and 50: ')
    if guess.isdigit():
        guess = int(guess)
        if guess>50:
            print('OUT OF BOUNDS, please type a valid number')
            continue
        else:
            pass
        
    else:
        print('OUT OF BOUNDS, please type a valid number')
        continue
        
    if guess == number:
        print(f'YOU GUESSED IT WITH {len(all_guess)} TRIES')
        break
    
    all_guess.append(guess)
       
    if all_guess[-2]:
        
        if abs(number - guess)< abs(number - all_guess[-2]):
            print('WARMER')          
        else:
            print('COLDER')
    else:
        if abs(all_guess[-2]-number) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    


# 

# In[ ]:




