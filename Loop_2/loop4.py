print("Enter numbers to sum. Enter -1 to stop.")
total = 0
count = 0
while True:
    num = int(input("Number: "))
    if num == -1: # Sentinel value
        break
    total += num
    count += 1
if count > 0:
    print(f"Sum: {total}, Average: {total / count:.2f}")
else:
    print("No numbers entered.")