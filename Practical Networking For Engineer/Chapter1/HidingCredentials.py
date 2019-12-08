import getpass
import base64

#ask for username .. will be displayed when typed
uname = input("Enter your username: ")

#ask for password ... wont be displated when typed
p = getpass.getpass(prompt="Enter your password: ")

#construct credential with *.* as seperator between uname and pass
creds=uname + '*.*' +p

###Encrypt  a given set of credentials
def encryptcredential(pwd):
    rvalue=base64.b64encode(pwd.encode())
    rvalue=rvalue.decode()
    return rvalue

###Decrypt a given set of credentials
def decryptcredential(pwd):
    rvalue=base64.b64decode(pwd)
    rvalue=rvalue.decode()
    return rvalue

if __name__ == "__main__":
    encryptedcreds=encryptcredential(creds)
    print ("Simple creds: " + creds)
    print ("Encrypted creds: " + encryptedcreds)
    print ("Decrypted creds: " + decryptcredential(encryptedcreds))
