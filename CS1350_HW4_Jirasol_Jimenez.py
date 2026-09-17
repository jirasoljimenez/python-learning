inventory = {"apples": 50, "bananas": 30, "oranges": 25}

for products in inventory: 
    print(products)

total = sum(inventory.values())
average = total / len(inventory)
print(f"Total inventory: {total}")

for product, total in inventory.items():
    print(f"{product}: {total}")

prices = {"laptop":999, "phone": 699, "tablet": 449, "watch": 299}

for key in sorted(prices):
    print(key)
for key in sorted(prices, key=prices.get):
    print(key, prices[key])
print(max(prices.items(),key=lambda x: x[1]))

temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}

print(f"Average: {sum(temps.values()) / len(temps):.1f}")

max_temp = max(temps.values())
min_temp = min(temps.values())

for day, temp in temps.items():
    total_temp += temp
    if temp > max_temp:
        max_temp = temp
        hottest_day: day # type: ignore
    if temp < min_temp:
        min_temp = temp
        coldest_day = day

print(f"Hottest Day: {hottest_day} with {max_temp}*F")
print(f"Coldest Day: {coldest_day} with {min_temp}*F")

avg_temp = total_temp / len(temps)


avg_temp = sum(temps.values()) / len(temps)
print(f"Average Temp: {avg_temp:.1f}")

hottest_day, max_temp = max(temps.items(), key=lambda item: item[1])
coldest_day, min_temp = min(temps.items(), key=lambda item: item[1])

print(f"Hottest Day: {hottest_day} with {max_temp}°F")
print(f"Coldest Day: {coldest_day} with {min_temp}°F")

above_count = sum(1 for temp in temps.values() if temp > avg_temp)
print(f"Days above average: {above_count}")

products = {
    "laptop": {"price":999, "stock": 15},
    "phone": {"price": 699, "stock": 50}
}

print(products["laptop"]["price"])

print(products["laptop"]["stock"])
print(products["phone"]["stock"])

countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]

mixed = {}
for  countries, capitals in zip(countries, capitals):
    mixed[countries] = capitals 
print(mixed)

products["Tablet"] = {"price": 499, "stock": 30}
print("Products Updated:", products)

for product, stock in list(products.items()):
    if stock["stock"] < 20:
        del products[product]

company = {
    "Engineering": {"Alice": 95000, "Bob": 85000},
    "Marketing": {"Carol": 75000, "Dave": 70000}
}

for name, info in company.items():
    print(f"\n{name}:")
    for employee, salary in info.items():
        print(f" {employee}: ${salary:,}")

engineering_salaries = company["Engineering"].values()
engineering_avg = sum(engineering_salaries) / len(engineering_salaries)
print(f"Engineering average salary: ${engineering_avg:,.2f}")

marketing_salaries = company["Marketing"].values()
marketing_avg = sum(marketing_salaries) / len(marketing_salaries)
print(f"Marketing Average Salary: ${marketing_avg:,.2f}")

highest_paid = max(
    (
        (employee, salary, department)
        for department, employees in company.items()
        for employee, salary in employees.items()
    ),
    key=lambda item: item[1]
)

print(
    f"Highest-paid employee: {highest_paid[0]} "
    f"({highest_paid[2]}) - ${highest_paid[1]:,}"
)

cubes = {x: x**3 for x in range(1, 6)}
temps = {"Mon": 72, "Tue": 68, "Wed": 75}

temps_c = {day: (f - 32) * 5/9 for day, f in temps.items()}
temps_c_rounded = {day: round((f - 32) * 5/9, 2) for day, f in temps.items()}

scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}

passing = {name: score for name, score in scores.items() if score >= 70}
def to_letter(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

letter_grades = {name: to_letter(score) for name, score in scores.items()}
student_ids = {"Alice": 101, "Bob": 102}
inverted_ids = {id_num: name for name, id_num in student_ids.items()}

print(letter_grades)
print(student_ids)
print(inverted_ids)
print(passing)


sales = [
    ("North", "Alice", 5000), ("South", "Bob", 4500),
    ("North", "Carol", 6000), ("South", "Alice", 3500)
]

sales_by_region = {}
for region, _, amount in sales:
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

sales_by_person = {}
for _, person, amount in sales:
    sales_by_person[person] = sales_by_person.get(person, 0) + amount

nested_sales = {}
for region, person, amount in sales:
    nested_sales.setdefault(region, {})[person] = (
        nested_sales.get(region, {}).get(person, 0) + amount
    )
print(sales_by_region)
print(sales_by_person)
print(nested_sales)

vowels = {"a", "e", "i", "o", "u"}
s = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

empty_set = set() #should have ()

text = "mississippi"
unique_chars = set(text)
#unique letter = m i s p

emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]
unique_emails = list(set(emails))

#fails because ot is an unhashable type: "list"

import time

numbers_list = list(range(1000000))
numbers_set = set(numbers_list)
target = 999999


start = time.counter()
target in numbers_list
list_time = time.counter() - start

start = time.counter()
target in numbers_set
set_time = time.counter() - start

key_set = frozenset([1, 2, 3])

group_permissions = {key_set: "Admin Access"}


print(group_permissions[key_set])
edges = [(1, 2), (2, 3), (1, 3), (3, 4)]

nodes = {node for edge in edges for node in edge}

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
#Find all unique numbers (union). 1, 2, 3, 4, 5, 6
# Find numbers in both sets (intersection).3, 4
# Find numbers only in set a (difference)1, 2

morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}

all_shifts = morning_shift & evening_shift & weekend_shift

any_shift = morning_shift | evening_shift | weekend_shift

only_morning = morning_shift - (evening_shift | weekend_shift)

exactly_one = (
    (morning_shift - evening_shift - weekend_shift)
    | (evening_shift - morning_shift - weekend_shift)
    | (weekend_shift - morning_shift - evening_shift)
)

print(" All shifts:", all_shifts)
print(" At least one shift:", any_shift)
print(" Only morning shift:", only_morning)
print(" Exactly one shift:", exactly_one)

prereqs_met = {"Alice", "Bob", "Carol", "Dave"}
has_space = {"Bob", "Carol", "Eve", "Frank"}
paid_tuition = {"Alice", "Carol", "Eve"}

eligible = prereqs_met & has_space & paid_tuition

prereq_unpaid = prereqs_met - paid_tuition

all_students = prereqs_met | has_space | paid_tuition
needs_prereq_or_tuition = all_students - (prereqs_met & paid_tuition)

print("Eligible to enroll:", eligible)
print(" Met prereqs but unpaid:", prereq_unpaid)
print(" Missing prereqs or tuition payment:", needs_prereq_or_tuition)

s = {1, 2, 3}
s.add(4)
s.remove(1)
print(" Modified set:", s)

evens = {x for x in range(21) if x % 2 == 0}
print(" Even numbers (0-20):", evens)

my_set = {10, 20, 30}

my_set.discard(99)
print(" discard(99):", my_set)

try:
    my_set.remove(99)
except KeyError:
    print(" remove(99) ")

nums = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]

unique_nums = list(dict.fromkeys(nums))
print("1. Unique numbers preserving order:", unique_nums)

sentence = "To be or not to be that is the question"

unique_words = {word.lower() for word in sentence.split()}
print("2. Unique words:", unique_words)

expected = set(range(1, 11))
actual = {1, 2, 4, 5, 7, 8, 10}

missing = expected - actual
print("Missing numbers:", missing)

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
            
    return duplicates

print(find_duplicates([1, 2, 2, 3, 3, 3, 4]))

alice = {"Python", "SQL", "Excel", "Tableau"}
bob = {"Python", "Java", "SQL", "AWS"}
carol = {"Python", "R", "SQL", "Tableau"}

all_three = alice & bob & carol

only_alice = alice - (bob | carol)

all_unique = alice | bob | carol

print("Skills all three have:", all_three)
print("Skills only Alice has:", only_alice)
print("All unique skills across team:", all_unique)

def common_chars(str1, str2):
    return set(str1) & set(str2)


print(common_chars("hello", "world"))
