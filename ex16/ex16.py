from sys import argv

script, filename = argv

r_mode = "read mode"
w_mode = "write mode"

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")
print("Opening the file...")
# open file object in write mode and assign it to target
target = open(filename, 'w')


print("Truncating the file. Goodbye!")
# empty the file. But in write mode, it automatically truncate the file
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("\tline 1: ")
line2 = input("\tline 2: ")
line3 = input("\tline 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("We close {} in {}.".format(filename, w_mode))
target.close()

# create new_target to open file in read mode
new_target = open(filename, 'r')
print("\nLet's see {}'s contents".format(filename))
print(new_target.read())

print("And finally, we close {} in {}.".format(filename, r_mode))
new_target.close()
