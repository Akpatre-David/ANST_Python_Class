monthlyIncome = float(input("Enter your Monthly Income:"))

monthlyExpenses = float(input("Enter your Monthly Expenses:"))

monthlySavings = float(monthlyIncome - monthlyExpenses)

# To calculate project annual savings

projectedSavings = float(monthlySavings * 12 + (monthlySavings * 12 * 0.05))

print(f"Your monthly saving is: {monthlySavings}")
print(f"Your projected annual savings after interest is: {projectedSavings}");;;;;;