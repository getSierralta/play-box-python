# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:58:30 2020

@author: sierr
"""

#list -> ordered 
#Dictionaries -> not ordered 
#Dictonaries are really fast
#Key-value pairs 

capitals = {'France':'Paris','Spain':'Madrid'}

capitals['France']
capitals.get('Spain')

capitals['Venezuela'] = 'Caracas'

print(capitals)

print(capitals.items())

for country, city in capitals.items():
    print(f'The capital of {country}, is {city}')
    

print()

print(capitals.keys())

print()
print(capitals.values())

if 'France' in capitals:
    print('It contains france')