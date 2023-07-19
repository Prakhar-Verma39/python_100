import random

rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ '''

paper = ''' 
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|'''
scissors =''' 
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/ '''



I_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if I_choice == 0:
    print(rock)
elif I_choice == 1:
    print(paper)
else:
    print(scissors)
C_choice = random.randint(0,2)

if C_choice == 0:
    print(rock)
elif C_choice == 1:
    print(paper)
else:
    print(scissors)
print("Computer chose:")
if (I_choice == 0 and C_choice == 1) or (I_choice == 1 and C_choice == 2) or (I_choice == 2 and C_choice == 0):
    print("You lose")
elif (I_choice == 0 and C_choice == 2) or (I_choice == 1 and C_choice == 0) or (I_choice == 2 and C_choice == 1):
    print("You win")
else:
    print("Draw")