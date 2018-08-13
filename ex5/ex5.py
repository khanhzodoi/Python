name = 'Pham Khanh'
age = 21 # not a lie
height_in_cm = 176.0 #centimeters
height_in_inches = round(height_in_cm / 2.54) # inches
weight_in_kg = 76.0 #kilograms
weight_in_ibs = round(weight_in_kg / 0.453) #ibs
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height_in_cm} cm or {height_in_inches} inches tall.")
print(f"He's {weight_in_kg} kg or {weight_in_ibs} pound heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + weight_in_kg + height_in_cm
print(f"If I add {age}, {height_in_cm}, and {weight_in_kg} I get {total}.")
