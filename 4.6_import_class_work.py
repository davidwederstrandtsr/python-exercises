import functions_exercises as fe

import itertools as it
fe.is_vowel('a')

import json
from  pprint import pprint

profiles = json.load(open('profiles.json'))

profiles[0].keys()

[profile['guid'] for profile in profiles[:4]]
[profile['balance'] for profile in profiles]

pprint(profiles)



# print list of all results
[profile['isActive'] for profile in profiles]



# Save this file as profiles.json inside of your exercises directory. 
# Use the load function from the json module to open this file, 
# it will produce a list of dictionaries. Using this data, 
# write some code that calculates and outputs the following 
# information:

# Total number of users
len(profiles)
# Number of active users
len([profile for profile in profiles if profile['isActive']])
# Number of inactive users
len([profile for profile in profiles if not profile['isActive']])
# Grand total of balances for all users
[profile['balance'] for profile in profiles]

profile = profiles[0]
profile['balance']
float(profile['balance'].replace('$', '').replace(',',''))

def convert_to_float(num):
    return float(num['balance'].replace('$', '').replace(',',''))

[convert_to_float(profile) for profile in profiles]

sum([convert_to_float(profile) for profile in profiles])
# Average balance per user
balances = [convert_to_float(profile) for profile in profiles]
avg_balance = sum(balances) / len(balances)
print('The average balance in %.2f' % avg_balance)
print(f'The average balance is {avg_balance:,.2f}')
print('The average balance is {:,.2f}'.format(avg_balance))
# User with the lowest balance
user_low_balance = [min(profiles, key=convert_to_float)]
user_low_balance
# User with the highest balance
user_high_balance = [max(profiles, key=convert_to_float)]
user_high_balance
# Most common favorite fruit

# Least most common favorite fruit

# Total number of unread messages for all users
[profile['greeting'] for profile in profiles]

profile = profiles[0]
greeting = profile['greeting']
greeting
greeting.index(' unread')
greeting[greeting.index('have ') +5:]

start_index = greeting.index('have ') + 5
end_index = greeting.index(' unread')
int(greeting[start_index:end_index])


# so 
def get_n_unread_messages(profile):
    greeting = profile['greeting']
    start_index = greeting.index('have ') + 5
    end_index = greeting.index(' unread')
    return int(greeting[start_index:end_index])

sum(get_n_unread_messages(profile) for profile in profiles)


def get_n_unread()
int(''.join([c for c in greeting if c.isdigit()]))
