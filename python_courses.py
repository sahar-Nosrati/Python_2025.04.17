import random

number = 86.6
print(type(number))

first_name = "Sahar"
print(type(first_name))

boolean_example = True
print(type(boolean_example))

fruits = ["cherry", "peach"]
print(type(fruits))

numbers_sequence = (1,2,3,4)
print(type(numbers_sequence))

apartment = {
  "location" :"Kargar", 
  "No" : 25
}
print(type(apartment["No"]))

number_range = range(6);
print(number_range) 

for element in number_range :
  print(element)

print(random.randrange(1,10));

multiple_lines_string = """Lorem ipsum"""

print(multiple_lines_string[0])

for element in multiple_lines_string :
  print(element)

print(len(multiple_lines_string))
print("ipsum" in multiple_lines_string)
print("ipsum" not in multiple_lines_string)
print(multiple_lines_string[0:4])
print(multiple_lines_string[:8])
print(multiple_lines_string[8:])