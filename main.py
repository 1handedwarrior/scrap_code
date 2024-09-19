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
odds.update(third_set)


print(odds)
print(numbers)