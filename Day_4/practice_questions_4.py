#1️⃣ Count by 3
#Print numbers from 3 to 30, counting by 3.
#📌 Use a while loop
number = 3
while number <= 30 :
    print(number)
    number += 3

#2️⃣ Stop at Zero
#Ask the user for numbers.
#Keep asking until the user enters 0.
#When they enter 0, print:
#Done!
number = int(input("Enter a number: "))
while number != 0 :
    number = int(input("Enter a number: "))
print("Done!")

#3️⃣ Skip a Number
#Print numbers from 1 to 10, but skip 7.
#📌 Use if inside the loop
number = 1
while number <= 10 :
    if number == 7 :
        number += 1
        continue 
    print(number)
    number += 1

#4️⃣ Limited Attempts
#Ask the user for a password.
#Allow 3 attempts only.
#If correct password is "python" → print "Access granted"
#If attempts finish → print "Locked out"
correct_password = "python"
count = 0
while count < 3 :
    password = input("Enter a password: ")
    if password == correct_password :
        print("Access Granted")
        break
    else:
        count += 1
if count == 3:
    print("Locked out")


#Running Total
#Ask the user to enter numbers.
#Keep adding them.
#Stop when the user enters -1.
#Print the total sum
number = int(input("Enter a number: "))
total = 0
while number != -1:
    number = int(input("Enter a number: "))
    if number != -1 :
        total += number 
print("Sum:", total)

