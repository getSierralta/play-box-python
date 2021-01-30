# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:48:05 2020

@author: sierr
"""

#Question 1 
#Write code that ask the user to input a number
#between 1 and 5 inclusive. 
#the code will take the integrer value and print out 
#the string value. so for example if the user inputs 
#2 the code will print two. reject any input 
#that's not in that range 

number = int(input('Please enter a number between 1 and 5: \n>>>>>'))

if number == 1:
    print('The number is: One')
elif number == 2:
    print('The number is: Two')
elif number == 3:
    print('The number is: Three')
elif number == 4:
    print('The number is: Four')
elif number == 5:
    print('The number is: Five')
else: 
    print(number,' is not within the range, please try again')



##Question 2 
#Repeat th previous task but this time
#the user will input a string and the code 
#will outpu the integer value. 
#convert the string to lowercase fisrt

numberStr = str(input('Please enter a number between one and five: \n>>>>>'))
numberStr = numberStr.lower()
if numberStr == 'one':
    print('The number is: 1')
elif numberStr == 'two':
    print('The number is: 2')
elif numberStr == 'three':
    print('The number is: 3')
elif numberStr == 'four':
    print('The number is: 4')
elif numberStr == 'five':
    print('The number is: 5')
else: 
    print(numberStr,' is not within the range or a valid format please try again')


#Question 3 
#Create a variable containing an integrer betweetn 1 and 10 inclusive.
#ask the user to guess the number. if they guess too high 
#or too low, tell them they have not won, tell them they win if they guess the correct number.

#my version 
winningNumber = 3

userNumber = int(input('Guess a number between 1 and 10. \n>>>>>>'))

if userNumber == winningNumber:
    print('Yes the number is: ', winningNumber, 'congrats!')
elif userNumber != winningNumber and userNumber <=10 and userNumber >= 1:
    print('Oh no, you lose :p')
else:
    print('Please try again and insert a valid number')

#prof version 
#
#secret_number = 3
#guess = input('Guess the number between 1-10: > ')
#if guess.isdigit():
#    guess = int(guess)
#    if guess == secret_number:
#        print('You guessed the correct number! you win!')
#    elif guess > secret_number and guess <= 10:
#        print('You guessed too high. Sorry you lose!')
#    elif guess < secret_number and guess >=1:
#        print('You guessed too low. Sorry you lose!')
#    else: 
#        print('Out of range')
#else:
#    print('That\'s not even an integrer! What are you playinng at?')

#Question 4 
#Ask the user to input their name. check the lenght of the name. 
#if its greater than 5 characters long, write a message tellinf then :
#    how many characters they have, otherwise write a message 
#    telling them the lenght of their name is a secret

name= str(input('Insert your name:\n>>>>'))
nameLen = len(name)

if nameLen > 5:
    print('Your name, ',name,', has a lenght of: ',nameLen,' letters, starting from 0')
else:
    print('The lenght of your name is a secret')

#Question 5
#ask the user for two integers betweent 1 and 20. if they 
#are both greater than 15 return their product. if only one 
#of then is greater than 15 return their sum, if neither are greater than 
#15 return 0
print('insert two integrers between 1 and 20')
number1 = input('Please insert fisrt number: \n>>>')
number2 = input('please insert second number: \n>>>')

if number1.isdigit() and number2.isdigit():
    number1 = int(number1)
    number2 = int(number2)
    if number1 >= 15 and number2 >= 15 and number1 <= 20 and number2 <= 20:
        print(number1*number2)
    elif number1 >= 15 and number1 <= 20 and number2 <= 20 or number2 >= 15 and number1 <= 20 and number2 <= 20:
        print(number1+number2)
    elif number1 < 1 or number1 >20 or number2 <1 or number2>20:
        print('out of range')
    else:
        print('0')
else: 
    print('Sure those are numbers?')


#Question 6
#ask the user for two integrers, then swap the content of 
#the variables,so if var1 = 1 and var 2 = 2 
#once the code has run var 1 should equal 2 and var 2 should equal 1

#my answer
print('please give me two integrers')

var1 = input('integrer please\n>>>')
var2 = input('more integrer please\n>>>')

if var1.isdigit() and var2.isdigit():
    var1 = int(var1)
    var2 = int(var2)
    print('Fisrt state, var1 = ',var1,' var2 = ',var2)
    var3 = var1
    var1 = var2
    var2 = var3
    print('Second state, var1 = ',var1,' var2 = ',var2)
else:
    print('I SAID INTEGRERS!!! >X(')

#professor 

#int_1 = int(input('Please enter first integer: > '))
#int_2 = int(input('Please enter second integrer: > '))
#print('Before swapping int_1 = ',int_1,' and int_2 = ',int_2)
#int_1,int_2 = int_2,int_1
#print('After swapping int_1 = ',int_1, ' and int_2 = ',int_2)
