digits = "0123456789ABCDEF"

number = input("Въведи число: ").upper()
from_system = int(input("От система (2, 8, 10 или 16): "))
to_system = int(input("Към система (2, 8, 10 или 16): "))

if from_system not in (2, 8, 10, 16) or to_system not in (2, 8, 10, 16):
    print("Невалидна система!")
else:

    total = 0

    if from_system == 10:
        total = int(number)

    else:
        for digit in number:
            value = digits.index(digit)
            total = total * from_system + value

    if to_system == 10:
        result = str(total)

    elif total == 0:
        result = "0"

    else:
        result = ""

        while total > 0:
            remainder = total % to_system
            result = digits[remainder] + result
            total = total // to_system

    print("Резултат:", result)