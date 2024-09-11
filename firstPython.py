                                            #  Lists are ordered and mutable. 
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





                                            #  Tuples support indexing since they are ordered, however immutable
#tuple = (10, 20, 50.7, "mango", 20, 20)

#print(tuple.index("mango"))
#print(tuple.count(20))     .count method- how many times a specififed element is spotted within a list or tuple





                                            # sets are unordered and mutable
#set = {10, 37, 600, "Apple"}

#set.add(750)                   I think these are the
#set.clear()                   only methods for sets 


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

"""
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

print(type(bikes))
print(bikes.get("Yamaha"))
print(bikes.keys())
print(bikes.values())
bikes.update(more_bikes)
print(bikes)
print(bikes["Ducati"])



capitals = {
    "Usa":"Washington DC",
    "Cuba":"Havana",
}

more_capitals = {
    "Puerto Rico":"San Juan",
    "China":"Beijing",
}


print(capitals.get("Cuba"))
print(capitals.keys())
print(capitals.values())
capitals.update(more_capitals)
print(capitals)

"""
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
#                               Handling a value error
#try:
#    user = int(input("Enter your age: "))
#    print(f"You're {user} ?")
    
#except ValueError:
#    print("\033[1;31m" "Invalid input")


'''                             Handling index errors
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
"""
#                           Handling key errors 
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




'''
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

    def avg_pay(self, employees):
        total = [Employee.salary for i in employees]
        print(total)

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

