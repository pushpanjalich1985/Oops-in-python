class BankAccount:
    def __init__(self,account_number, initial_balance):
        self.account_number = account_number
        self.__balance = initial_balance

        #the attributes we write in the lhs, and rhs don't have to be the same, but the things that are on the right side, are placeholders in the __init__

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited amount ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw  ${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Invalid withdrawl amount or insufficient funds.")
    def show_balance(self):
        print(f"Account {self.account_number} Current balnce: ${self.__balance}")

my_account = BankAccount("AI-STUDENT-2026", 1000)

print(f"Accessing public account number: {my_account.account_number}")

my_account.deposit(500)
my_account.withdraw(200)
my_account.show_balance()

# 4. Proving Encapsulation (This will cause an error)

try:
    print(my_account.__balance)
except AttributeError:
    print("\nSUCCESS: Private attribute &#39;__balance&#39; cannot be accessed directly from outside the class.")


#Inheritence

class Vehicle:
    def __init__(self,brand):
        self.brand = brand
        
    def move(self):
        print(f"The {self.brand} is moving forward")

class Car(Vehicle):
    def display_type(self):
        print(f"[{self.brand}] Vehicle type: 4-wheeler bike")

class Bike(Vehicle):
    def display_type(self):
        print(f"[{self.brand}] Vehicle type: 2-wheeler bike")

my_Car = Car("Mahindra")
my_bike = Bike("Royal Enfield")

print("-----Testing the car-----")

my_Car.display_type()
my_Car.move()

print("-----Testing the bike----")
my_bike.display_type()
my_bike.move()


class Dog:
    def speak(self):
        print("Bark")
# 2. Class Cat with its own version of speak()
class Cat:
    def speak(self):
        print("Meow")
my_dog = Dog()
my_cat = Cat()
# Store both objects in a single list
# Even though they are different types of objects, we group them together
animals = [my_dog, my_cat]

print("--- Calling speak() using a loop ---")
# Iterate through the list and call speak() on each object
for animal in animals:
# Polymorphism in action:
# Python dynamically decides which speak() to execute based on the object type!
  animal.speak()

