# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ")
previous = float(input("Enter previous meter reading: "))
current = float(input("Enter current meter reading: "))

# Check if the name isn't blank
if name.strip()== "":
    print("Costumer name must NOT be empty, please try again.")
    name = input("Enter customer name: ")

# Check if the reading s atleast 0
if previous < 0:
    print("Previous reading must be atleast 0.")
    previous = float(input("Enter previous meter reading: "))
    
# Check if the reading is atleast the previous reading
if current < previous:
    print("Current reading must be atleast the previous reading.")
    current - float(input("Enter current meter reading: "))

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
