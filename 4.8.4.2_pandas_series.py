#!/usr/bin/env python
# coding: utf-8

import pandas as pd

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

# ## 1 Use pandas to create a Series from the following data:
# 
# ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

vowels = list('aeiou')

# ##### a. Name the variable that holds the series fruits.

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", 
          "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# ##### b. Run .describe() on the series to see what describe returns for a series of strings.

fruits.describe()

# ##### c. Run the code necessary to produce only the unique fruit names.

fruits.unique()

# ##### d. Determine how many times each value occurs in the series.

fruit_name_count = fruits.value_counts()
fruit_name_count

# ##### e. Determine the most frequently occurring fruit name from the series.

most_frequent_fruit = fruit_name_count.head(1)
most_frequent_fruit

# ##### f. Determine the least frequently occurring fruit name from the series.

least_frequent_fruit = fruit_name_count.tail(1)
least_frequent_fruit

# ##### g. Write the code to get the longest string from the fruits series.

longest_fruit_name = fruits[fruits.str.len() == fruits.str.len().max()]
longest_fruit_name

# ##### h. Find the fruit(s) with 5 or more letters in the name.

fruits_with_five_or_more = fruits[fruits.str.len() >= 5]
fruits_with_five_or_more

# ##### i. Capitalize all the fruit strings in the series.

capitalize_fruit_names = fruits.str.capitalize()
capitalize_fruit_names

# ##### j. Count the letter "a" in all the fruits (use string vectorization)

a_count = fruits.str.count('a').sum()
a_count

# ##### k. Output the number of vowels in each and every fruit.

fruits.str.count(r'[aeiou]')

# ##### l. Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

fruits[fruits.apply(lambda s: s.count('o') > 1)]

# ##### m. Write the code to get only the fruits containing "berry" in the name

fruits[fruits.str.contains('berry')]

# ##### n. Write the code to get only the fruits containing "apple" in the name

fruits[fruits.str.contains('apple')]

# ##### o. Which fruit has the highest amount of vowels?

longest_fruit_name = fruits[fruits.str.count(r'[aeiou]') == fruits.str.count(r'[aeiou]').max()]
longest_fruit_name

# ### 3. Use pandas to create a Series from the following data:

dollar_amounts = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', 
                            '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', 
                            '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', 
                            '$452,650.23'])

# - What is the data type of the series?

type(dollar_amounts)
# pandas.core.series.Series

# - Use series operations to convert the series to a numeric data type.

new_dollar_amounts = dollar_amounts.str.replace('$','').str.replace(',','').astype(float)
new_dollar_amounts

# - What is the maximum value? The minimum?

new_dollar_amounts.max()

new_dollar_amounts.min()


# - Bin the data into 4 equally sized intervals and show how many values fall into each bin.

pd.cut(new_dollar_amounts, 4).value_counts()

# - Plot a histogram of the data. Be sure to include a title and axis labels.

new_dollar_amounts.plot.hist()
plt.title("Dollar Amount by Range")
plt.xlabel("Dollar Amount")
plt.show()

# ### 4. Use pandas to create a Series from the following exam scores:

exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
type(exam_scores)

# - What is the minimum exam score? The max, mean, median?

exam_scores.agg(['min', 'max' ,'mean', 'median'])

# - Plot a histogram of the scores.

exam_scores.plot.hist()

# - Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.

def score_to_letter_grade(num):
    if num >= 90:
        letter = 'A'
    elif num >= 80:
        letter = 'B'
    elif num >= 70:
        letter = 'C'
    elif num >= 60:
        letter = 'D'
    else:
        letter = 'F'
    return letter


letter_grade = exam_scores.apply(score_to_letter_grade)
letter_grade


# - Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, 
#   and that many points should be given to every other score as well.

curve_points = 100 - exam_scores.max()
curve_points

def curve_grades(score):
    return score + curve_points

curved_grades = exam_scores.apply(curve_grades)
curved_grades

# ### 5. Use pandas to create a Series from the following string:

letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))
letters

# #### What is the most frequently occuring letter? 

letters.value_counts().head(1)

# Least frequently occuring?

letters.value_counts().tail(1)

# #### How many vowels are in the list?

letters[letters.isin(vowels)].size

# #### How many consonants are in the list?

letters[~ letters.isin(vowels)].size

# #### Create a series that has all of the same letters, but uppercased

letters.str.upper()

# #### Create a bar plot of the frequencies of the 6 most frequently occuring letters.

six_most_freq = letters.value_counts().head(6)
six_most_freq

six_most_freq.plot.bar()
plt.title("Six Most Frequent Letters")
plt.xticks(rotation=0)
plt.ylabel("Letter Frequency")
plt.xlabel("Letters")
plt.show()