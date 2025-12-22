#PRACTICE 1 (DO THIS)
#Write a function called hello
#It should print "Hello World"
#Call it once
def hello() :
    print("Hello world")
hello()

#PRACTICE 2
#Write a function called ask_age
#Ask the user for their age
#Print: "You are X years old"
def ask_age() :
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
ask_age()

#PRACTICE 3
#Create a function double
#It takes one number
#Prints the number multiplied by 2
def double(number):
    print(number * 2)
double(4)

#PRACTICE 4
#Create a function square
#Takes one number
#Returns the square
#Print the result
def square(a):
    return a * a
result = square(6)
print(result)

