#Ask the user for numbers.
#Stop when they type a negative number.
#Print the sum of all numbers typed.
number = int(input("Enter a number: "))
total = 0
while number >= 0 :
    total += number
    number = int(input("Enter a number: "))
print(f"the sum of all the numbers is : {total}")

#Ask for a username.
#If it’s wrong → ask again.
#Maximum 3 attempts.
correct_username = "Melvin"
count = 0
while count < 3:
    username = input("Enter username: ")
    if username == correct_username :
        print("Access granted")
        break
    else:
        print("Wrond username.Try again")
    count += 1
if count == 3:
    print("Too many attempts.Access denied>")

#Print this shape using nested while loops:
i = 1
while i <= 4:
    j = 1
    while j <= i :
        print("*",end="")
        j += 1 
    print()
    i += 1

