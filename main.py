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

# *** LISTS ***
# ordered, mutable, sequences 
empty_list = list() # constructor
another_empty_list = []
class_roster = ["Bryce", "Finny", "Jackson", "Kevin", "Maia", "Natalie", "Paige"]
print(class_roster)
print(len(class_roster))
# Indexes start at 0 
first_item = class_roster[0]
print(first_item)
# Update an item in a list, access by index
class_roster[2] = "Jack"
print(class_roster)

# Sorting lists 
lottery_nums = [5,148, 12, 589, 1, 999, 32039458, 51]
print(sorted(lottery_nums))
print(sorted(lottery_nums, reverse=True))
print(lottery_nums) # sorted() does not modify OG list
# Sort IN PLACE -> modifies OG list
lottery_nums.sort()
print(lottery_nums)
class_roster.sort(reverse=True)
print(class_roster)

# List operations
class_roster.append("Alex")
class_roster.insert(0, "Zoie")
print(class_roster)
class_roster.remove("Zoie")
class_roster.pop() # remove last item
print(class_roster)

# Check if item exists in a list
print(13 in lottery_nums)
print(1 in lottery_nums)

# *** TUPLES ***
# ordered & immutable (can't change items)
# useful for "snapshot" of a row of data
student = ('Natalie', 17, 'Computer Science', 4.0)
print(student)
# student[3] = 2.6 # CAN'T RE-ASSIGN ITEM!

# *** SETS ***
# unsorted, stores other immutable types
# NO DUPLICATED allowed!
songs = {'Stranger', '3005', '7', '3', 'Mutt', 'Freeze', '3005'}
print(songs)
# sets can be used to de-duplicate list items
colors = ['blue', 'pink', 'purple', 'blue', 'pink']
print(set(colors))
# you CAN add/remove items
songs.add('Gypsy')
songs.add('Stranger') # duplicate value
print(songs)
# look up set OPERATIONS to compare items btwn sets

# *** DICTIONARIES ***
# mutable, but the KEYS can only be immutable types
# { key: value } pairs. Keys must be UNIQUE!
# unordered (no index, can't sort in place)
characters = { 'Aelin': 'assassin queen',
              'Karate Kid': 'pupil',
              'Mr. Miyagi': 'sensei',
              'Phil Dunphy': 'dad',
              'Wall-E': 'trash robot',
              'Princess Peach': 'damsel in distress',
              'Dexter': 'serial killer (justified)',
              'Lara Jean': 'letter writer'
              }
print(len(characters))
# dictionary with numerical keys, list values
grade_requirements = { 9: ['Bio','Math','English','PE'],
                      10: ['Chem','Math','English','PE'],
                      11: ['Physics','Math','English','PE'],
                      12: ['Math','English','PE']
                      }

# Boolean Expressions: True or False
print(10 > 5) # True
print(5 > 10) # False
print(10 >= 10) # True
print(7 <= 5) # False
print(5 == 5) # True
print(5 != 5) # False
print('a' > 'b') # False
print('cat' < 'cot') # o is GREATER bc it comes LATER
print('T' == 't') # False
print('T' < 't') # True, capital letters come first

# Checking equality vs. identity
list_a = [1, 2, 3]
list_b = [1, 2, 3]
print(list_a == list_b) # True, lists contain same items
print(list_a is list_b) # False, not the same object
# Typically one use "is" when comparingn to None, True, False
boolean_a = True
print(boolean_a is True)
print(boolean_a is not False)

# Compound boolean operators: and, or, not
boolean_b = True
boolean_c = False
print(boolean_a and boolean_b) # True
print(boolean_b and boolean_c) # False
print(boolean_b or boolean_c) # True
print(boolean_a and (boolean_b or boolean_c)) # True

# Conditionals / branching / selection
def can_drive(age):
    if (age >= 17):
        print('You can get a license in NY state!')
    elif (age == 16):
        print('You can get a permit in NY state!')
    else:
        print('Get off the road')

# Test out function with different values
can_drive(18)

# ITERATION (repetition)
# while loop: run until a condition is no longer True
max = 16
counter = 6
while (counter <= max):
    print(f'Count is {counter}')
    counter += 1

# for-in loop: iterates through a collection
print(class_roster)
for student in class_roster:
    print(student)

# for-in range
# prints 0 until 3
for num in range(4):
    print(num)
# range(start, stop) -> not inclusive of stop
for num in range(1, 6):
    print(num)
# range(start, stop, step)
for num in range(10, 50, 5):
    print(num)

# BTW, python has a help function
# help(range)

# enumerate() lets you loop through index AND items
# useful for LIST collections
for index, item in enumerate(class_roster):
    print(f'Item: {item} is at index {index}')

# use .items() on a dictionary to loop over keys AND values
for character, description in characters.items():
    # character represents the KEYS of this dict
    # description represents the VALUES of this dict
    print(f'{character} is a {description}')

# review: setting up a dictionary
hex_colors = {
    'red': '#FF0000',
    'green': '#008000',
    'blue': '#0000FF'
}
