# Prompt user for monthly income

monthlyIncome = int(input("Enter your monthly income:"))


totalMonthlyExpenses = int(input("Enter your total monthly Expenses:"))

monthlySavings = monthlyIncome - totalMonthlyExpenses

projectedSavings = monthlySavings * 12 + int(monthlySavings * 12 * 0.05)

print(f"Your monthly savings are ${monthlySavings}")

print(f"Projected savings after one year, with interest, is: ${projectedSavings}")