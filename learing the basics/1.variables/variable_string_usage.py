#simple name print
name = "ada lovelace"

#the var "name" is all lowercase. The "." means the method will act on the var "name". The method capitolizes every word in a string
print(name.title())

#prints var as all uppercase letters
print(name.upper())

name = "ADA LOVELACE"
#prints var as all lowercase letters
print(name.lower())

first_name = "john"
last_name = "doe"

#the f"{x} {y}" is a formatted string. Python will interperet the vars inside the brackets "{}" and replace the value in that location
full_name = f"{first_name} {last_name}"
print(full_name)

#prints a formated string message, greating the person and capitolizes the first letter in their name
print(f"hello, {full_name.title()}")

#although f-string format is the newest way to write vars in strings, this is another way of doing it
full_name = "Hello again,{} {}".format(first_name.title(), last_name.title())
print(full_name)

#adding tabs and newline to strings
string_1 = "hello User"
string_2 = "how are you?"

#added a "tab" white space formatting and a newline between the two strings
new_message = f"\t{string_1}\n\t{string_2}"
print(new_message)

#stripping the whitespace from the new message
