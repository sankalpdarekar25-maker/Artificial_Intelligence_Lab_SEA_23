a = int(input("Enter marks of subject 1: "))
b = int(input("Enter marks of subject 2: "))
c = int(input("Enter marks of subject 3: "))
d = int(input("Enter marks of subject 4: "))
e = int(input("Enter marks of subject 5: "))

total = a + b + c + d + e
percentage = total / 5

print("Percentage =", percentage)

if percentage < 40:
    print("Fail")
elif percentage < 65:
    print("II Class")
elif percentage < 75:
    print("I Class")
else:
    print("Distinction")

program.py
Displaying program.py.
