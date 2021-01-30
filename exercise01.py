# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 10:00:21 2020

@author: sierr
"""

#Ask the user for the radius of a circle and then print the area 

radius = float(input('To calculate the area of a circle\t Please insert the radius: '))
pi=3.14159
area = pi*radius**2

print('for a radius of ',radius,' the area of the circle is\t',area)

#Convert farenheit to celsius
print('Farenheit(ºF) to celsius(ºC) convertor')
fahrenheit = float(input('Please insert Fahrenheit (ºF): '))
celsius = (fahrenheit-32)*5//9
print(fahrenheit,'ºF is equal to: ',celsius,'ºC')

#Obtain the sum of two integrers 
print('Addition of two numbers calculator')
num_1 = int(input('Please insert a number: '))
num_2 = int(input('Please insert a second number: '))
suma = num_1+num_2

print('The sum of ',num_1,' and ',num_2,' equals: ',suma)

#Obtain the product of two integrers
print('Product of two integrers calculator')
num1 = int(input('Please insert a number: '))
num2 = int(input('Please insert a second number: '))
product = num1*num2

print('The product of ',num1,' and ',num2,' equals: ',product)

print('\nBob, Ann, Jane and Ashwin want to order pizza - they know they will each eat 4 slices of pizza. The local pizza shop sells pizza of only 6 slices Whats the minimum number of pizzas needed- use floor division \n')

needed_slices = 4*4 #16

minimum_pizzas = (needed_slices+5)//6 # A multiple of 6 or 1 higher than what we get from floor division
total_slices = minimum_pizzas*6
slices_left = minimum_pizzas*6-needed_slices
print('\nThe number of slices than bob, Ann, Jane and Ashwin need is ',needed_slices, end=' ' )
print('if they buy ',minimum_pizzas,'they will have a total of ',total_slices,' slices', end=' ')
print('And a reminer of ',slices_left,'slices')

def two_sum(list_v, num):
    '''recives a list and find the two numbers that sum a given number'''
    
    for i in range(len(list_v)):        
        for j in range(len(list_v)):
            if list_v[i] + list_v[j] == num:
                print(i, list_v[j])
    print('-1')