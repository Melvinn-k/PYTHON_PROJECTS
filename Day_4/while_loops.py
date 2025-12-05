fruits = ["apple", "banana", "orange"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i+=1 
#Print numbers 1 to 10 using a while loop
i = 0
while i <= 10 :
    print(i)
    i += 1
#Create a countdown from 10 to 1.
i = 10
while i > 0:
    print(i)
    i -= 1
#Print each letter in your name using a while loop.
name = "Melvin"
i = 0
while i < len(name):
    print(name[i])
    i += 1
#Ask the user for a password.
#Keep asking while the password is NOT "python123".
password = ""
while password != "python123":
    password = input("Enter your password: ")
print("Access granted") 
#Using a list of 5 foods, print each food with index
foods = ["pilau","chicken","chapati","mukimo","samosa"]
i = 0
while i < len(foods):
    print(f"food at index {i} is {foods[i]}")
    i +=1 
