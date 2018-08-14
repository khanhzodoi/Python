#other ways to ask a question without print
person = input("[?]What's your name? ")
emotion = input("[?]How do you feel now? ")
favourite_sport = input("[?]What's your favorite sport? ")
age = int(input("[?]How old are you? "))
height = int(input("[?]How tall are you? "))
weight = int(input("[?]How much do you weigh?"))

greeting = "\n-----------------------------\a\
            \n[.]Hello, {}!".format(person)
print(greeting)
print("[+]Your favorite sport is {} and you feel {}.".format(favourite_sport, emotion))
print("[+]So, you're {} old, {} tall and {} heavy.".format(age, height, weight))
