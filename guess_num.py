''' • The program randomly selects a number between 1 and 100.
    • The user tries to guess the number.
    • The game gives hints if the guess is too high, too low, or close to the correct number.
    • The game continues until the user guesses the correct number.'''

import random
def guess():
    guess=random.randint(1,100)
    return guess
num=guess()
    
while True:
    is_ready=input('Hy there Are you ready to guess the number?(y/n) ')
    if is_ready.lower()=='y':
        while True:
            user_guess=int(input('Guess the Number : '))
            if user_guess==num:
                print(f'Hurrey!!The number is {num}  You guessed it correct ! well Done')
                exit()
            elif user_guess in range(num-10,num):
                print("You are almost there the number is larger then this")
            elif user_guess in range(num+1,num+11):
                print("You are almost there the number is less than this")
            elif user_guess<num:
                print(f"oh noo! you went too far ,The number is greater than this")
            elif user_guess>num:
                    print(f" oh hoo! You went too far ,The number is less than this") 
    elif is_ready.lower()=='n':
         print('You are not ready?? Please be ready .This game is fun')
    
    else:
         print("It's and invalid option please choose between(y/n)")
        
    


