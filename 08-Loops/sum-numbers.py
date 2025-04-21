students_scores = [150, 100, 200, 150, 500, 300]

# Using the sum function to sum all numbers
total_score = sum(students_scores)
# print(total_score)

# Using loop to sum up all numbers
total = 0
for score in students_scores:
    total += score

# print(total)

# Using the max function to get the highest number
max_number = max(students_scores)
# print(max_number)

highest_number = 0
# Using loop to get the highest number
for score in students_scores:
    if score > highest_number:
        highest_number = score
    else:
        highest_number = highest_number

    # print(highest_number)

    # Looping through a range

    array_lize_umber = []
for number in range(1, 101):
    append_number = array_lize_umber.append(number)

# print(array_lize_umber)

# Sum all numbers from 1 to 100
total_number = 0
for number in array_lize_umber:
    total_number += number

# print(total_number)

# To use the range function and increase the step
for number in range(5, 200, 5):
    print(number)
