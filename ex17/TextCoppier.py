from sys import argv
#from os.path import exists # add exists() feature from os.path module

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
    # in_file = open(from_file)
    # indata = in_file.read()
indata = open(from_file).read()

print(f"\tThe input file is {len(indata)} bytes long")

# exists() function return True if file exists, otherwise it will return False
# get rid all of below residual tasks in copy
    # print(f"Does the output file exist? {exists(to_file)}")
    # print("Ready, hit RETURN to continue, CTRL-C to abort.")
    # input()

out_file =  open(to_file, 'w')
out_file.write(indata)

print("\tAlright, all done.")

out_file.close()
