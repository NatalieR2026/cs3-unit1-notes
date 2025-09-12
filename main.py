print("hello world")

# Variables store data
lucky_num = 13 # int
my_name = "Natalie" # str
cash = 5.50 # float
is_raining = True # bool
is_sunny = False

#CONCATENATE string literal + string variable
greeting = "Howdy, " + my_name
print(greeting)
# You can use single quotes instead
greeting = 'Python is cool, it\'s better than Java'
# You can use triple double quotes for long strings
long_greeting = """
                we were both young
                when i first saw you
                i close my eyes
                """
# f-strings are FORMATTED strings (like templates)
f_string = f"My name is {my_name} and my lucky number is {lucky_num}"
print(f_string)

# FUNCTIONS are reusable recipes/processes
# Use the keyword def to DEFINE a new function
def helloworld():
    # function BODY indented under the colon
    print("hello world I am a function")

# UN-indent to signal the END of that block
# CALL a void function (no output)
helloworld()

# Define a function with ARGUMENTS (input) + RETURN (output)
def multiply(x, y):
    result = x * y
    return result

# CALL a non-void function (handle the output)
five_times_three = multiply(5,3)
print(five_times_three)
# you can also call the function directly in another
print(multiply(20,6)) # funcs evaluated from INSIDE to OUTSIDE