#!/usr/bin/env python
# coding: utf-8

# In[1]:


def display_board(board):
    clear_output() 
    
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]} ') 


# In[2]:


def choose_marker():
    
    x_or_o = 0
   
    while x_or_o not in ['X', 'O']:
        
        x_or_o = input('Player 1: Would you like to be X or O?  ').upper()
    
        
        if x_or_o not in ['X', 'O']:
            print('Invalid Input')
        
            
        if x_or_o == 'X':
        
            players = ('X','O')
   
        else:
        
            players = ('O','X')
    
    print(f'\n\nPlayer 1 will be {players[0]}')
    print(f'\nPlayer 2 will be {players[1]}')
    
    return players
    


# In[3]:



def player_turn(number):
    
    
    acceptable_value = False
   
    turn = ''
    
    while turn.isdigit() == False or acceptable_value == False or not empty_check(board, position):
        turn = input(f'\nPlayer {number} Choose a position (1-9): ')
        
        if turn.isdigit() == False:
            print("I said a number, it shouldn't be this hard")
       
        if turn.isdigit():
            if int(turn) in range(1,10):
                acceptable_value = True
            else:
                print('I said 1-9 dummy')
    
        
             
        position = int(turn)-1
        return position
       
    


# In[4]:


def player_marker(board, marker, position):
    
    board[position] = marker
    


# In[5]:


def empty_check(board, position):
    return board[position] == ' '


# In[6]:


def winner(board):
            global wincheck
            wincheck = 0
    
            if 'X' == board[0] == board[3] == board[6] or 'O' == board[0] == board[3] == board[6]:
                print('Congratulations! You Won')
                wincheck = True
        
            elif 'X' == board[1] == board[4] == board[7] or 'O' == board[1] == board[4] == board[7]:
                print('Congratulations! You Won')
                wincheck = True
            
            elif 'X' == board[2] == board[5] == board[8] or 'O' == board[2] == board[5] == board[8]:
                print('Congratulations! You Won')
                wincheck = True
                
            elif 'X' == board[0] == board[1] == board[2] or 'O' == board[0] == board[1] == board[2]:
                print('Congratulations! You Won')
                wincheck = True
                
            elif 'X' == board[3] == board[4] == board[5] or  'O' == board[3] == board[4] == board[5]:
                print('Congratulations! You Won')
                wincheck = True
                
            elif 'X' == board[6] == board[7] == board[8] or 'O' == board[6] == board[7] == board[8]:
                print('Congratulations! You Won')
                wincheck = True
                
            elif 'X' == board[0] == board[4] == board[8] or 'O' == board[0] == board[4] == board[8]:
                print('Congratulations! You Won')
                wincheck = True
                
            elif 'X' == board[2] == board[4] == board[6] or 'O' == board[2] == board[4] == board[6]:
                print('Congratulations! You Won')
                wincheck = True
                
            return wincheck
            



# In[7]:


def choose_first():
    
    first = random.randint(1,2)
    
    print(f'Player {first} will go first')
    print("\nLet's Play!")
    
    if first == 1:
        return 'Player1'
        
    else:
        return 'Player2'
        


# In[8]:


def playagain():
    return input('\n\nWould you like to play agian? (yes or no)   ').lower().startswith('y')
    


# In[9]:


####Game#####

from IPython.display import clear_output
import random

##setup##
while True:
    
    
    play_on = True
    
    #reset board
    
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    #show numberpad 
    display_board(['1','2','3','4','5','6','7','8','9'])
      
    #player1 choses x or o
    markplayer1, markplayer2 = choose_marker()
    
    #chose first turn
    turn = choose_first()
    
    
    
#gameplay
    while play_on:
        
        #first player turn
        
        if turn == 'Player1':
                
            position = player_turn(1)
            player_marker(board, markplayer1, position)
            display_board(board)
            
            #check for winners or ties
            winner(board)
            if wincheck:
                play_on = False

                break
            
            elif ' ' not in board:
                print('Tie Game')
                play_on = False
                break
                
            turn = 'Player2'
         
        #second player turn
        
        else:
                
            position = player_turn(2)
            player_marker(board, markplayer2, position)
            display_board(board)
                
            winner(board)
            if wincheck:
                play_on = False
                break
            
            elif ' ' not in board:
                print('Tie Game')
                play_on = False
                break
                
            turn = 'Player1'
                
    #ask if you need to play again and rerun from the beginning            
    
    if playagain():
        play_on = True
    else:
        play_on = False
        print('\nThank you for Playing')
        break
            

