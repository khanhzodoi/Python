article = "a"
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \n{} a line."
backslah_cat = f"I'm \\ {article} \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat.format("on"))
print(backslah_cat)
print(fat_cat)
