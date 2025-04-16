a = int(input("Enter value a: "))
b = int(input("Enter value b: "))
c = int(input("Enter value c: "))

print(f"Before swapping a = {a}, b = {b}, c = {c}")

a, b, c = b, c, a

print("After swapping a=", a, "b=", b, "c=", c)
