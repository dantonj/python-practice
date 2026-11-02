total = 0
count = 0

expense = float(input("Enter an expense(0 to stop):"))
if expense == 0:
    print("No expenses entered.")
else:
    total += expense
    count += 1

    while True:
        expense = float(input("Enter an expense(0 to stop):"))
        if expense == 0:
            break
        total += expense
        count += 1

    average = total / count
    print(f"Total expenses: ${total:.2f}")
    print(f"Average expense: ${average:.2f}")
