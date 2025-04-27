# Line 3 is an example of docString. It is a form of brief documentation about our function and it is always written immediately after our function declaration. When you hover on function in line 8, we will see the documentation displayed
def function_with_output(sentence):
    """Format a sentence to be capitalized and print the title case"""
    print(sentence.capitalize())
    print(sentence.title())


function_with_output("this is a statement")
