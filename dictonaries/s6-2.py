# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 08:32:00 2020

@author: sierr
"""

"""
Question 1 can you remember how to check if a key exist 
in a dictionary? using the capitals dictionary below 
write some code to ask the user to input 
a country, them check if that country is in the dictionary 
and if it is print the capital, if not tell the user it's not there 
""" 


capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
            'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
            'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
            'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
            }
""""
student
"""
key = input('Please insert a country, make sure the fisrt letter is capitalize\n>>>')

if key in capitals:
    print(f'The capital of {key} is ',capitals.get(key))
else:
    print('We dont have that information')


## profesor 

#user_input = input('Which country would you like to check?:> ')
#
#user_input = user_input.lower()
#
#while ('united kingdom' not in user_input and not user_input.isalpha()):
#    if user_input == 'united states':
#        break
#    print('You must input a string')
#    user_input = input('Which country would you like to check?:> ')
#
#user_input = user_input.title()
##print(user_input)
#if user_input in capitals:
#    print(f'The capital of {user_input} is {capitals[user_input]}')
#else:
#    print('No data available') 



"""
Question 2 

Write python code that will create a disctionary containing key, value pairs 
that represent the fisrt values of the fibonacci 
sequence 

"""

n = 12
a = 0 
b = 1
d = dict()
for i in range(1,n+1):
    d[i] = a
    a,b = b,a+b
print(d)  


























