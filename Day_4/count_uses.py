#Question
#Ask the user to enter numbers until -1.
#Count only positive numbers.
count = 0
number = 0
while number != -1:
    number = int(input("Enter a number (-1 to stop): "))
    if number > 0 :
        count += 1
print("Positive numbers are :", count)

#QUESTION 2 — Count Even Positive Numbers
#Ask the user to enter numbers until -1.
#Count only positive even numbers.
#Hint
#Use % (modulo)
count = 0
number = 0
while number != -1 :
    number = int(input("Enter a number (-1 to stop): "))
    if number > 0 and number % 2 == 0 :
        count += 1
print("Even positive numbers entered:", count)

#QUESTION 3 — Count Numbers Greater Than 10
#Ask the user to enter numbers until -1.
#Count how many numbers are greater than 10.
count = 0
number = 0
while number != -1 :
    number = int(input("Enter a number (-1 to stop): "))
    if number > 10 :
        count += 1
print("Numbers greater than ten entered:", count)


#QUESTION 4 — Count Valid Scores
#Ask the user to enter exam scores until -1.
#Count how many scores are valid.
#Valid score rules
#Between 0 and 100 (inclusive)
#Ignore negatives (except -1)
count = 0
exam_scores = 0
while exam_scores != -1:
    exam_scores = int(input("Enter your score (-1 to stop): "))
    if exam_scores >= 0 and exam_scores <= 100 :
        count += 1 
print("Valid scores entered:", count)

#QUESTION 5 — Count Correct Password Attempts
#Ask the user to enter a password until they type "exit".
#Count how many times the user enters the correct password.
#Rules
#Correct password is "python123"
#Do not count "exit"
correct_password = "python123"
count = 0
password = ""
while password != "exit" :
    password = input("Enter a password (type exit to stop): ")
    if password == correct_password :
        count += 1
print("correct password entered:", count)

