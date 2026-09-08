name = input("Enter your name: ")

maths = int(input("Enter Maths marks: "))
physics = int(input("Enter Physics marks: "))
python = int(input("Enter Python marks: "))
english = int(input("Enter English marks: "))
electronics = int(input("Enter Electronics marks: "))

total = maths + physics + python + english + electronics
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- RESULT -----")
print("Name:", name)
print("Total:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)

if percentage >= 40:
    print("Result: PASS 🎉")
else:
    print("Result: FAIL")
