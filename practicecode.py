colors = ["red" , "blue"]
sizes = ["S" , "M" , "L"]

for color in colors:
    for size in sizes:
        print(f"{color}{size}" , end=" ")
    print()

accumulator = 0
scores = [85, 92, 78, 95, 88]
count = 0
for score in scores:
    accumulator += score
    count += 1
print(f"{accumulator / count:.2f}")