#1️⃣Ask user for username, password, and role.
#Allow login ONLY if:
#username is "root"
#password is "1234"
#role is "admin"
username = input("Enter a username: ")
password = int(input("Enter a password: "))
role = input("Enter a role: ")
if username == "root" :
    if password == 1234 :
        if role == "admin":
            print("Login successful")
        else:
            print("Login failed")
    else:
        print("Login failed")
else :
    print("Login failed")

#Ask user for age and country.
#Permit access ONLY if:
#age ≥ 21
#country is "Kenya"
#AND they say “yes” to having a passport.
age = int(input("Enter your age: "))
country = input("Enter a country: ")
passport = input("Do you have a passsport?(yes/no): ")
if age >= 21 :
    if country == "Kenya" :
        if passport == "yes" :
            print("Access granted")
        else: 
            print("Access denied")
    else:
        print("Access denied")
else:
    print("Access denied")

#Mpesa-like flow:
#Ask for amount, balance, and PIN.
#Allow transaction only if:
#amount ≤ balance
#PIN is correct
#Else show appropriate errors.
amount = int(input("Enter amount: "))
balance = int(input("Enter balance: "))
pin = int(input("Enter PIN: "))
if amount <= balance :
    if pin == 1234 :
        print("Transaction complete")
    else:
        print("Incorrect PIN")
else:
    print("Insufficient balance")

