total_100 = 0
total_50 = 0
total_20 = 0
total_10 = 0
total_5 = 0
total_1 = 0
customer_served = 0
total_dispensed = 0
serving = True  
while serving:
    name = input("What is your name? ")
    amount = int(input(f"Hello {name}, how much money would you like to withdraw? "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive number.")
        continue
    remaining_amount = amount
    index = 1
    while index <= 6:
        if index == 1:
            bill_value = 100
        elif index == 2:
            bill_value = 50
        elif index == 3:
            bill_value = 20
        elif index == 4:    
            bill_value = 10
        elif index == 5:
            bill_value = 5
        else:
            bill_value = 1
        count = remaining_amount // bill_value
        if count > 0:
            print(f"Dispensing {count} x ${bill_value} bills.")
            remaining_amount -= count * bill_value
            total_dispensed += count * bill_value
            if bill_value == 100:
                total_100 += count
            elif bill_value == 50:
                total_50 += count
            elif bill_value == 20:
                total_20 += count
            elif bill_value == 10:
                total_10 += count
            elif bill_value == 5:
                total_5 += count
            else:
                total_1 += count
        index += 1
    customer_served += 1
    print(f"Thank you {name}, your withdrawal of ${amount} has been processed.\n")
    total_dispensed += amount
    again = input("Would you like to serve another customer? (yes/no): ")
    if again.lower() != "yes":
        serving = False
print("Daily Denomination Report;")
for slots in range(1, 7):
    if slots == 1:
        bill_value = 100
        total_count = total_100
    elif slots == 2:
        bill_value = 50
        total_count = total_50
    elif slots == 3:
        bill_value = 20
        total_count = total_20
    elif slots == 4:
        bill_value = 10
        total_count = total_10
    elif slots == 5:
        bill_value = 5
        total_count = total_5
    else:
        bill_value = 1
        total_count = total_1
    print(f"${bill_value} bills dispensed: {total_count}")

print(f"100s: {total_100}")
print(f"50s: {total_50}")
print(f"20s: {total_20}")
print(f"10s: {total_10}")
print(f"5s: {total_5}")
print(f"1s: {total_1}")