# from sys import argv# Add argument variavle(argv) from sys module
#
# script, filename = argv# Unpack argv and assign it to all of these variables in the left order
#
# txt = open(filename)# Open object file with open function and assign it to txt
#
# print(f"Here's your file {filename}:")# print something with the format string
# print (txt.read())# Read the the text file by read function without any parameters and print file's content
# txt.close()
#txt_again.close()

# Worse way to get file name. You can not tab to match the filename quickly like what we can do
#  with argv, because we did not type in terminal
from sys import argv

filename = argv

prompt = '> '
filename = input("{} Enter your file name:".format(prompt))

txt = open(filename)

print(f"Here's your file {filename}.")
print(txt.read())

txt.close()
