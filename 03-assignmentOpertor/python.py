# Assignment Operator
# =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
# The assignment operators are used to assign values to variables.
# The assignment operator (=) is used to assign a value to a variable.
# The other assignment operators are used to perform an operation on a variable and assign the result to the variable.

frequency = 4

frequency += frequency
# print(frequency)

# F-strings (This is just like template literals in JS which allows us to embed expressions inside string literals)
print("The current frequency is: " + str(frequency))

score = 20
height = 1.8
is_winning = True

# Using f-string to concatinate without the plus sign
print(
    f"Your score is={score} and your height is = {height}. Are you winning? {is_winning}"
)
