name_key = "name"

person_dictionary = {
    name_key: "Olawale",
    "age": 30,
    "occupation": "Software Developer",
    "children": 3,
}
# print(person_dictionary["name"])

person_dictionary["partner"] = "Gloria"
person_dictionary["children"] = 4
# print(person_dictionary)

# # Wipe a dictionary
# person_dictionary = {}
# print(person_dictionary)

# Loop through dictionary keys
for key in person_dictionary:
    print("Key", key)

# Loop through dictionary values
for key in person_dictionary:
    print("Value", person_dictionary[key])
