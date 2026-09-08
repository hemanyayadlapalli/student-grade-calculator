name = input("Enter your name: ")

maths = int(input("Enter Maths marks (0-100): "))
physics = int(input("Enter Physics marks (0-100): "))
python = int(input("Enter Python marks (0-100): "))
english = int(input("Enter English marks (0-100): "))
electronics = int(input("Enter Electronics marks (0-100): "))

marks = [maths, physics, python, english, electronics]

if any(mark < 0 or mark > 100 for mark in marks):
    print("Invalid marks! Please enter marks between 0 and 100.")
else:
    total = sum(marks)
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
        print("Result: PASS")
    else:
        print("Result: FAIL")

if percentage >= 40:
    print("Result: PASS 🎉")
else:
    print("Result: FAIL")
