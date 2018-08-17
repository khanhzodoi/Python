from sys import argv # import argv from sys module

script, input_file = argv# Unpack argv and assign it to all of the variables in the left hand order

def print_all(f): # define a function to print all contents of file
    print(f.read())

def rewind(f):# define function to move the r/w location to the beginning of the file
    # file.seek(offset, from_what())
        # from_what defines the point of reference
        # 0 : means your reference point is the beginning of the file
        # 1 : means your reference point is the current file position
        # 2 : means your reference point is the end of the file

    f.seek(0)

def print_a_line(line_count, f):# define function to print one line in each time and keep r/w location in the next line
    print(line_count, f.readline(), end='')

current_file = open(input_file)# Open input_file, then create file object and assign it to current_file

print("First let's rewind the whole file:\n")

# call function print_all with current_file object as the argument
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# call function rewind to make the r/w location in current_file move backward to the beginning
rewind(current_file)

print("Let's print three lines:")

# initialize current_line to 1
current_line = 1
# call function print_a_line to print only the "current_line" line in current_file
print_a_line(current_line, current_file)

current_line = current_line + 1
# call function print_a_line to print only the "current_line" line in current_file
print_a_line(current_line, current_file)

current_line = current_line + 1
# call function print_a_line to print only the "current_line" line in current_file
print_a_line(current_line, current_file)
