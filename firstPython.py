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
print(capitals.update(more_capitals))
print(capitals)