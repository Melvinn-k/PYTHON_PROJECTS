#Exercise 1 — Simple Function
#Write a function called greet() that prints:
#Hello, welcome!
#Then call the function.
def greet():
    print("Hello, welcome!")
greet()

#Exercise 2 — Function With One Parameter
#Write a function say_hello(name) that prints:
#Hello <name>!
#Ask the user for their name and pass it to the function.
def say_hello(name) :
    print(f"Hello {name}")
user = input("Enter a name: ")
say_hello(user)

#Exercise 3 — Function With Two Parameters
#Write a function add(a, b) that prints the sum of two numbers given by the user.
def add(a,b):
    print(a + b) 
num = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
add(num,num2)

#Exercise 4 — Function That Returns a Value
#Write a function square(num) that returns the square of the number.
#Print the returned value.
def square(num):
    return num * num
num = int(input("Enter a number: "))
answer = square(num) 
print(answer)

#Exercise 5 — Multiple Steps Inside a Function
#Write a function user_profile(name, age) that prints a formatted message like:
#Name: <name>, Age: <age>
#Then call this function using user input.
def user_profile(name,age):
    print(f"name:{name}, age: {age}")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
user_profile(name,age)

#Exercise 6 — Function That Uses an If Statement
#Write a function check_age(age):
#If age ≥ 18 → print “Adult”
#Else → print “Minor”
#Call the function.
def check_age(age):
    if age >= 18 :
        print("Adult")
    else:
        print("Minor")
age = int(input("Enter your age: "))
check_age(age)

#Exercise 7 — Function that Returns Instead of Prints
#Write a function bmi(weight, height) that returns the BMI value.
#Print the result outside the function.
def bmi(weight,height):
    bmi_value = weight / (height ** 2)
    return bmi_value
weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meters: "))
bmi_result = bmi(weight,height)
print(f"The BMI value is {bmi_result}")

#Exercise 8 — Function With Defaults
#Write a function:
#def greet_user(name="Guest"):
#And print:
#Hello <name>
#Call it with a name AND without a name
def greet_user(name="Guest"):
    print(f"Hello {name}")
greet_user("Melvin")
greet_user()

#Exercise 9 — Function Calling Another Function
#Write:
#a function multiply(a, b) that returns the product
#another function show_result() that calls multiply and prints the result
def multiply(a,b):
    return a * b 
def show_result():
    a = int(input("Enter a number: "))
    b = int(input("Enter second number: "))
    answer = multiply(a,b)
    print(f"the result is {answer}")
show_result()

#Exercise 10 — Clean Up User Input (Using Function)
#Write a function clean_text(text) that:
#strips spaces
#converts to lowercase
#returns the cleaned value
#Ask the user for a word, clean it using the function, and print the result
def clean_text(text):
    cleaned_value = text.strip().lower()
    return cleaned_value
word = input("Enter a word: ")
result = clean_text(word)
print(result)

