# bubblegum = 202
# toffee = 118
# ice_cream = 2250
# milk_chocolate = 1680
# doughnut = 1075
# pancake = 80
#
# income:  = bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake
#
# print("Earned amount:")
# print(f"Bubblegum: ${bubblegum}")
# print(f"Toffee: ${toffee}")
# print(f"Ice cream: ${ice_cream}")
# print(f"Milk chocolate: ${milk_chocolate}")
# print(f"Doughnut: ${doughnut}")
# print(f"Pancake: ${pancake}" + "\n")
# print(f"Income : ${income:.1f}")
#
# print("Hello, " + name)
# name = input()

# amount = 1000
# interest_rate = 5
# years = 1
# # change the next line
# income = (amount * interest_rate * years) / 100
#
# n_group1 = int(input())
# n_group2 = int(input())
# n_group3 = int(input())
#
# need_desks = 0
# if n_group1 > 0:
#     need_desks += (n_group1 // 2) + (n_group1 % 2)
# if n_group2 > 0:
#     need_desks += (n_group2 // 2) + (n_group2 % 2)
# if n_group3 > 0:
#     need_desks += (n_group3 // 2) + (n_group3 % 2)
#
# print(need_desks)

# print("The ", end="Chip")
# characters = ['Humphrey the Bear', 'Spike the Bee', 'Fat Cat']
# for element in characters:
#     print("\n", element, end="@gmail.com")
# print("\n", *characters)

#
# name = ['M', 'A', 'R', 'C', 'O']
# # modify the next line
# print(*name, sep="-", end="!")

# poem = ['The night', 'the pharmacy', 'the street', 'the pointless lamppost in the mist']
# print(*poem, sep=', ')

bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80

staff_expenses = int(input("Staff expenses: "))
other_expenses = int(input("Other expenses: "))
net_expenses = staff_expenses + other_expenses

expenses_type_list = [bubblegum, toffee, ice_cream, milk_chocolate, doughnut, pancake]

income = 0
for types in expenses_type_list:
    income += types
net_income = income - net_expenses
print("Earned amount:")
print("Bubblegum: $", bubblegum)
print("Toffee: $", toffee),
print("Ice cream: $", ice_cream)
print("Milk chocolate: $", milk_chocolate)
print("Doughnut:  $", doughnut)
print("Pancake: $", pancake, end="\n\n")
print("Income: $", float(income))
print("Staff expenses:")
print(staff_expenses)
print("Other expenses:")
print(other_expenses)
print("Net income: $", net_income)
#
# bubblegum = 202
# toffee = 118
# iceCream = 2250
# milkChocolate = 1680
# doughnut = 1075
# pancake = 80
#
# income: float = bubblegum + toffee + iceCream + milkChocolate + doughnut + pancake
#
# print("Earned amount:")
# print(f"Bubblegum: ${bubblegum}")
# print(f"Toffee: ${toffee}")
# print(f"Ice Cream: ${iceCream}")
# print(f"Milk Chocolate: ${milkChocolate}")
# print(f"Doughnut: ${doughnut}")
# print(f"Pancake: ${pancake}" + "\n")
# print(f"Income : ${income:.1f}")