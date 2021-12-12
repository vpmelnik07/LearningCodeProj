# "For" Looping

#defining list to work with in the loops
colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']

#for loop
#color is a variable name to hold the iterated values of the list
#colors is the list that the for look with iterate through
#loops are contained through indentation
for color in colors:
	print(color)

#this printout will be outside the loop and will execute after it has finished
print("that was a lot of colors!")

# "Range" looping

#num is a variable name to hold the iterated value of range
#range is inclusive to starting value, exclusive to ending value
#total loop counts is always (end value) - (start value): 5-2 = 3
for num in range(2,5):
	print(num)		#prints 2,3,4

# Making a list of numbers with range()

#like for loop range, there will be 5 numbers: 6-1=5
numbers = list(range(1,6))
print(numbers)		#contents printed: 1,2,3,4,5

#The added "2" means every 2nd number
even_numbers = list(range(2,10,2))
print(even_numbers)

#using range() loops to fill a list
squares = []
for num in range(1,10):
	square = num ** 2
	squares.append(square)

print(squares)

# iterating with range through a list of unknown size
# index_num is the iterated num 0 -> length of list
# len(squares) is the total number of entries within the list
for index_num in range(0,len(squares)):
	print(squares[index_num])  # prints the value of the indexed entry

# simple statistics with number lists
print(min(squares))

print(max(squares))

print(sum(squares))

# list comprehension, creating list by iterative value in a single line
# "value ** 2" is the iterative contents of the for loop above
# for loop created to loop on range values, results are stored within the list brackets "[]"
new_squares = [value ** 2 for value in range(1,10)]
print(new_squares)

# create a new list of all capital words of colors list
new_colors = [colors[index].upper() for index in range(0,len(colors))]
print(new_colors)

#for loop equivelant, not as simple as the list comprehension above
new_colors2 = []
for index in range(0,len(colors)):
	new_colors2.append(colors[index].upper())

print(new_colors2)

#slicing of lists
#you must specify the first and last element of the list you want to work with

players = ['charlie', 'lilah', 'alex', 'caroline' , 'jack']

#slicing will operate on the starting slice index
#slicing will not operate on the final slice value, it always ends 1 before
#3-1 = index 2 as the last operated on value
#in our case, the final print is "alex"
print(players[0:3])
print(players[1:3])

#if start index is ommited, it will start at the beginning of the list
print(players[:2])

#if ending index slice is ommited, it will operate from start index to end of list
print(players[1:])

#looping through a sliced list
#unlike range, this will loop through the first 3 indexes
for player in players[:3]:
	print(f"hello {player}, welcome to the game!")

#looping through the sliced list as a range end value, then printing the players in that slicing
for player_index in range(0,len(players[:3])):
	print(f"would you like a drink, {players[player_index]}?")


#copying whole list without specifying start/stop indexes
player_copy1 = players[:]
print(player_copy1)

player_copy1.append('joe')

#the appended joe added to the copy and not the original
print(players)
print(player_copy1)