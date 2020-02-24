def calculate_tip(percent, bill):
    while (percent < 0 or percent > 1):
        print("The percentage for tip needs to be between 0 and 1")
        percent = input("Enter a tip between 0 and 1: (0.15 for 15%)")
    tip = bill * percent
    return bill + tip


total_bill = calculate_tip(0.15, 100)
print(total_bill)

