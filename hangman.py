import random 

import hangman_words, hangman_art

print("Welcome to hangman game!!\n", hangman_art.logo)

word = hangman_words.word_list[random.randint(0,len(hangman_words.word_list)-1)]

print("_ "*len(word))

ch = []

for l in range(0,len(word)):
    ch.append("_ ")

not_hanged = 6

while not_hanged:
    guess = input("Guess a letter! ").lower()

    if guess in word:
        for i, l in enumerate(word):
            if l == guess:
                ch[i] = guess +" "
    else:
        print(hangman_art.stages[not_hanged])
        not_hanged -= 1
    
    print(''.join(ch))
    if ''.join(ch) == word:
        print('You Win.')
        break
if not_hanged == 0:
    print(hangman_art.stages[not_hanged] + "\nYou lose.")