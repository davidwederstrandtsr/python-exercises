vowels = ['a', 'e', 'i', 'o', 'u']

# 1. Define a function named is_two. It should accept one input and return True if the passed input is 
#	 either the number or the string 2, False otherwise.
def is_two(num):
	return num == 2 or num == "2"


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(ch):
    if str(ch).isdigit():
        return False
    ch = ch.lower()
    return ch in vowels

# 3. Define a function named is_consonant. 
#	 It should return True if the passed string is a consonant, False otherwise. 
#	 Use your is_vowel function to accomplish this.
def is_consonant(ch):
    if str(ch).isdigit():
        return False
    ch = ch.lower()
    return ch not in vowels

# 4. Define a function that accepts a string that is a word. 
#	 The function should capitalize the first letter of the word if the word starts with a consonant.
def capitilize_word(word):
    ch = word[0]
    if is_consonant(ch):
        return word.title()
    else:
        return word

# or

def cap_word(word):
	if str(word).isdigit():
		return word
	ch = word[0]
	if ch not in ['a', 'e', 'i', 'o', 'u']:
		return word.title()
	else:
		return word


# 5. Define a function named calculate_tip. 
#	 It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(percent, bill):
    while (percent < 0 or percent > 1):
        print("The percentage for tip needs to be between 0 and 1")
        percent = input("Enter a tip between 0 and 1: (0.15 for 15%)")
    tip = bill * percent
    return bill + tip

# 6. Define a function named apply_discount. 
#	 It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def calculate_discount(percent, bill):
    while (percent < 0 or percent > 1):
        print("The percentage for discount needs to be between 0 and 1")
        percent = input("Enter a discount between 0 and 1: (0.15 for 15%)")
    discount = bill * percent
    return bill - discount

# 7. Define a function named handle_commas. 
#	 It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(number):
    new = number.replace(',','')
    return new


# 8. Define a function named get_letter_grade. 
#	 It should accept a number and return the letter grade associated with that number (A-F).

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# 10. Define a function named normalize_name. 
#	  It should accept a string and return a valid python identifier, that is:
# 		- anything that is not a valid python identifier should be removed
# 		- leading and trailing whitespace should be removed
# 		- everything should be lowercase
# 		- spaces should be replaced with underscores
# 		- for example:
# 			~ Name will become name
# 			~ First Name will become first_name
# 			~ % Completed will become completed

# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative 
#	  sum of the numbers in the list.
# 		- cumsum([1, 1, 1]) returns [1, 2, 3]
# 		- cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# Bonus
# Create a function named twelveto24. 
#   It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation 
#   of the time in a 24-hour format. Bonus write a function that does the opposite.


# Create a function named col_index. 
#.  It should accept a spreadsheet column name, and return the index number of the column.
# 		- col_index('A') returns 1
# 		- col_index('B') returns 2
# 		- col_index('AA') returns 27










