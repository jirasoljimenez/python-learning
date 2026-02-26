# 1. Ask the user for three integer values
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

# Chained comparison
exp1 = a < b < c
print(f"a < b < c: {exp1}")

# De Morgan's candidate
exp2 = not (a > b or b > c)
print(f"not (a > b or b > c): {exp2}")

exp3 = a <= b and b <= c
print(f"a <= b and b <= c: {exp3}")

are_equal = exp2 == exp3
print(f"\nDo expressions 2 and 3 match? {are_equal}")
print("This confirms De Morgan's Law: not (A or B) == not A and not B")

# 1. Ask the user for temperature and rain status
temp = float(input("Enter the current temperature (°F): "))
is_raining = input("Is it raining? (yes/no): ").strip().lower()

# 2. Temperature and Rain Advisory Logic
if temp > 100:
    print("EXTREME HEAT WARNING: Stay indoors!")

elif temp > 85:
    if is_raining == "yes":
        print("Warm rain — watch for flash floods.")
    else:
        print("Hot and dry — stay hydrated.")

elif 60 <= temp <= 85:
    # Using a combined Boolean expression
    if is_raining == "yes":
        print("Grab an umbrella!")
    else:
        print("Nice weather — enjoy your day!")

elif 32 <= temp <= 59:
    print("It's cold — bundle up!")

else: 
    print("FREEZE WARNING: Roads may be icy!")

# 1. Input Section
name = input("Enter the student's name: ")
score1 = float(input("Enter Exam 1 score: "))
score2 = float(input("Enter Exam 2 score: "))
score3 = float(input("Enter Exam 3 score: "))

# 2. Calculate the average
average = (score1 + score2 + score3) / 3

if average >= 90:
    letter = "A"
elif average >= 87:
    letter = "A-"
elif average >= 83:
    letter = "B+"
elif average >= 80:
    letter = "B"
elif average >= 77:
    letter = "B-"
elif average >= 73:
    letter = "C+"
elif average >= 70:
    letter = "C"
elif average >= 67:
    letter = "C-"
elif average >= 63:
    letter = "D+"
elif average >= 60:
    letter = "D"
else:
    letter = "F"

if average >= 90:
    standing = "Dean's List"
elif average >= 70:
    standing = "Good Standing"
elif average >= 60:
    standing = "Academic Probation"
else:
    standing = "Academic Suspension Warning"

# 5. Print Formatted Grade Report
print("\n" + "="*30)
print(f"GRADE REPORT: {name.upper()}")
print("="*30)
print(f"Average Score:  {average:.2f}")
print(f"Letter Grade:   {letter}")
print(f"Standing:       {standing}")
print("="*30)
