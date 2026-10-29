name = input("Enter Business Name:")
revenue = float(input("Enter Revenue:"))
expenses = float(input("Enter Expenses:"))
def calculate_profit(revenue,expenses):
    return (revenue - expenses) 

if revenue == 0:
    print("Revenue cannot be zero.")
else:
    profit = calculate_profit(revenue, expenses)
    profit_margin = calculate_profit(revenue, expenses) / revenue * 100
    print("Business Name:", name)
    print(f"Revenue: ${revenue:,.2f}")
    print(f"Expenses: ${expenses:,.2f}")
    print(f"Profit: ${profit:,.2f}")
    print(f"Profit Margin: {profit_margin:.2f}%")

    if profit < 0:  
        print("Business Status: Loss")
    elif profit == 0:
        print("Business Status: Break-even")
    else:
        print("Business Status: Profit")


