####################################  Lists ---->  Ordered, Mutable, Duplicates OK

#name = ["Chris", "Bryan", "Delvys"]
#age = int(input("Enter your age: "))


#list = ["apple", 25, 27.5, "strawberry", 25]
#list = [10, 39, 750]

#list.append("banana")
#list.clear()
#print(list.count(25))  
#list.index(25)                 locates index of specified element
#list.insert(2, "kiwi")         Two arguments  (index, what_gets_inserted )  can be str, int, float or bool
#list.pop(index)                pops last element by default, can specify .pop(index)
#list.remove("strawberry")      removes specified element
#list.sort()
#list.reverse()


##########################################  Tuples ----> Ordered, Immutable, Duplicates OK


#tuple1 = (10, 20, 50.7, "mango", 20, 20, 20)
#print(tuple1.index('mango'))             ### Gives index of given values' 1st appearance 
#print(tuple1.count(20))                  ### Gives num of time the element was seen

#my_tuple = (750, 'Nissin')
#print(my_tuple.count(750))
#print(my_tuple[2])





################################## Sets ---> Unordered, Mutable, NO duplicates
"""
my_set = {10, 37, 600, "Apple"}
second_set = {600, 750, 'banana', "Apple"}
third_set  =  {'mango', '4', 600}

my_set.add(750)                   
third_set.add(750)                   
#my_set.clear()                    
same = my_set.intersection(second_set)
diff = my_set.difference(second_set)
my_set.difference_update(second_set)    # Needs reviewing
my_set.intersection_update(second_set)  # this one two, im prob smth easy
# Before I continue ill just review the set methods now

numbers = {1, 50 ,49, 77, 90, 103}
odds = {number for number in numbers if number % 2 == 1}
third_set = {'Nissan', 'sr20', 'det', 77, 78}
#even_oddSet = {'Odd' if number % 2 == 1 else 'Even' for number in numbers}
#even_oddList = ['Odd' if number % 2 == 1 else 'Even' for number in numbers]



#print(numbers)
#print(odds)
#print(odds.difference(numbers))
#print(odds.intersection(numbers))
#odds.add(40)           # the comp only creates set, doesnt maintain it
#odds.discard(77)

#subset = numbers.issubset(odds)
#subset = odds.issubset(numbers)
#subset = numbers.issuperset(odds)
#subset = odds.issuperset(numbers)
#disjoint = odds.isdisjoint(third_set)         # Returns True if sets have no shared elements
#print(odds.union(numbers))                   # Union doesnt modify OG list
#print(odds.symmetric_difference(third_set))   # Returns all unique from both sets
#print(odds.difference(third_set))            # Returns elements in caller, absent in called
#odds.symmetric_difference_update(numbers)    # Updates caller to difference from called
#odds.update(third_set)                        # Modifies OG set


print(odds)
print(numbers)
"""

#name = input("Enter your name: ")
#age = int(input("Enter your age: ")) 
#birthday = input("Enter your birthday: ").lower()



#def user_info():
#    if birthday == "october7" or birthday == "january20":
#        print("Yoo its a real nigga bday")
#    elif birthday == "july27":
#        print("Yoo its another real nigga bday")
#    else:
#        print("Its somebodys birthday!")


#games = ["Call-Of-Duty", "GTA", "Midnight Club"]
#games.append("FarCry")
#numbers = (10, 25, 50)

#full_name = "Christian Alvarez"

#first_name = full_name[:9]
#last_name = full_name[-7:]

#print(first_name)
#print(f"{first_name} {last_name}")

############################### Dictionary ---> Ordered, Mutable, NO Duplicates

###############################                   Bike Dict
'''
bikes = {
    "Suzuki": "gsxr",
    "Yamaha": "r1",
    "Kawasaki": "zx10r",
    "Honda": "cbr"
}
more_bikes = {
    "Ducati":"v4",
    "Aprilia":"rsv4"
}

#print(bikes.get("Yamaha"))         # Gives value of specified key
#print(bikes.keys())                # Returns a list with all keys
#print(bikes.values())               # Returns a list with all values
#print(bikes.items())               # Gives back a list, each k:v in a tuple 
#bikes.update(more_bikes)            # Update a dict with the (specified) dict
#print(bikes.popitem())             # Pops and Returns the last k,v pair 
#print(bikes.pop('Kawasaki'))        # Pops specified key, Returns that value 

print(bikes)

'''
##################################### Capitals dict
"""
capitals = {
    "Usa":"Washington DC",
    "Cuba":"Havana",
}

more_capitals = {
    "Puerto Rico":"San Juan",
    "China":"Beijing",
}


#print(capitals.get("Cuba"))
#print(capitals.keys())
#print(capitals.values())
capitals.update(more_capitals)
#print(capitals)
for k, v in capitals.items():
    print(f'Country: {k} \n \t Capital: {v}')     ## Just learned why i needed items

"""

##############################################  My original attempt at this replit
'''
counter = 0
print("Welcome to the lyrics game! ")
print()

def evaluation(counter):
  running = True
  questions = []
  
  
  while running:
    question_one = input("Never made it as a _____ man: ").lower()
    questions.append(question_one)
    if questions[0] == "wise":
      print("Nice")
      counter += 1
      break
    else:
      print("Nope try again!")
      break
  while running:
    question_two = input("Couldnt cut it as a _____ man stealing: ").lower()
    questions.append(question_two)
    if questions[1] == "poor":
      print("Das right")
      counter += 1
      break
    else:
      print("Not that one")
      break
  while running:
    question_three = input("This is how you _____ me: ").lower()
    questions.append(question_three)
    if questions[2] == "remind":
      print("Yesssir")
      counter += 1
      break
    else:
      print("Nopeeee")
      break


  print(f"You got {counter}/3 questions right! ")
evaluation(counter)
'''
##############################################  My up-to-date attempt at this replit 09/15
"""
import time
questions = []
score = 0

while True:
    q1 = input("Never made it as a ____ man: \n").lower()
    if q1 == 'wise':
        score += 1
        print("Nice")
        time.sleep(1)
    else:
        print("Nope try again..")
        time.sleep(1)
    q2 = input("Couldnt cut it as a ____ man stealing.. \n").lower()
    if q2 == 'poor':
        score += 1
        print("Good")
        time.sleep(1)
    else:
        print("Nope try again..")
        time.sleep(1)
    q3 = input("This is how you ______ me \n").lower()
    if q3 == 'remind':
        score += 1
        print("Very well")
        time.sleep(1)
        break
    else:
        print("Nope try again..")
        time.sleep(1)
        break
    
print(f'Nice jobbb you got {score}/3 correct! ')

"""


###########################################  Handling a value error
######## Color codes
#\033[1;30m   BOLD GREY
#\033[1;31m   BOLD RED
#\033[1;32m   BOLD YELLOW
#\033[1;33m   BOLD ORANGE
#\033[1;34m   BOLD BLUE
#\033[1;35m   BOLD CREAM
#\033[1;36m   BOLD CYAN
#\033[1;37m   BOLD WHITE
#\033[1;38m   BOLD RED
"""
while True:
  try:
      user = int(input("Enter your age: "))
      print(f"\033[1;32m  You're {user} ? \033[0m")
      
  except ValueError:
      print("\033[1;31m Invalid input \033[0m")
"""
#############################################   Handling index errors 
'''          
cars = ["ranger", "rouge", "altima", "brz"]
try: 
    print(cars[4])

except IndexError:
    print("Specified index: Empty")

try:
    print(cars[4])

except IndexError:
    print("\033[31m Index: Empty")
'''
#############################################   Handling key errors 
"""

car_dict = {
    "Nissan":"Silvia",
    "Toyota":"Supra"
}
try: 
    print(car_dict["Mazda"])
    print(car_dict[0])

except KeyError:
    print("\033[32m Invalid key")
"""
''' 
name, age, last_name = "Chris ", 20, "Alvarez"

try:
    print(name + age)
    #print(name + last_name)

except TypeError:
    print("\033[1;36m Mix-matched data type concatenation")
'''
"""
bikes = ["gix", "yam", "kaw", "duc", "hon"]
bikes.append("gix")
bikes.clear()
bikes.count("gix")

for bike in bikes:
    print(bike)
print(bikes.count("gix"))
"""
'''

sasuke_moves = {"Amaterasu", "Fireball Juitsu", "Kirin"}
killua_moves = {"Rhythm Echo", "Thunderbolt", "Yo-Yos"}
goku_moves = {"Kamehameha", "Spirit Bomb", "Kaio-ken"}
meliodas_moves = {"Full Counter", "Hellblaze", "Assault Mode"}
fighters = ["sasuke", "killua", "goku", "meliodas"]


print("🥊 FIGHTERS: Sasuke   Killua    Goku     Meliodas 🥊")
player1 = input("Player 1 select a fighter > ").lower()
player2 = input("Player 2 select a fighter > ").lower()


while True:
  if player2 == player1:
    print("Please select another fighter")
    player2 = input("Player 2 select a fighter > ").lower()
    continue
  elif player1 not in fighters:
    print("Who's that?")
    player1 = input("Player 1 select a fighter > ").lower()
  elif player2 not in fighters:
    print("I dont know that fighter")
    player2 = input("Player 2 select a fighter > ").lower()
  break

print()
print(f"Let the match begin!  {player1} vs. {player2}")
print()

if player1 == fighters[0]:
  player1_attacks = sasuke_moves
elif player1 == fighters[1]:
  player1_attacks = killua_moves
elif player1 == fighters[2]:
  player1_attacks = goku_moves
elif player1 == fighters[3]:
  player1_attacks = meliodas_moves


if player2 == fighters[0]:
  player2_attacks = sasuke_moves
elif player2 == fighters[1]:
  player2_attacks = killua_moves
elif player2 == fighters[2]:
  player2_attacks = goku_moves
elif player2 == fighters[3]:
  player2_attacks = meliodas_moves




`'''
"""

import random

def any_sided():
  user = int(input("Enter your dice # of sides: "))
  num = random.randint(1, user)
  print(num)

def six_sided():
  i = random.randint(1, 6)
  return i

def eight_sided():
  x = random.randint(1, 8)
  return x

def multiply():
  result = six_sided() * eight_sided()
  return result

running = True

while running:
  fighter = input("Enter your fighter: ")
  hp = multiply()
  print(f"{fighter} has {hp}hp")
  restart = input("Do you want to go again? ").lower()
  if restart[0] != "n":
    continue
  else:
    running = False

"""
'''
fruits = ["apple", "banana"]
fruits.append("mango")


#print(type(fruits))

for fruit in fruits:
    print(fruit * 2)
  
for letter in fruits[2]:
  print(letter * 5)
'''
"""
class bikes:
    
    
    def __init__(self, make, year, model):
        self.make = make
        self.year = year
        self.model = model

gix = bikes("Suzuki", 2005, "gsxr")

print(gix.model)
"""

'''
class Employee:                     # blueprint for creating instances
    
    employer = "company.inc"         # example of a class variable

# def __init__: special method to create instances
    def __init__(self, name, age, pay):       # self is labeled self by 
        self.name = name                      # convention. first arg used  
        self.age = age                        # for the instance
        self.pay = pay                # examples of instance variables

emp_1 = Employee("Chris", 20, 75000)    #first instance
emp_2 = Employee("Mary", 25, 60000)     #second instance
emp_3 = Employee("Jane", 30, 80000)     #third instance

print(emp_1.__dict__)         #     __dict__ used to see the name-space for each inst 
print(emp_2.__dict__)
'''
"""
class Player:
    
    char_count = 0
    
    def __init__(self, user_id, health, weapon):
        self.user_id = user_id                  # variables are properly reffered to as properties for classes
        self.health = health
        self.weapon = weapon
        Player.char_count += 1

    def showcase(self):                       #   functions are properly referred to as methods for classes
                                              #   for the Player class
        return f"Here we have {self.user_id} with a {self.weapon} at {self.health} hp!"
        #return "Here we have {} with a {} at {} hp!".format(self.user_id, self.weapon, self.health)
        
        # f-strings make the code cleaner and more readable



sly = Player("slyandlethal", 750, "ballista")
kay = Player("kay", 4000, "D-Skimmi")

#print(Player.char_count)
#print(sly.showcase())
"""
''' 
import time

cars = []

class Car:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

    def engineSpecs(self, name, hp):
        print(f"Lets pop the hood on that {self.model}")
        time.sleep(2)
        print(f"Damnnnn, is that a {name} ? How much hp?  {hp}")


for _ in range(2):
    model = input("Enter your car model: ")
    cap = int(input("Enter your vehicle capacity: "))
    car_creator = Car(model, cap)
    if model in cars:
        continue
    else:
        cars.append(car_creator)


#car1 = Car("Durango", 8)
#car2 = Car("Silvia", 2)
#car2.engineSpecs('SR20det', 400)
#car1.engineSpecs('Hemi', 350)


while True:
    suggestion = input("What should we do today? ")
    size = int(input("How many people you bringing? "))
    time.sleep(1)
    if size > 2 and size <= 8:
        print(f"Aighttt lets take the {user_01.model}")
    elif size <= 2:
        print(f"Bet lets take the {user_02.model}")

'''









# '''
"""
class onlineCourse:
    students = []

    def __init__(self, teacher):
        self.teacher = teacher
        

    def enrollStudent(student):
        if student not in onlineCourse.students:
          onlineCourse.students.append(student)
          print(f"{student} has been enrolled! ")
        else:
          print("That student is already enrolled")

    def classroom(self):
       print(f"{self.teacher} is teaching the class of: {onlineCourse.students}")
          

    
prof = onlineCourse("Mr. Bean")
onlineCourse.enrollStudent("John")
onlineCourse.enrollStudent("Billy")
onlineCourse.enrollStudent("Joe")
onlineCourse.enrollStudent("Billy")
onlineCourse.classroom(prof)
"""
'''
employees = []

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_amount(self):
        self.salary *= 1.5
        print(f"{self.name} has earned a raise! Hes now making: {self.salary}")

    def emp_cars(self):
        car = input("What car would you like to take to work today? ").lower()
        print(f"{self.name} is driving his {car} to work! ")

    def hiring(self):
        num = int(input("How many hirees? "))
        for i in range(num):
          name = input("Enter your employee name: ")
          salary = int(input("Enter your employee salary: "))
          emp = Employee(name, salary)
          employees.append(emp)
          for employee in employees:
            print(employee.name, employee.salary)
    


emp1 = Employee('Whis', '75000')
emp1.hiring()
emp1.avg_pay(employees)

'''
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class Fiction(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre
    
    def info(self):
        super().info()
        print(f"Genre: {self.genre}")



book1 = Fiction("Power of now", "Ekhert Tolle", "Spiritual")
book1.info()
"""

# To use dicts with classes effeciently, ill practice them more before including.
'''
bike_yr = {
    "gsxr":2005,
    "cbr":2008,
    "s1k":2016,
    "yamaha":'r1'
}
bike_yr_two = {
    "ducati":'v4'
}

#print(bike_yr.items())        # Packs your key:value pairs into a list, each k:v in a tuple
#print(bike_yr.get('cbr'))    # get method gets the value for specified key
#popped = bike_yr.pop('gsxr')  # Tnteresting. pop method return the value of the popped ("key")
#print(popped)                # var popped = 2005 in this case
#popped2 = bike_yr.popitem()   # pops and returns the last k:v in your dict
#print(popped2)               #
#bike_yr.update(bike_yr_two)   # updates the dict that used the method by adding the (dict2)
#print(bike_yr.values())      # sticks your values in a list, inside a tuple (i think)
#print(bike_yr.clear())        # wipes dict clean
print(bike_yr)
'''











################################################ Vehicle class
"""

import time

class Vehicle:
    garage = {}

    def __init__(self, make, model):
        self.make = make.capitalize()
        self.model = model.title()

    def __str__(self):
        return f'Make: {self.make} \nModel: {self.model}'
    
class EngineSpecs(Vehicle):
    
    def __init__(self, make, model, engine, hp):
        super().__init__(make, model)
        self.engine = engine.lower()
        self.hp = hp
        self.garage.update({make: model})
      
    def __str__(self):
        if self.engine.count('t') >= 1:
            return f'The {self.make} {self.model} comes equipped with a turbocharged {self.engine}'
        else:
            return f'The {self.make} {self.model} comes equipped with a {self.engine}'



amount_cars = int(input("How many cars do you want to make? "))
for _ in range(amount_cars):
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    time.sleep(2)
    engine = input("Enter the engine your car is equipped with: ")
    car = EngineSpecs(make, model, engine)
    print(car)
    time.sleep(2)
    print()
for k, v in Vehicle.garage.items():
            print(f"{k}: {v}")
    


#car = Vehicle('nissan', 'silvia')
#car2 = Vehicle('toyota', 'supra')
#car1_engine = EngineSpecs(car.make, car.model, 'sr20det')



"""
'''
import os

with open('Testing.html', 'w') as file:
    file.write("Lets do some testing")
    file.seek(15)                    ####### seek- replaces your position in file to given index 
    file.write("Testing Done...")

os.remove('Testing.html')

'''
################################################### Bank class
"""
class Bank:
    def __init__(self, name, bank_id):
        self.name = name
        self.bank_id = bank_id
        self.banks = []

    def __str__(self):      # This dunder method allos you to print the object in a string format 
        return f'Bank: {self.name} \nBank Id: {self.bank_id}'          # otherwise you get mem location

class Account(Bank):
    def __init__(self, name, bank_id, balance):
        super().__init__(name, bank_id)
        self.balance = round(balance, 2)                     ## Applying functions here is handy


    def __str__(self):
        return f"Client Name: {self.name} \nClient Id: {self.bank_id} \nBalance: ${self.balance}"
    
    def viewBalance(self):
        print(f"Your current balance is: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} successfully deposited.\nCurrent Balance: ${self.balance}")
        





num_of_clients = int(input("How many clients would you like to have? "))

for _ in range(num_of_clients):
  name = input("Enter your name: ")
  client = input("Enter your client ID: ")
  cash = float(input("Enter your current funds: "))
  acc01 = Account(name, client, cash)
  #acc01 = Account('Chris', "750", 500)
  acc01.withdraw(250)
  print()

"""
################################################# List Comprehensions
'''
nums = [0, 5, 10, 555, 600]
evens = [num for num in nums if num % 2 == 0]
odds = [num for num in nums if num % 2 == 1]

fruits = ['apple', 'mango', 'coconut', 'kiwi']
wFruits = [fruit for fruit in fruits if fruit.count('w') >= 1]
#print(wFruits)

mySet = {1, 5, 26, 50, 600}
secondSet = {num for num in mySet if num % 5 == 0}

print(secondSet)

'''
"""

my_list = ['America', 'Germany', 'Australia']
nums = [1, 2, 3]
A_list = [word for word in my_list if word if word.startswith('A')]
joined = ' /// '.join(my_list)

userI = input("Name/Age/Weight: ")
name_age = userI.split("/")
print(f"Name: {name_age[0]} \nAge: {name_age[1]} \nWeight: {name_age[2]}lbs")
"""
######################################### Dict Comprehenssion
'''

capitals = {
    'United States':'Washington DC',
    'Puerto Rico':'San Juan',
    'Australia':'Sydney'
}


#for k, v in capitals.items():
#    print()
#    print(f"{k}: {v}")

#more_capitals = {k:v for (k, v) in capitals.items() if v.lower().count('s') >= 1}
#more_capitals = {key:value for (key, value) in capitals.items() if value.lower().count('y') >= 1}

from random import randint, choice
programmers = ['Delvys', 'Bryan', 'Chris', 'Willie', 'John', 'Jamie']
choice = choice(programmers)
print(choice)
nums = [randint(1, 6)]
nums
######## zip function, two lists as args in a dict comprehension
# zip must takes each sequences first element and links them, the choice gives it a word and zip takes the first letter.
dev_dic = {k:v for (k, v) in zip(choice, nums) }
print(dev_dic)




from random import randint, choice

programmers = ['Delvys', 'Bryan', 'Chris', 'Willie', 'John', 'Jamie']
nums = [1, 2, 3, 4, 5 ,6]

dev_dic = {k:v for (k, v) in zip(programmers, nums)}

for k ,v in dev_dic.items():
    print(f'Name: {k} \nEmployee ID: {v}')
    print()


'''
"""
##################################### Set comprehensions
numbers = {1, 50 ,49, 77, 90, 103}
odds = {number for number in numbers if number % 2 == 1}
third_set = {'Nissan', 'sr20', 'det', 77, 78}
#even_oddSet = {'Odd' if number % 2 == 1 else 'Even' for number in numbers}
#even_oddList = ['Odd' if number % 2 == 1 else 'Even' for number in numbers]
"""
'''
class Vehicle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def __str__(self):
        return f'Make: {self.make} \nModel: {self.model} \nColor: {self.color}'

    def drive(self):
        print(f"The {self.model} started driving.")



class SportCar(Vehicle):
    def __init__(self, make, model, color, engine):
        super().__init__(make, model, color)
        self.engine = str(engine).upper()
    
    def drive(self):
        print(f'You finally took the {self.model} out for some fun! ')

    def engine_info(self):
        if self.engine.count('T') >= 1:
            print(f"The {self.make} {self.model} came with a turbocharged {self.engine}")
        else:
            print(f"The {self.make} {self.model} came with a {self.engine}")
            


class Motorcycle(SportCar):
    def __init__(self, make, model, color, engine, rider):
        super().__init__(make, model, color, engine)
        self.rider = rider
        
    #def drive(self):
    #    print(f"{self.rider} is riding his {self.make} {self.model}")


gix = Motorcycle('Suzuki', 'gsxr', 'black', 750, 'Whis')
s15 = SportCar('Nissan', 'silvia', 'grey', 'sr20det')
gix.drive()
gix.engine_info()


#evo = SportCar('Mitsubishi', 'Evo', 'Black', '4g63t')
#evo.drive()
#print(evo)
'''
import os

os.remove('main.py')