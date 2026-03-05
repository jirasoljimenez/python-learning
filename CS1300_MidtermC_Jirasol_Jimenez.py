distance = float(input("Enter distance value: "))
unit = input("Enter unit (km or mi):")

if unit == "km":
  result = (distance * 1.60934)
  print(f"{distance}km is {result:.1f}mi")

elif scale == "mi":
  result = (distance * 0.60934)
  print(f"{distance}mi is {result:.1f}km")

else:
  print("Invalid unit.")

assignments = ["Quiz 1", "Homework 1", "Lab 1", "Quiz 2", "Homework 2"]
scores = [85, 92, 78, 88, 95]

print("== Grade Book==")
print("1. Quiz 1    -85")
print("2. Homework 1   -92")
print("3. Lab 1   -78")
print("4. Quiz 2   -88")
print("5. Homework 2  -95")
(=) * 10
