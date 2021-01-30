# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:30:30 2020

@author: sierr
"""

my_string = 'Python'

len(my_string)
my_string[0]
my_string[1]
my_string[0:4]
my_string[:4]
my_string[-1]
letter = my_string[4]

my_string.upper()
my_string.lower()

#Guess the word

word = 'summer'

guess = input('I\'m thinking of a word, can you guess\
 what it is? hint it\'s a season. \n >>>> ')

guess = guess.lower()

if guess == 'summer':
    print('Yes, it\'s Summer, Well done!')
elif guess == 'winter':
    print('No it\'s not winter. Sorry!')
elif guess == 'autumn':
    print('No it\'s not autumn. Sorry!')
elif guess == 'spring':
    print('No it\'s not spring. Sorry!')
else:
    print(guess.capitalize(),' is not a season!')