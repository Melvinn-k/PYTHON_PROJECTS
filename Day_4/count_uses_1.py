 #Practice 1 (Very Easy)
 #Allow 2 attempts to guess "yes".
 #Rules:
#If correct → print "Correct"
#If failed → "Out of attempts"
attempt = 0
success = True
while attempt < 2 :
    guess = input("Enter a word: ")
    if guess == "yes":
        print("Correct")
        success = True
        break
    attempt += 1
if not success :
    print("Out of attempts")

#Practice 2 (Easy)
#Allow 3 attempts to enter PIN "4321"
#Rules:
#Correct → "Transaction allowed"
#Wrong → "Wrong PIN"
#After 3 failures → "Card blocked"
attempt = 0 
correct = False
while attempt < 3 :
    PIN = int(input("Enter a pin: "))
    if PIN == 4321 :
        print("Transaction allowed")
        correct = True
        break
    else :
        print("Wrong PIN")
        attempt += 1
if not correct :
    print("Card blocked")

#Practice 3 (Medium)
#Ask for password "admin123"
#Rules:
#3 attempts
#Print "Attempts left: X" after each failure
#Lock after 3
attempt = 0
count = 3
while attempt < 3 :
    password = input("Enter password: ")
    if password == "admin123" :
        print("Welcome")
        break
    else :
        print("Attempts left:",count)
        attempt += 1
        count -= 1
if attempt == 3 :
    print("Locked")

#Practice 4 (Real-World)
#Mpesa-style PIN:
#Rules:
#PIN = "1111"
#Max attempts = 3
#If correct → stop immediately
#If wrong → count attempts
#After lock → "Try again after 24 hours"

