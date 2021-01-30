# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:53:23 2020

@author: sierr
"""
'''
Question 1 
Ask the user for two numbers between 1 and 100. 
then count from the lower number to the higher number 
print the result to the scream
'''
#Student version

##We ask for the two numbers and we set in into variables
print('Please insert two integrers between 1 and 100')
count = 0
num1 = input('Insert first number:\n>')
num2 = input('Insert second number:\n>')
#We check if the user actually inserted numbers
if num1.isdigit() and num2.isdigit():
    #We create a list so we can sort the numbers and set the two numbers while converting 
    #them to integrers with int()
    data1 = [int(num1),int(num2)]
    #We sort the numbers and create a copy of the list 
    #so we dont interfear with the original list
    data1 = sorted(data1)
    data1_copy = sorted(data1)
    print(data1_copy)
    #We create a while loop to count the numbers beteween the 
    #smallest number and the biggest number it stons when they are the same number 
    while data1_copy[1] >= data1_copy[0]:
        count += 1
        #We make sure each interection the smallest number is 1 
        #number closer to the biggest number ill they are equal
        data1_copy[0] += 1
        #print the result
    print('The smaller number is ',data1[0],' and the greater one is ',data1[1],', they are ',count-1,' beteewn the two number')   
else: 
    #if the user dint put a digit then it gives an error
    print('error')
    

    
#professor

# num_1 = int(input('Please enter a number between 1-100:> '))
# num_2 = int(input('Please enter a number between 1-100:> '))
#  
#while num_1 < 0 or num_2 <0 or num_1 > 100 or num_1 == num_2:
#    print('Numbers must be different values between 1 and 100, try again')
#    num_1 = int(input('Please enter a number between 1-100:> '))
#    num_2 = int(input('Please enter a number between 1-100:> '))
#  
#if num_1 < num_2: 
#    for i in range(num_1,num_2+1):
#        print(i, end=' ')
#else:
#    for i in range(num_2, num_1+1):
#        print(i,end=' ')
'''
Question 2
Ask the user to input a string and then print it put to the
screen in reverse order (use a for loop)
'''
##student version
#We ask for the string and we set it into a variable
string = input('Insert a string: \n>') 
#we calculate the len of the string and we set it into a variable
len_string = len(string)
#We make a for loop using the len of the string starting from the greatest number 
#to the lowest (-1)
for i in range(len_string, 0, -1):
    #We print the sting in the possition of the greatest number -1
    #we set it into the same line with end=
    print(string[i-1],end = '')

##Professor version 
#
#word = input('Please enter a word:> ')
#reverse_string = ''
#for char in word:
#    reverse_string = char + reverse_string
#
#print (reverse_string)
#print(word[::-1])
'''
Question 3 
ask the user for a number between 1 and 12 and then 
display a times table for that number 
'''

##student response, it brakes so easily but im tired of existing
#We ask for a number and set it into a variable
number = input('Please insert a digit between 1 and 12:\n>>')
#we set a while loop so it keeps asking till it has an digit
while number.isdigit() == False:
 number = input('Please insert a digit between 1 and 12:\n>>')
#Once we have a digit we convert it into integrers
number = int(number)
#We check if the number if greater than 1 and lower than 12
if number >= 1 and number <= 12:
        #we make a for loop that calculates the number 
#        times the iterator, if the number is 3 then goes 
#        3*0=0 3*1=1 3*2=6 3*4=12 3*5=15 and so on
      for i in range(13):
          print(number*i,end=' ')
#If the number is smaller than 1 we create a loop to keep asking they
#For a valid number
elif number < 1:
    #we check if they insert a digit and then we convert it 
    #to integrer so we can create a while loop 
    #that continies to ask as long as number is lower than 1      
      while number < 1:
         number = input('the number is too low. Please insert a digit between 1 and 12:\n>>')
         if number.isdigit():
             number = int(number)
        #Once the number is greater than 1 and a valid digit 
      #We ask once again if the number is digit 
      #and if the number is higher than 1 and lower than 12
      if number.isdigit() and number >= 1 and number <= 12:
          #if the number mets al conditionals we realize the equation once again
         number = int(number)
         for i in range(13):
              print(number*i,end=' ')
#We do the same but this time in case the number is higher than 12
elif number > 12:
        while number > 12:
            number = input('Please insert a digit between 1 and 12:\n>>')
            if number.isdigit():
                number = int(number)
        if number.isdigit() and number >= 1 and number <= 12:
            number = int(number)                 
            for i in range(13):
             print(number*i,end=' ')
#In case they dont put a number
else:
     print('You ruined everything')


#professors 

#user_input = input('Please enter = number between 1 and 12:>')
#
#while(not user_input.isdigit()) or (int(user_input) <1 or int(user_input > 12)):
#    print('Must be an integer between 1 and 12')
#    user_input = input ('Please make selection:>')
#user_input = int(user_input)
#print('===========================')
#print()
#print(f'this is the {user_input} times table')
#print()
#for i in range(1,13):
#    print(f'{i} x {user_input} ={i*user_input})
#    
'''
Question 4 
Can you amend the solution to question 3 so that 
it just prints out times table between 
1 and 12? (no need to ask the user for input )
'''
#We set a variable to 0
count = 0
#We make a while that will continue while the count varieble is lower than 12

while count < 12:
#We increase the variable by one so each time the loop iterates 
#it gets higher by 1
 count+=1 
#We print the actual number of the variable
 print('\n\n',count,' times ----------------------------\n')  
#We make a iterator inside the while loop 
 for i in range(13):
#This iterator will multiplicate the variable inside the while loop 
#times the the number of iterations it does
   print(count*i,end = ' ')
'''
Question 5 
Ask the user to input a sequence of numbers. 
then calculate the mean and print the result
 the sum of the values divided by the number of values.
'''
##student response
#We ask for 6 numbers and we transforme them into integrers
num1 = int(input('Please insert a number 1\n>'))
num2 = int(input('Please insert a number 2\n>'))
num3 = int(input('Please insert a number 3\n>'))
num4 = int(input('Please insert a number 4\n>'))
num5 = int(input('Please insert a number 5\n>'))
num6 = int(input('Please insert a number 6\n>'))
#we set a list with the valiues
numbers = [num1,num2,num3,num4,num5,num6]
#we sum every number within the list with the sum() function
sum1 = sum(numbers)
#We print the total sum   
print(sum1)
#we print the total sum divided by the number of vales, this time 6
print(sum1//6)

#profesor 
#
#user_input = input('Please enter a number type exit to stop:>')
#numbers=[]
#while user_input.lower()!= 'exit':
#    while not user_input.isdigit():
#        print('That\'s not a number!')
#        user_input = input('try again:>')
#    numbers.append(int(user_input))
#    user_input = input('Please enter next number:>')
#total = 0
#for number in numbers:
#    total+=number
#print(f'Mean is {total/len(numbers)}')
#print(sum(numbers)/len(numbers))
'''
Question 6 
Write code that will calculate 15 factorial (Factorial 
is the product of positive ints up to a given numbr. e.g 
5 factorials is 5*4*3*2*1)
'''
#student
print('15 factorials')
#we create a variable containing 1 more the times we want to factorial
count = 16
#We create a variable that will contain the multiplication
multiple = 1
#We create a iteration in the rage of our dessired factorial
for i in range(15):
#in each interation we disminiate eh value of count by 1
    count -= 1
    #we print a visualization of the multiplication
    print(f'x {count} ',end='')
    #We set multiple to count and them we multiply it by it
    multiple *= count
#we print the end result
print('= ',multiple)

#professor
n = 15
fact = 1
for i in range(1,n+1):
    fact = fact * i
    
print(fact)
'''
Question 7 
write code to calculate Fibonacci numbers. 
Create list containing fisrt 20
fibonacci numbers , (fib numbers made by the sum 
                     of preceedig two 
                     series, starts 0 1 1 2 3 5 8 13....)
'''
#Number of Fib numbers required 
n=50

##Set a and b to the first two numbers in the sequence 
a=0
b=1

#List in which to store numbers 
fib_nums = []

#Use a for loop to create the sequence, repeat n times 
for i in range(n):
    fib_nums.append(a)
    a,b = b,a+b
    
#print(f'The first {n} Fibonacci numbers are, {fib_nums}')
'''
Question 8 
The previous question was the fisrt to contain comments. 
Go back through the other questions in this file 
and add comments to the solutions.
'''

'''
Question 9 

    *****
    *
    ****
    *
    *
    *

can you draw this using python?

'''
#Well  yes but actually no
print('******')
print('*')
print('****')
print('*')
print('*')
print('*')

##We set a variable with the desing we will be using 
#star = '*'
#
##we will need 6 lines so we do a loop witin that range pls 1
#
for i in range(1,7):
    #we do a loop for the 6 loops so it checks the value of i in each iteration
    for j in range(1,6):
        #we do a conditional for each line, represented by i 
        # on the 1th line we want 5 star so we tell it to print till j is greater than 6
        if i == 1 and j <6:
            print(star,end='')
 #Second line we only one a star so we tell it to print til J is equal to 1
        elif i == 2 and j == 1:
            print()
            print(star)
#Thrith line we want 4 star so we tell it to print till j is greater than 5
        elif i == 3 and j < 5:
            print(star,end='')
#forth line we only one a star so we tell it to print til J is equal to 1
        elif i == 4 and j ==1:
            print()
            print(star)
#5th line we only one a star so we tell it to print til J is equal to 1
        elif i == 5 and j ==1:
            print(star)
#sixth line we only one a star so we tell it to print til J is equal to 1
        elif i == 6 and j ==1:
            print(star)
'''
Question 10
Write code that will determine all odd and even numbers between 
1 and 100. put the odds in a list named odd and the evens in 
a list named even.
'''

##We create the lists
odds = []
even = []
n = 100
#We create a loop so we can go throw each number 
for i in range(n+1):
#We check if the number in i is even by checking if it can be divisible 
#by 2
    if i % 2 == 0:
        even.append(i)
    else: 
        odds.append(i)

print('Even = ',even)
print('Odds = ',odds)














