print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $ "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_amount = round(((bill * (tip_percentage / 100)) + bill) / people , 2)

print(f"Each person should pay: ${total_amount}")