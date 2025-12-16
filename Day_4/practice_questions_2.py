#⿡Skip Numbers
#Print numbers from 1 to 10, but skip 5.
number = 1
while number <= 10:
    if number == 5:
        number += 1
    print(number)
    number += 1

#Count Even Numbers
#Print only even numbers from 1 to 20 using a while loop.
number = 1
while number <= 20 :
    if number % 2 != 0:
        number += 1
    print(number)
    number += 1

#⿣ Stop at a Number
#Ask the user for a number.
#Keep counting from 1 upward until you reach that number.
#📌 Example input: 7
#📌 Output: 1 2 3 4 5 6 7
num = int(input("Enter a number: "))
count = 1
while count <= num:
    print(count)
    count += 1 

#4️⃣ Sum of Numbers
#Ask the user for a number n.
#Use a while loop to calculate the sum from 1 to n.
#Example:
#Input: 5
#Output: 15
number = int(input("Enter a number: "))
count = 1
total = 0
while count <= number:
    total += count
    count += 1 
print("Sum:", total )

#Countdown with Message
#Count down from 5 to 1, then print:
#Boom!🚀
#IMPORTANT RULE
#Do not use for loops
#Do not use break or continue yet
number = 5
while number >= 1:
    print(number)
    number -= 1
print("Boom!")


