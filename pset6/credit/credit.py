from cs50 import get_float

# // integer division
# / float division

i = get_float("Enter your paren'ts credit card number: ")

finalval = 0
firsti = i // 10
secondi = i
ilength = 0

if firsti >= 10:
    while firsti > 0:
        # add every other number*2
        tempval = (firsti % 10) * 2
        finalval += (tempval // 10 + tempval % 10)
        ilength += 1
        firsti = firsti // 100
    while secondi > 0:
        # add every other number
        finalval += secondi % 10
        ilength += 1
        secondi = secondi // 100
else:
    print("INVALID")

if finalval % 10 == 0:
    if ilength == 15:
        # if 15 numbers
        if i // 10000000000000 == 34 or i // 10000000000000 == 37:
            print("AMEX")
        else:
            print("INVALID")
    elif ilength == 16:
        # if 16 numbers
        if i // 1000000000000000 == 4:
            print("VISA")
        elif i // 100000000000000 > 50 and i // 100000000000000 < 56:
            print("MASTERCARD")
        else:
            print("INVALID")
    elif ilength == 13:
        # if 13 numbers
        if i // 1000000000000 == 4:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")
else:
    print("INVALID")