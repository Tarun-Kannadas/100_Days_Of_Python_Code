print("Welcome to the tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12 or 15?"))
people = int(input("How many people to split the bill?"))

bill_with_tip = tip / 100 * bill + bill

print(f"Everyone has to pay is {bill_with_tip/people}")