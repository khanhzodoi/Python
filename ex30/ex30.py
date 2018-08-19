people = 30
cars = 40
trucks = 15

# Determine whether the condition is true or not. If True then run code in its blocks, otherwise check the others
if cars > people == True:
    print("We should take the cars.")
# If the above conditions were False, then determine the below condition is True or False. If True run code inside it, otherwise check the others
elif cars < people == True:
    print("We should not take the cars.")
# If all of the conditions were False, the code in this below would be excuted
else:
    print("We can't decide.")

# Determine whether the condition is true or not. If True then run code in its blocks, otherwise check other conditions
if trucks > cars == True:
    print("That's too many trucks.")
# If the above conditions were False, then determine the below condition is True or False. If True run code inside it, otherwise check the others
elif trucks < cars == True:
    print("Maybe we could take the trucks.")
# If all of the conditions were False, the code in this below would be excuted
else:
    print("We still can't decide.")

# Determine whether the condition is true or not. If True then run code in inside it, otherwise check the others
if people > trucks == True:
    print("Alright, let's just take the trucks.")
# If all of the conditions were False, the code in this below would be excuted
else:
    print("Fine, let's stay home then.")
