#!/usr/bin/env python
# coding: utf-8
# %%

# %%
import pandas as pd
import numpy as np
from pydataset import data


# %%


np.random.seed(123)


# %%


students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']


# %%


# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))


# #### create the dataframe

# %%


df = pd.DataFrame(
    {
        'name': students,
        'math': math_grades,
        'english': english_grades,
        'reading': reading_grades
    })


# %%


df.describe()


# ## 1. Copy the code from the lesson to create a dataframe full of student grades.

# %%


student_grades = df.copy()
student_grades


# - Create a column named passing_english that indicates whether each student has a passing grade in reading.

# %%


student_grades['passing_english'] = student_grades.english > 70

student_grades


# - Sort the english grades by the passing_english column. How are duplicates handled?

# %%


student_grades.sort_values(by="passing_english")


# - Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)

# %%


student_grades.sort_values(by=['passing_english', 'name'])


# - Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.

# %%


student_grades.sort_values(by=['passing_english', 'english'])


# - Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.

# %%


student_grades["overall_grade"] = (student_grades.math + student_grades.english + student_grades.reading) / 3
student_grades


# ## 2. Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

# %%


data('mpg', show_doc=True) # view the documentation for the dataset


# %%


mpg = data('mpg')
mpg


# - How many rows and columns are there?

# %%


mpg.shape


# - What are the data types of each column?

# %%


mpg.dtypes


# - Summarize the dataframe with .info and .describe

# %%


mpg.info()


# %%


mpg.describe()


# - Rename the cty column to city.

# %%


mpg = mpg.rename(columns={'cty': 'city'})
mpg


# - Rename the hwy column to highway.

# %%


mpg = mpg.rename(columns={'hwy':'highway'})
mpg


# - Do any cars have better city mileage than highway mileage?

# %%


mpg[mpg.city > mpg.highway]


# - Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.

# %%


mpg["milage_difference"] = mpg.highway - mpg.city
mpg


# - Which car (or cars) has the highest mileage difference?

# %%


mpg.nlargest(n=1, columns='milage_difference', keep='all')


# - Which compact class car has the lowest highway mileage? The best?

# %%


mpg[mpg['class'] == ('compact')].nsmallest(n=1, columns="highway", keep="all")


# %%


mpg.nlargest(n=1, columns="highway", keep="all")


# - Create a column named average_mileage that is the mean of the city and highway mileage.

# %%


mpg['average_milage'] = (mpg.city + mpg.highway) / 2
mpg


# - Which dodge car has the best average mileage? The worst?

# %%


mpg[mpg['manufacturer'] == ('dodge')].nlargest(n=1, columns="average_milage", keep="all")


# %%


mpg[mpg['manufacturer'] == ('dodge')].nsmallest(n=1, columns="average_milage", keep="all")


# ## 3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

# %%


Mammals = data('Mammals')


# - How many rows and columns are there?

# %%


Mammals.shape


# - What are the data types?

# %%


Mammals.dtypes


# - Summarize the dataframe with .info and .describe

# %%


Mammals.info()


# %%


Mammals.describe()


# - What is the the weight of the fastest animal?

# %%


Mammals.sort_values(by='speed', ascending=False).head(1).weight


# - What is the overal percentage of specials?

# %%


Mammals['specials'].sum() / len(Mammals.index) * 100


# - How many animals are hoppers that are above the median speed? What percentage is this?

# %%


Mammals.head(4)
median_speed = Mammals['speed'].median()


# %%


fastest = Mammals[(Mammals['hoppers'] == (True)) & (Mammals['speed'] > median_speed)]
len(fastest)


# %%


len(fastest) / len(Mammals) * 100

