# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:08:13 2020

@author: sierr
"""

var3,var4,var5 = 15,20,25

print('var3 = ', var3,'var4 = ',var4,' var5 = ',var5, end = '\n\n')

print('var4 and var5 < 100?: ', var4 < 100 and var5 <100)
print('var4 and var5 < 22?: ',var4 <22 and var5<22)
print('var4 or var5 <22?: ',var4 < 22 or var5<22, end = '\n\n')

print('not True is: ', not True)
print('not False is: ',not False, end = '\n\n')

print('not(var4 and var5 < 100?) ',not(var4<100 and var5<100))
print('not(var4 and var5 < 22?) ', not(var4<22 and var5<22))
print('not(var4 or var5 < 22?) ',not(var4 <22 or var5 < 22))

#if statement

some_condition = True 

if some_condition:
    print('The variable \'some_condition\' is True')
else:
    print('The variable \'some_condition\' is False')

#What should i wear?

temp = int(input('Please enter the temperature in Celsius. \
An integrer between 0-40: >>>>>>'))

if temp > 30:
    print('Wear shorts and sun cream!')
elif temp <= 30 and temp > 20:
    print('It\'s warm, but not shorts weather!')
elif temp <= 20 and temp > 10:
    print('You\'ll probably need a vest today!')
else: 
    print('Too cold! Don\'t go out!')    
