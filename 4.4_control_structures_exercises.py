# 1. Conditional Basics
import string

# a. prompt the user for a day of the week, print out whether the day is Monday or not

# day_of_the_week = input("Please enter the day of the week: ")
day_of_the_week = "Monday"
if day_of_the_week.title() == "Monday":
	print("It is Monday!")
else:
	print("It is not Monday")
print("********")

# 	b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Firday", "monday", "tuesday", "wednesday", "thursday", "friday"]
weekend = ["Saturday", "Sunday", "saturday", "sunday"]
# answer2 = input("Enter a day of the week: ")
answer2 = "saturday"

if answer2.title() in weekday:
	print("Aw, it a weekday")
elif answer2.title() in weekend:
	print("Yeah, its the weekend")


# 	c. create variables and make up values for
print("Paycheck")
# 		- the number of hours worked in one week
week_hours_worked = 60
time_and_half = 1.5
normal_hours = 40
# 		- the hourly rate
hourly_rate = 35
# 		- how much the week's paycheck will be
week_paycheck = normal_hours * hourly_rate

# 		- write the python code that calculates the weekly paycheck. 
#		  You get paid time and a half if you work more than 40 hours
overtime = week_hours_worked - normal_hours

overtime_pay = hourly_rate * time_and_half * overtime

take_home = week_paycheck + overtime_pay
print(f"For {week_hours_worked} hours, at {time_and_half} for overtime")
print(f"Employee earned ${week_paycheck} regular time, ${overtime_pay} overtime")
print(f"for total take home of ${take_home}")


# 2. Loop Basics

# 	a. While
print("********")
print("WHILE LOOPS")
print("********")
# 		- Create an integer variable i with a value of 5.
i = 5
# 		- Create a while loop that runs so long as i is less than or equal to 15
while i <= 15:
	print(i)
	i += 1
print("****")

# 		- Each loop iteration, output the current value of i, then increment i by one.
#		- Create a while loop that will count by 2's starting with 0 and ending at 100. 
k = 0
j = 2
n = 100

while k <= n:
	print(k)
	k += j
# 			Follow each number with a new line.
# 		- Alter your loop to count backwards by 5's from 100 to -10.
print("****")

while n > -10:
	print(n)
	n -= i

# 		- Create a while loop that starts at 2, and displays the number squared on each 
#			line while the number is less than 1,000,000.
print("****")
while j < 1000000:
	print(j)
	j **= 2

print()

# Write a loop that uses print to create the output shown below.
i = 100
j = 5

while i > 0:
	print(i)
	i -= j
print("End of While Loop")

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

print()
print("FOR LOOP")
# num = input("Enter a integer: ")

num = 7
for n in range(1, 11):
	answer = int(num) * n
	print(f"{num} * {n} = {answer}")

# ii. Create a for loop that uses print to create the output shown below.

for i in range(1, 10):
	n = str(i)
	print(n * i)

# C. break and continue
# i. Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered.

# num = int(input("enter an odd integer between 1 and 50: "))
num = 21

while num % 2 != 0:
	if str(num).isdigit() == True and num >= 1 and num <= 50:
		break;
	else:
		num = input("enter an odd integer between 1 and 50: ")

print(num)

for n in range(1, 50):
	if n % 2 != 0:
		if n == num:
			continue
		else:
			print(n)
		
# D. The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the 
# input function returns a string, so you'll need to convert this to a numeric type.)

# num = int(input("Enter a positive number: "))
num = 17

while num < 1:
	print("You entered a non-positive number")
	num = int(input("Enter a positive number: "))

for n in range(0, num + 1):
	print(n)

# Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.

# Enter a positive integer

# num = int(input("Enter a positive number: "))

num = 33
while num < 1:
	print("You entered a non-positive number")
	num = int(input("Enter a positive number: "))

while num >= 1:
	print(num)
	num -= 1


# 3. Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1, 100):
	if i % 3 == 0 and i % 5 != 0:
		print(f"{i} Fizz")
	elif i % 5 == 0 and i % 3 != 0:
		print(f"{i} Buzz")
	else:
		print(f"{i} Fizz Buzz")



# 5. Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

# user_input = int(input("What number would you like to go to? "))

user_input = 3000
print()
print("Here is your table!")
print()

print("number | squared | cubed")
print("------ | ------- | -----")

for n in range(1, user_input):
	n_sq = n ** 2
	n_cube = n ** 3
	print("{:<7}|{:<9}|{:<12}".format(n, n_sq, n_cube))

# # Bonus: Research python's format string specifiers to align the table


# # 5. Convert given number grades into letter grades.

# # 	- Prompt the user for a numerical grade from 0 to 100.
# # 	- Display the corresponding letter grade.
# # 	- Prompt the user to continue.
# # 	- Assume that the user will enter valid integers for the grades.
# # 	- The application should only continue if the user agrees to.
# # 	- Grade Ranges:

# # 		A : 100 - 88
# # 		B : 87 - 80
# # 		C : 79 - 67
# # 		D : 66 - 60
# # 		F : 59 - 0

print()
print()
print("BONUS - GRADES")
submit = True

while submit == True :
	grade_input = float(input("Enter a integer grade: "))	
	score = int(grade_input)
	grade = ''
	if score >= 88:
		grade = 'A'
	elif score >= 80:
		grade = 'B'
	elif score >= 67:
		grade = 'C'
	elif score >= 60:
		grade ='D'
	else:
		grade = 'F'

	
	correct = input(f"Is {grade} correct? (y/n) ")
	if correct == 'y':
		print(f"A number score of {score} is a {grade}")
	else:
		submit = True

	score_again = input("Enter another numberical grade? (y/n) ")
	if score_again == 'n':
		break;

print("This is the end of the grade bonus")






print()
print()
print("BONUS - GRADES")
submit = True

while submit == True :
	grade_input = float(input("Enter a integer grade: "))	
	score = int(grade_input)
	grade = ''

	if score >= 99:
		grade = "A+"
	elif score >= 95:
		grade = "A"
	elif score >= 90:
		grade = "A-"
	elif score >= 89:
		grade = "B+"
	elif score >= 85:
		grade = "B"
	elif score >= 80:
		grade = "B-"
	elif score >= 79:
		grade = "C+"
	elif score >= 75:
		grade = "C"
	elif score >= 70:
		grade = "C-"
	elif score >= 69:
		grade = "D+"
	elif score >= 65:
		grade = "D"
	elif score >= 60:
		grade = "D-"
	else:
		grade = 'F'

	
	correct = input(f"Is {grade} correct? (y/n) ")
	if correct == 'y':
		print(f"A number score of {score} is a {grade}")
	else:
		submit = True

	score_again = input("Enter another numberical grade? (y/n) ")
	if score_again == 'n':
		break;

print("This is the end of the extra grade bonus")















