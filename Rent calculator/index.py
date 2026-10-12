Rent = int(input("Enter your hostel/Flat rent: "))
Food = int(input("Enter your food expenses: "))
electricity = int(input("Enter your electricity bill: "))
charge_per_unit = int(input("Enter your electricity charge per unit: "))
persons = int(input("Enter the number of persons sharing the rent: "))

total = Rent + Food + electricity * charge_per_unit
per_person = total / persons

print("Total expenses: ", total)
print("Expenses per person: ", per_person)