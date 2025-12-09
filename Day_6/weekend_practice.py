#Keep Asking Until User Enters an Even Number
number = int(input("Enter an even number: "))
while number % 2 != 0:
    print("That is not an even number")
    number = int(input("Enter an even number: "))
print("Correct, that is an even number.")
#Print numbers 1–10, but skip odd numbers using continue.
number = 1
while number <= 10 :
    if number % 2 != 0:
        number += 1
        continue
    print(number)
    number += 1
#Make a menu that keeps showing until the user types "exit".
while True :
    print("\n Menu: ")
    print("1.Chapati")
    print("2.Ugali")
    print("3.Chicken")
    print("Type exit to quit")

    choice = input("Enter a choice:")
    if choice == "exit":
        print("Goodbye")
        break
#Count Digits in a Number (no strings allowed)
number = int(input("Enter a number: "))
count = 0
while number > 0 :
    count += 1
    num //= 10
print("Digits:",count) 

