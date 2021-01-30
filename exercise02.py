
'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''
class bankAccount(object):
    '''Bank account '''    
    def __init__(self,balance):
        self.balance = balance
         
    def withdraw(self,amount):
        self.balance = self.balance - amount
        print(f'You succesfully withdraw {amount}, The new balance is {self.balance}')
         
    def deposit(self,amount):
        self.balance += self.balance
        print(f'You succesfully deposit {amount}, The balance is {self.balance}')
         
    def display(self):
        print(f'The balance is {self.balance}')
         
        
        
un_dos = bankAccount(500)
un_dos.display()
un_dos.withdraw(20)
un_dos.deposit(400)
un_dos.withdraw(1000)


'''
Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''


class circle(object):
    '''Circle '''
    
    def __init__(self,radius):
        self.radius = radius
    
    def areaCircle(self):
        print(f'The area of a circle with the radius {self.radius} is {3.14159265 * (self.radius * self.radius) }')
        
        
        
circle = circle(3.5)
circle.areaCircle()