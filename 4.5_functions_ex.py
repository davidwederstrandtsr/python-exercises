#!/usr/bin/env python
# coding: utf-8

# In[8]:


vowels = ['a', 'e', 'i', 'o', 'u']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']


# In[ ]:


# 1. Define a function named is_two. It should accept one input and return True if the passed input is 
#	 either the number or the string 2, False otherwise.
def is_two(num):
	return num == 2 or num == "2"

print(is_two(2))
print(is_two('2'))
print(is_two(3))


# In[ ]:


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(ch):
    if str(ch).isdigit():
        return False
    ch = ch.lower()
    return ch in vowels


# In[ ]:


print(is_vowel('a'))
print(is_vowel('A'))
print(is_vowel('b'))


# In[ ]:


assert is_vowel('c') == False
assert is_vowel('a') == True

# nothing will display if the assertions are correct


# In[9]:


# 3. Define a function named is_consonant. 
#	 It should return True if the passed string is a consonant, False otherwise. 
#	 Use your is_vowel function to accomplish this.
def is_consonant(ch):
    if str(ch).isdigit():
        return False
    ch = ch.lower()

    return ch in consonant
# return ch.isalpha() and not in vowels

print(is_consonant('D'))
print(is_consonant('a'))


# In[10]:


"c".isalpha()


# In[ ]:


assert 


# In[13]:


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


# In[14]:


def c_word(word):
    first_letter = word[0]
    if is_consonant(first_letter):
        return word.capitalize()
    else:
        return word


# In[15]:


cap_word1 = capitilize_word("david")
cap_word2 = capitilize_word("anthony")
cap_word3 = cap_word("david")
cap_word4 = cap_word("anthony")
cap_word5 = c_word("ant")
cap_word6 = c_word("bant")


# In[16]:


print(cap_word1)
print(cap_word2)
print(cap_word3)
print(cap_word4)
print(cap_word5)
print(cap_word6)


# In[1]:


# 5. Define a function named calculate_tip. 
#	 It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(percent, bill):
    if percent > 0:
        percent = percent / 100.0
    while (percent < 0 or percent > 1):
        print("The percentage for tip needs to be between 0 and 100")
        percent = int(input("Enter a tip between 0 and 100: "))
    tip = bill * percent

    return bill + tip

# 5 putput
percent = int(input("Enter a tip between 0 and 100: "))
bill = int(input("Enter the bill amount $"))
bill_including_tip = calculate_tip(percent, bill)
print(f"Your nill before including tip is ${bill}")
print(f"Your bill after including tip is ${bill_including_tip}")


# In[2]:


# 6. Define a function named apply_discount. 
#	 It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def calculate_discount(percent, bill):
    if percent > 0:
        percent = percent / 100.0
    while percent < 0 or percent > 1:
        print("The percentage for discount needs to be between 0 and 100")
        percent = int(input("Enter a discount between 0 and 100: "))
        if percent > 0:
            percent = percent / 100.0
    discount = bill * percent
    return bill - discount

# 6 output
percent = int(input("Enter a discount between 0 and 100: "))
bill = int(input("Enter the bill amount $"))
bill_after_discount = calculate_discount(percent, bill)
print(f"Your bill after discount is ${bill_after_discount}")


# In[25]:


# 7. Define a function named handle_commas. 
#	 It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(number):
    new = number.replace(',','')
    return int(new)


# In[26]:


assert handle_commas("1,234") == 1234
assert handle_commas("1,234,567,890") == 1234567890


# In[27]:


print(handle_commas('1,000'))


# In[29]:


# 8. Define a function named get_letter_grade. 
#	 It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(number):
	while (str(number).isdigit() == False
		or number < 0 or number > 100):
		print("The entered number is not valid.")
		number = input("Enter a numerical grade: ")

	if number >= 90:
		grade = 'A'
	elif number >= 80:
		grade = 'B'
	elif number >= 70:
		grade = 'C'
	elif number >= 60:
		grade = 'D'
	else:
		grade = 'F'

	return grade

letter_grade = get_letter_grade(87)
print(letter_grade)
print()


# In[30]:


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(word):
    new_string = ''
    for w in word:
        l = w.lower()
        if w not in vowels and l not in vowels:
            new_string += w
        else:
            continue
    return new_string

word_minus_vowels = remove_vowels('MississippI')
print(word_minus_vowels)

print()

# ''.join([c for c in word if not is_vowel(c)])


# In[32]:


def remove_vowels2(string):
    return ''.join([c for c in string if not is_vowel(c)])


# In[33]:


# assert remove vowels
assert remove_vowels('a') == ''
assert remove_vowels('ab') == 'b'
assert remove_vowels('daa') == 'd'
assert remove_vowels('dad') == 'dd'
assert remove_vowels('aaa') == ''
assert remove_vowels('asasasa') == 'sss'


# In[40]:


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

def normalize_name(name):
    new_name = ''
    name = name.lower().strip()
    name = name.replace(' ','_')
    
    for n in name:
        if n in vowels or n in consonant or n == '_':
            new_name += n
        else:
            continue         
   
    return new_name


# In[41]:


fixed_name = normalize_name('0 Da vid')
print(fixed_name)
print()


# In[42]:


# 10 redone
# 10 helper function
def remove_special_character(string):
    return ''.join([c for c in string if c.isalnum() or c == ' '])


# In[43]:


remove_special_character("a!@#$#@%$#$%^^b")


# In[44]:


def norm_name(string):
    without_special_chars = remove_special_character(string)
    return without_special_chars.lower().strip().replace(' ', '_')


# In[45]:


norm_name('0 Da vid')


# In[46]:


# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative 
#	  sum of the numbers in the list.
# 		- cumsum([1, 1, 1]) returns [1, 2, 3]
# 		- cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumsum(num_list):
    new_list = []
    temp = 0
    for n in num_list:
        new_list.append(n + temp)
        temp += n
    return new_list

list1 = cumsum([1, 1, 1])
list2 = cumsum([1, 2, 3])
print(list1)
print(list2)

print()


# In[47]:


# Bonus
# Create a function named twelveto24. 
#   It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation 
#   of the time in a 24-hour format. Bonus write a function that does the opposite.


def twelveto24(time_to_convert):
    hour = []
    minutes = ''
    ampm = ''
    parts = time_to_convert.split(':')
    hour = parts[0]
    temp = parts[1]
    for t in temp:
        if t.isdigit():
            minutes += t
        else:
            ampm += t

    if ampm == 'pm':
        hour = int(hour) + 12

    time_converted = str(hour) + ':' + minutes
    return time_converted


# In[48]:


print(twelveto24('11:23am'))
print(twelveto24('11:23pm'))


# In[ ]:


# Create a function named col_index. 
#.  It should accept a spreadsheet column name, and return the index number of the column.
# 		- col_index('A') returns 1
# 		- col_index('B') returns 2
# 		- col_index('AA') returns 27

def col_index(col_name):
    num = 0
    for i in col_name:
        num = num * 26 + 1 + ord(i) - ord('A')
    return num


# In[ ]:


col_index('A')


# In[ ]:


col_index('AA')


# In[ ]:




