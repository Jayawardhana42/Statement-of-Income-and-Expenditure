def main():
    incomes = {}
    expenses = {}

    print("--- Income Statement Generator ---")

    # Collect incomes
    print("\nEnter Incomes (type 'done' to finish):")
    while True:
        item = input("Income item: ").strip()
        if item.lower() == "done":
            break
        if not item:
            continue

        try:
            val = float(input(f"Amount for '{item}': "))
            incomes[item] = incomes.get(item, 0) + val
        except ValueError:
            print("Please enter a valid number.")

    # Collect expenses
    print("\nEnter Expenses (type 'done' to finish):")
    while True:
        item = input("Expense item: ").strip()
        if item.lower() == "done":
            break
        if not item:
            continue

        try:
            val = float(input(f"Amount for '{item}': "))
            expenses[item] = expenses.get(item, 0) + val
        except ValueError:
            print("Please enter a valid number.")

    # Calculation
    tot_inc = sum(incomes.values())
    tot_exp = sum(expenses.values())
    net = tot_inc - tot_exp

    # Output
    print("\n--------------------------------")
    print("FINANCIAL SUMMARY")
    print("--------------------------------")

    print("\nINCOMES:")
    for k, v in incomes.items():
        print(f" - {k}: {v:.2f}")
    print(f"Total Income: {tot_inc:.2f}")

    print("\nEXPENSES:")
    for k, v in expenses.items():
        print(f" - {k}: {v:.2f}")
    print(f"Total Expenses: {tot_exp:.2f}")

    print("--------------------------------")
    if net > 0:
        print(f"Net Profit: {net:.2f}")
    elif net < 0:
        print(f"Net Loss: {abs(net):.2f}")
    else:
        print("Break-even (0.00)")


main()
