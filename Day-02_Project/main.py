                # TIP CALCULATOR
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
percTip = (tip / 100) * bill
totalBill = percTip + bill
countAll =   totalBill / people
print(f'EACH PERSON SHOULD PAY: {countAll: .2f}')