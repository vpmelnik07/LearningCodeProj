#initializing a list
foods = ['bread', 'tacos', 'ice cream', 'milk']

#print will show entire list, formatting is not desirable
print(foods)

#printing individual elements based off index
print(foods[0])

#modifying individual elements for print
print(foods[0].title())

#printing the last element in the list
print(foods[-1].upper())

#list values used in strings
message = f"hello word, I love {foods[2].title()}!"
print(message)

#section will be modifying existing lists

#changing a value within the list
foods[0] = 'candy'
print("I changed my mind, I love {}!".format(foods[0]))

#adding to an existing list
foods.append('burgers')
print(f"I added a new item to my favorite foods, it's {foods[-1].upper()}!")

#inserting elements to a list at a specific location
foods.insert(0,'fries')
print(foods)

#removing elements in a list
del foods[1]
print(foods)

#pop the last item in the list
popped_item = foods.pop()
print(f"we removed this from the menu: {popped_item}")
print(foods)

#pop an item based on element position
first_item_popped = foods.pop(0)
print (f"removed this item too: {first_item_popped}\n{foods}")

