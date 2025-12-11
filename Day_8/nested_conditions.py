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
country = input("Enter a country: ").lower()
passport = input("Do you have a passsport?(yes/no): ")
if age >= 21 :
    if country == "kenya" :
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

#4️⃣ Shopping discount system:
#Ask for:
#Has coupon? (yes/no)
#Is VIP member? (yes/no)
#Rules:
#If VIP → automatic 20% discount
#If coupon → 10%
#If both → 30%
coupon = input("Do you have a coupon?(yes/no): ").lower()
vip = input("Are you a VIP member?(yes/no): ").lower()
if vip == "yes" :
    if coupon == "yes" :
        print("You have a 30% discount")
    else:
        print("You have a 20% discount")
else : 
    if coupon == "yes"
    print("You have a 10% discount")
else :
    print("No discount")

#Student exam grading system:
#Ask:
#exam score
#project submitted? (yes/no)
#Rules:
#If score ≥ 50 AND project submitted → pass
#If score ≥ 50 BUT project not submitted → “Submit project”
#If score < 50 → fail
score = int(input("Enter your exam score: "))
project = input("Have you submitted the project?(yes/no): ").lower()
if score >= 50 :
    if project == "yes" :
        print("Pass")
    else :
        print("Submit project")
else :
    print("Fail")

