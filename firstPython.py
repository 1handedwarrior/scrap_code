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
#list.pop(index)                pops last element by default, can specific .pop(index)
#list.remove("strawberry")      removes specified element
#list.sort()
#list.reverse()





                                            #  Tuples support indexing since they are ordered, however immutable
#tuple = (10, 20, 50.7, "mango", 20, 20)

#print(tuple.index("mango"))
#print(tuple.count(20))     .count method shows how many times a specififed element is spotted within a list or tuple





                                            # sets are unordered and immutable
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

#bikes = {
#    "Suzuki": "gsxr",
#    "Yamaha": "r1",
#    "Kawasaki": "zx10r",
#    "Honda": "cbr"
#}
#more_bikes = {
#    "Ducati":"v4",
#    "Aprilia":"rsv4"
#}

#print(type(bikes))
#print(bikes.get("Yamaha"))
#print(bikes.keys())
#print(bikes.values())
#print(bikes.update(more_bikes))
#print(bikes["Suzuki"])
#print(bikes)



#games = ["Call-Of-Duty", "GTA", "Midnight Club"]
#games.append("FarCry")
#numbers = (10, 25, 50)

#full_name = "Christian Alvarez"

#first_name = full_name[:9]
#last_name = full_name[-7:]

#print(first_name)
#print(f"{first_name} {last_name}")



#bikes = ["gix", "yam", "kaw", "hon"]
#bikes.append("Duc")

#for bike in bikes:
#    print(bike)

#capitals = {
#    "Usa":"Washington DC",
#    "Cuba":"Havana",
#}

#more_capitals = {
#    "Puerto Rico":"San Juan",
#    "China":"Beijing",
#}


#print(capitals.get("Cuba"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.update(more_capitals))
#print(capitals)

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
#'''

sasuke = ["Amaterasu", "Fireball Juitsu", "Kirin"]
killua = ["Rhythm Echo", "Thunderbolt", "Yo-Yos"]
goku = ["Kamehameha", "Spirit Bomb", "Kaio-ken"]
meliodas = ["Full Counter", "Hellblaze", "Assault Mode"]
fighters = ("sasuke", "killua", "goku", "meliodas")
running = True


print("🥊 FIGHTERS: Sasuke   Killua    Goku     Meliodas 🥊")
player1 = input("Player 1 select a fighter > ").lower()
player2 = input("Player 2 select a fighter > ").lower()


while running:
  if player2 == player1:
    print("Please select another fighter")
    player2 = input("Player 2 select a fighter > ").lower()
  elif player1 not in fighters:
    print("Who's that?")
    player1 = input("Player 1 select a fighter > ").lower()
  elif player2 not in fighters:
    print("I dont know that fighter")
    player2 = input("Player 2 select a fighter > ").lower()
  break

print(f"Let the match begin! {player1} vs. {player2}")
print(player1)
print(player2)










#'''
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


