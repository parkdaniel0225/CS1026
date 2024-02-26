# CompSci 1026A 2nd Assignment
# Name: Daniel Park
# Codes
# importing Codes
from code_check import BasicCode
from code_check import PositionalCode
from code_check import UniversalProductCode

digits = input("Please enter code (digits only) (enter 0 to quit): ")

basic = []
positional = []
universalproduct = []
none = []

# Loop
while digits != "0":
    none_digits = True
    if digits == "0":
        break
    if BasicCode(digits):
        basic.append(digits)
        none_digits = False
    if PositionalCode(digits):
        positional.append(digits)
        none_digits = False
    if UniversalProductCode(digits):
        universalproduct.append(digits)
        none_digits = False
    if none_digits:
        none.append(digits)
        print("--code:", digits, "not Basic, Position or UPC code.")

    digits = input("Please enter code (digits only) (enter 0 to quit): ")

print("Summary")
print("Basic :", ', '.join(basic) if basic else 'None')
print("Position :", ', '.join(positional) if positional else 'None')
print("UPC :", ', '.join(universalproduct) if universalproduct else 'None')
print("None :", ', '.join(none) if none else 'None')
