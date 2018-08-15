# from sys import argv# Add argument variavle(argv) from sys module
#
# script, filename = argv# Unpack argv and assign it to all of these variables in the left order
#
# txt = open(filename)# Open file with open funtion and assign it to txt
#
# print(f"Here's your file {filename}:")# print something with the format string
# print (txt.read())# Read the the text file by read function without any parameters and print file's content
#

# Worse way to get file name. You can not tab to match the filename quickly like what we can do
#  with argv, because we type in terminal
from sys import argv

filename = argv

prompt = '> '
filename = input("{} Enter your file name:".format(prompt))

txt = open(filename)

print(f"Here's your file {filename}.")
print(txt.read())
