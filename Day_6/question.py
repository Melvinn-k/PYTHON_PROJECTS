#Write a program that keeps asking the user for the password until they enter "python123".
password = ""
while password != "python123":
    password = input("Enter a password: ")
print("Access granted")
#Ask the user for a number, then count down to 0.
number = int(input("Enter a number: "))
while number >= 0 :
    print(number)
    number -= 1
#Keep asking the user for numbers.
#Stop only when they type "stop" and print the total.
total = 0
number = ""
while number != "stop":
    number = input("Enter a number: ")
    if number != "stop":
        total += int(number) 
print("Total =", total)
#The user has to guess the number 7.
#Give hints:
#“Too low”
#“Too high”
answer = 7
guess = ""
while guess != answer :
    guess = int(input("Guess a number: "))
    if guess < answer:
        print("Too low")
    else:
        print("Too high")
print("Correct")
#Ask the user for a username.
#If it’s less than 5 characters, ask again.
user = input("Enter a username: ")
while len(user) < 5:
    print("Too short")
    user = input("Enter a username: ")
print("Accepted")

