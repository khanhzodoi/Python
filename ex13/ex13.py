from sys import argv # Adds argv(argument variable) function from module sys

# Unpack argv and assign it to all of these below variableson the left hand in order
script, first, second, third = argv

print("The script is called: ", script)
print("His first crime is: ", first)
print("His second crime is: ", second)
print("His third crime is: ", third)
# Gets something else from the user
fourth = input("What do you think of him? ")
print("So you think that he is {}.".format(fourth))
