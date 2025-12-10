#1️⃣ Check for None
#Ask the user to input a value.
#If the input is empty (use None), print "No input provided"
#Else print "Input received"
value = "none"
user = input("Enter a value: ")
if user is value :
    print("No input provided")
else:
    print("Input received.")

#2️⃣ Compare Two Lists
#Create two lists with the same values: [10, 20, 30]
#Check if they are the same object using is
#Print "Same object" or "Different objects"
num_1 = [10, 20, 30]
num_2 = [10, 20, 30]
if num_1 is num_2 :
    print("Same objects")
else:
    print("Different objects")

#3️⃣ Assign and Compare
#Create a list a = [5, 6, 7]
#Assign b = a
#Use is to check if a and b point to the same object, print a message if they are
a = [5, 6, 7]
b = a
if b is a :
    print("objects are the same")

#4️⃣ Using is not
#Create two separate strings: str1 = "hello", str2 = "hello"
#Check if they are not the same object using is not
#Print "Different objects" if they aren’t the same
str1 = "hello"
str2 = "".join(["h", "e", "l", "l", "o"])
if str2 is not str1 :
    print("Different objects")
else :
    print("Same objects")

#5️⃣ Identity vs Equality
#Create two variables: x = 1000, y = 1000
#Print the result of x == y and x is y
#Observe the difference and explain why it happens
x = [1000]
y = [1000]

print(x == y)
print(x is y )


