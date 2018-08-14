# sets variable formatter string with four places for variables to be embeded
formatter = "{} {} {} {}"

# pass to format four arguments to match up the four {} in the variable formatter
print(formatter.format(1, 2, 3, 4)) # pass integer values to format
print(formatter.format("one", "two", "three", "four"))# pass strings to format
print(formatter.format(True, False, False, True))# pass True and False values to format
print(formatter.format(formatter, formatter, formatter, formatter))#pass four string variables formatter to format
print(formatter.format(
    'Hello, ',
    'Fall for you, ',
    'My heart will go on, ',
    'Lonely.'
))# pass my own strings (song names) to format
