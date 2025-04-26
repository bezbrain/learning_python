# Nesting list and dictionary

person_dictionary = {
    "name": "Michael",
    "age": 32,
    "children": ["David", "Ezekiel", "Felicity"],
    "laptop": {
        "laptop_name": "HP",
        "backup": "4hrs",
        "ram": "16GB",
        "internal_memory": "256GB",
    },
}
# print(person_dictionary)

get_children = person_dictionary["children"][1]
get_ram = person_dictionary["laptop"]["ram"]
print(get_children)
print(get_ram)
