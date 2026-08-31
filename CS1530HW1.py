my_info = {
    "name" : "Jirasol",
    "age" : "nineteen",
    "major" : "cybersecurity"
}

print(my_info)
print(type(my_info))


food = dict(soda=2.99, sandwiches=4.50, chips=1.00, ice_cream=2.50)
print(food)
print(type(food))


courses_credits = dict("CS1350":3, "CJ2500":3, "CS2500":3, "EGR2000":3, "NET2300":3")


weekly_temps = dict("Monday":76f, "Tuesday":78f, "Wednesday":82f, "Thursday":80f, "Friday":80f, "Saturday":82f, "Sunday":79f)


pet = {"name": "Buddy", "type": "dog", "age": 3}
print(pet["name"])
print(pet["age"])


pet = {
  "name": "Buddy",
  "type": "dog",
  "age": 3
}
print(pet.get("color"))


student = {
  "Name": "Jirasol",
  "Course": "CS2000",
  "Grade": 85,
  "Academic Standing": "Passing"
}
print(student.get("Academic Standing))


products = {
  "Hair Oil": 20.99, 
  "Bar Shampoo": 15.99,
  "Bar Conditioner": 15.99,
  "Anti-Friz": 5.99
}
print(products.get("Body Wash", "Product Not Available"))
print(products.get("Hair Oil"))


Inventory = {}
Inventory["Cups"] = 120
Inventory["Bowls"] = 150
Inventory["Utensils"] = 175
print("After adding:", Inventory)


scores = {"Team A": 45, "Team B": 38}

scores["Team B"]= 52
print("After update:", scores["Team B"])

scores["Team C"] = 41
print("After adding:", scores)

removed = scores.pop("Team A")
print(removed)
print(scores)


cart = {}
cart["Milk"] = 2.09
cart["Eggs"] = 1.75
cart["Bread"] = 1.00

cart["Eggs"] = 2.75
print("After updating:", cart["Eggs"])

removed = cart.pop("Bread")
print(removed)
print(cart)

"student_name" = valid, names are immutable
[1,2,3] = invalid, lists are mutable
100 = valid, numbers are immutable
("x","y") = valid, tuples are immutable
{"a":1} = invalid, sets are mutable
frozenset({1,2}) = vaild, frozensets are immutable


#FindErrorAndFix
locations = {(40.7,-70.0): "New York", (34.0,-118.2):"Los Angeles:}


#PrintOutput
data = {"a": 1, "b": 2, "a": 3, "b": 4}
print(data)
print(len(data))
TypeError: Unhashable type: 'dict'
It was valid, I wonder why however since it is a dict class and is mutable

#InvestigateHash
print(hash("Jirasol"))
7858717126683173729
print(hash("100"))
8543016660832658670


#Advanced
print("\n=== Game Data ===")
game_data = {("Josh", "Game 1"): 25, ("Josh", "Game 2"): 22, ("Josh", "Game 3"): 26}
print(game_data[("Josh", "Game 2")])

Could not figure out number 2 under advanced.


#Beginner2.2
temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}
temps_data = {"Days": 3}
print(temps.keys())
print(temps.values())
print(temps_data["Days"])
#Intermediate2.2
print(max(temps.values())
if "Friday" in temps.keys():
    print("Friday Available")
if "Friday" not in temps.keys():
    print("Friday not available")
temps.setdefault("Thursday", 70)
key_view = temps.keys()
print(key_view)


#Advanced2.2
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}
print(sum(prices.values()))
print(sum(prices.values()) / len(prices.values()))
print(max(prices.items()))
print(min(prices.items()))
import sys
prices_ = {i: i*2 for i in range(10000)}
view = prices_.keys()
as_list = list(prices_.keys())
print(f"View size: {sys.getsizeof(view)} bytes")
print(f"List size: {sys.getsizeof(as_list)} bytes") 
prices.update({"Airpods": 150, "Smart Ring": 200, "Screen Protecter": 50})
print(prices)


#Beginner2.3
colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
for name, color in colors.items():
    print(f"{name} is {color}")

#prediction
('apple', 'red'), ('banana", 'yellow'), ('grape', 'purple')


prices = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}
for name, price in prices.items():
    taxed_price = price * 1.10
    print(f"{name}: ${price:.2f} + tax = ${taxed_price:.2f}")


    
    
