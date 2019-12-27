import socket


# Validating an IPv4 address
# Method 1
def method_1():
    ip_address = input("Enter IP adress: ")

    # Remove any extra characters
    ip_address = ip_address.strip()

    # Initialize a flag to point to true for an ip add
    ip_address_flag = True

    # validate if there are only dots (.) in ip add
    if (not(ip_address.count('.') == 3)):
        ip_address_flag = False
    else:
        # Validate if each of the octet is in range 0 - 255
        ip_address = ip_address.split('.')
        for val in ip_address:
            val = int(val)
            if(not(0 <= val <= 255)):
                ip_address_flag = False

    # based upon the flag value display the relevant message
    if (ip_address_flag):
        print("Given IP is correct")
    else:
        print("Given IP is not correct")


# ==========================Method 2
def method_2():
    addr = input("Enter IP address: ")
    try:
        # Give to socket the ip address, and have socket checked the ip add
        socket.inet_aton(addr)
        print("IP add is valid")

    except socket.error:  # if any errors socket finds
        print("IP add is NOT valid")
