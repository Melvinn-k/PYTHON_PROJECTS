
#Asking Until Non-Zero
#Ask the user to enter a number.
#Keep asking until the number is not zero.
#Rules:
#If number == 0 → print "Zero not allowed"
#Else → print "Accepted"
number = int(input("Enter a number: "))
while number == 0 :
    print("Zero not allowed")
    number = int(input("Enter a number: "))
print("Accepted")

#2️⃣ keep Asking Until Even
#Ask the user to enter a number.
#Keep asking until the number is even.
#Rules:
#If odd → print "Not even, try again"
#If even → print "Thank you!"
number = int(input("Enter a number(even nmber): "))
while number % 2 != 0 :
    print("Not even, try again")
    number = int(input("Enter a number(even number): "))
print("Thank you!")

#3️⃣ keep Asking Until Within Range
#Ask the user to enter a number.
#Keep asking until the number is between 1 and 10 (inclusive).
#Rules:
#If outside range → print "Out of range"
#If valid → print "Correct"
number = int(input("Enter a number: "))
while number < 1 or number > 10 :
    print("Out of range")
    number = int(input("Enter a number: "))
print("correct")

#4️⃣ Keep Asking Until Correct Word
#Ask the user to enter a word.
#Keep asking until they type "yes".
#Rules:
#If wrong → print "Try again"
#If correct → print "Correct"
word = ""
while word != "yes":
    print("Try again")
    word = input("Enter a word(type yes): ")
print("Correct")

