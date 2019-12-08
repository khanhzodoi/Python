getinput=input("Do you want to store a new record (Y/N) ")
# Remove any extra space
getinput=getinput.strip()
# Convert all input to lower case
getinput=getinput.lower()
# read values and create a record
if ("y" in getinput):
    readValueName=input("Enter the Name: ")
    readValueAge=input("Enter the age: ")
    readValueLocation=input("Current location: ")
    temp=readValueName+","+readValueAge+","+readValueLocation+"\n"
    ###open a file myrecord.csv in write mode, write the record and close it
    fopen=open("myrecord.csv", "w")
    fopen.write(temp)
    fopen.close()
