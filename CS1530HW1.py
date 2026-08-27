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


