#Keep Asking Until Within Range
#Ask the user to enter a number.
#Keep asking until the number is between 1 and 10 (inclusive).
#Rules:
#If outside range → print "Out of range"
#If valid → print "Correct"
number = int(input("Enter a number: "))
while number < 1 or number > 10 :
    print("Out of range")
    number = int(input("Enter a number: "))
print("Correct")


#Keep Asking Until Non-Zero
#Ask the user to enter a number.
#Keep asking until the number is not zero.
#Rules:
#If number == 0 → print "Zero not allowed"
#Else → print "Accepted"
number = int(input("Enter a number: "))
while number == 0 :
    print("Zero not allowed")
print("Accepted")

#Keep Asking Until Even
#Ask the user to enter a number.
#Keep asking until the number is even.
#Rules:
#If odd → print "Not even, try again"
#If even → print "Thank you!"
number = int(input("Enter a number: "))
while number % 2 != 0:
    print("Not even, try again")
    number = int(input("Enter a number: "))
print("Thank you!")

#Password Retry
#Ask the user to enter a password.
#Keep asking until the password is "admin".
#Rules:
#If wrong → print "Wrong password"
#If correct → print "Access granted"
password = input("Enter a password: ")
while password != "admin":
    print("Wrong password")
    password = input("Enter a password: ")
print("Access granted")

#Count Attempts
#Ask the user to enter a number greater than 100.
#Rules:
#Count how many wrong attempts were made
#If number ≤ 100 → print "Too small"
#When valid → print "Accepted after X attempts"
attempts = 0
number = int(input("Enter a number greater than 100: "))
while number <= 100:
    print("Too small")
    attempts += 1
    number = int(input("Enter a number greater than 100: "))

print(f"Accepted after {attempts} attempts")

#Sentinel Value (-1)
#Ask the user to enter numbers.
#Stop when they enter -1.
#Rules:
#Count how many numbers were entered (exclude -1)
#Print the total count
count = 0
number = int(input("Enter a number (-1 to stop): "))
while number != -1:
    count += 1
    number = int(input("Enter a number (-1 to stop): "))

print("Total numbers entered:", count)

