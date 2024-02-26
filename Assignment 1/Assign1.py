# Daniel Park
# Home Power Consumption Calculator
x = False

# Loop
while not x:
    offpeak = float(input("Enter kwh during Off Peak period: "))
# Loop to break if typed 0
    if offpeak == 0:
        x = True
        if x == True:
           break
# Inputs
    onpeak = float(input("Enter kwh during On Peak period: "))
    midpeak = float(input("Enter kwh during Mid Peak period: "))
    senior = input("Is owner senior? (y,n): ")

    rateoffpeak = float(offpeak) * 0.085
    ratepeak = float(onpeak) * 0.176
    ratemidpeak = float(midpeak) * 0.119
    total = rateoffpeak + ratepeak + ratemidpeak
# Total Usage Discount
    if (float(offpeak) + float(onpeak) + float(midpeak)) < 400:
        total = total * 0.96
#On Peak Discount
    elif float(onpeak) < 150:
        ratepeak = ratepeak * 0.95
        total = rateoffpeak + ratepeak + ratemidpeak
# Senior Discount
    if senior == "y":
        total = total * 0.89

    if senior == "Y":
        total = total * 0.89
# Applying Tax
    total = total * 1.13
    total = round(total , 2)
# Final Cost
    print("Electricity cost: $" + str(total))
    print()
