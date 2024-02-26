# Basic Code
def BasicCode(digits):
    digits1 = sum(map(int, str(digits)[:-1]))

    # modulo 10 finding remainder
    rem = digits1 % 10

    # Check if it is true
    if rem == int(str(digits)[len(str(digits)) - 1]):
        print("--code:", digits, "valid Basic code.")
        return True
    else:
        return False


# Positional Code
def PositionalCode(digits):
    digits1 = 0

    for index, integer in enumerate(str(digits)[:-1], 1):
        digits1 += (index * int(integer))

    # modulo 10 finding remainder
    rem = digits1 % 10

    # Check if it is true
    if rem == int(str(digits)[len(str(digits)) - 1]):
        print("--code:", digits, "valid Position code.")
        return True
    else:
        return False


# Universal Product Code
def UniversalProductCode(digits):
    digits1 = 0

    for index, integer in enumerate(str(digits)[:-1], 1):
        if index % 2 == 0:
            digits1 += int(integer) * 1
        else:
            digits1 += int(integer) * 3

    # modulo 10 finding remainder
    rem = digits1 % 10

    # last digit calculations
    if 0 < rem <= 9:
        rem = 10 - rem

    # Check if it is true
    if rem == int(str(digits)[len(str(digits)) - 1]):
        print("--code:", digits, "valid UPC code.")
        return True
    else:
        return False
