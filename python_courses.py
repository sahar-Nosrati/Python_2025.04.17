# first_name = "nastaran"
# convert_string_to_uppercase = first_name.upper()
# convert_string_to_uppercase = first_name.upper()
# convert_string_to_lowecase = convert_string_to_uppercase.lower()


# print(convert_string_to_uppercase)
# print(convert_string_to_lowecase)

# street_name = "       sheykhsafi        "
# removed_whitespace_of_street_name = street_name.strip()
# print(removed_whitespace_of_street_name)
# print(street_name)

# cities = ["warsaw", "Tehran", "seol", "berlin"]
# modified_cities = []

# for element in cities:
#   if element == "Tehran" :
#     modified_cities.append(element.replace("Tehran", "Vienna"))
#     continue
#   modified_cities.append(element)

# print (modified_cities)


# modified_tehran_city = cities[1].replace("Tehran", "vienna")
# print(modified_tehran_city)
# print(cities)

# nice_sentence_text = "The sky, at sunset, looked like a carnivorous flower."

# splitted_nice_sentence = nice_sentence_text.split(" ")
# print(splitted_nice_sentence)

# first_name = "Nastaran"
# last_name = "Minaei"

# full_name = first_name + " " +last_name
# print(full_name)

replacing_flower_name = "Rose"
nice_sentence_text = "The sky, at sunset, looked like a carnivorous flower."

f_string_sentence = f"The sky, at sunset, looked like a carnivorous and {replacing_flower_name} flower."
print(f_string_sentence)