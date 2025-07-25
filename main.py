from my_data import fruits,vegetables, instruments
import random

categories = [vegetables,fruits,instruments]
categorie_index = random.randint(0,len(categories)-1)
element_index = random.randint(0,len(vegetables)-1)
print(f'categories[{categorie_index}][{element_index}]')

print(categories[categorie_index][element_index])


