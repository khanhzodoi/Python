#types_of_people holds the number 10 to be its value
types_of_people = 10

#sets x to string with one embeded format string variable 'types_of_people'
x = f"There are {types_of_people} types_of_people"

#sets binary to hold the string "binary" to be its value
binary = "binary"
#set do_not to hold the string "don't" to be its value
do_not = "don't"

#sets variable y to string with two embedded format strings
y = f"Those who know {binary} and those who {do_not}."

#display the formatted strings x && y
print(x)
print(y)

#display the formatted string in which we put the variable x
print (f"I said: {x}")
#display the formatted string in which we put the variable y
print (f"I also said: '{y}'")

#hilarious holds False to be its value
hilarious = False
#sets varriable joke_evaluation to string with the place '{}' to be embeded
joke_evaluation = "Isn't that joke so funny?! {}"

#embed the variable hilarious to formatted string variable joke_evaluation
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

#display w && e together in one string
# adding strings concatenates them, literally joining them together
print(w + e)
