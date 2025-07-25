from my_data import fruits,vegetables, instruments
import random

categories = [vegetables,fruits,instruments]
def chose_secret_word():
    categorie_index = random.randint(0,len(categories)-1)
    element_index = random.randint(0,len(vegetables)-1)
    secret_word = categories[categorie_index][element_index]
    return secret_word 

hangman_word = chose_secret_word()
if hangman_word in vegetables:
    print('Guess the word! HINT: word is a vegetable')
if hangman_word in fruits:
    print('Guess the word! HINT: word is a fruits')
if hangman_word in instruments:
    print('Guess the word! HINT: word is an instruments')
print('Word to find: ', hangman_word)
hangman_word_secret = '- ' * len(hangman_word)
hangman_word_secret_list = list(hangman_word_secret)
print(hangman_word)
hangman_word.lower()
print(hangman_word_secret)

while True:
    user_character = input("Enter a letter to guess: ")
    user_character_alpha = user_character.isalpha()
    if user_character_alpha:
        user_character
        print(user_character)
    else:
        print('not letter')

print('end program')