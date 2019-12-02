#create a dict
config={
    "IOS":"exec-timeout 15 0",
    "NXOS":"exec-timeout 15"
    }

getchoice=input("Enter IOS type (IOS/NXOS): ")

if (getchoice=="IOS"):
    print(config.get("IOS"))
elif (getchoice=="NXOS"):
    print(config.get("NXOS"))
##Using this approach, we can remove
##the usage of multiple if statements and directly call
##the dictionary values based upon the
##mappings done in the dictionary
