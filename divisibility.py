numerator = int(input("Enter a number as numerator: "))
denominator = int(input("Enter a number as denominator: "))
if numerator % denominator == 0:
    print(f"{numerator} is divisible by {denominator}")
else:
    print(f"{numerator} is not divisible by {denominator}")
