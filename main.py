from my_data import vegetables,fruits,instruments
import random

words_list = vegetables+fruits+instruments
hangman_word = words_list[random.randint(0,len(words_list)-1)]
hangman_word_secret = '-'*len(hangman_word)
hangman_word_secret_list = list(hangman_word_secret)

if hangman_word in vegetables:
    categorie = "vegetables"
elif hangman_word in fruits:
    categorie = "fruits"
elif hangman_word in instruments:
    categorie = "instruments"
print(f'Guess the word ! HINT: The word is a {categorie}')
hangman_word_upper = hangman_word.upper()
print(hangman_word)
print(hangman_word_secret)

while hangman_word_secret != hangman_word:
    user_guess = input("Enter a letter to guess: ")
    user_guess = user_guess.upper()
    if user_guess in hangman_word_upper:
        for i in range(0,len(hangman_word)):
            if  user_guess == hangman_word_upper[i] :
                hangman_word_secret_list[i] = hangman_word[i]
                hangman_word_secret = ''.join(hangman_word_secret_list)
    else:
        print("letter not in the word")
    print(hangman_word_secret)

print('Congratulations, You won!')
