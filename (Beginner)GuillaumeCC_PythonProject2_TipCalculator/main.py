# Project 2: Tip Calculator
# Guillaume CC, aka TheFirewallDragon

print("Welcome to My Tip Calculator.")

bill = float(input("What was the total bill amount?\n$:"))
tip = int(input("How much tip would you like to give?\nPercent:"))
split = int(input("How many people to split the bill?\nPeople:"))

total = ("{:.2f}".format((((bill * (tip / 100)) + bill) / split)))

print(f"Each person should pay: ${total}")