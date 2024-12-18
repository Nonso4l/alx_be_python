monthly_income = int (input("Enter your monthly income:"))
monthly_expenses = int (input("Enter your total monthly expenses:"))
monthly_savings = monthly_expenses - monthly_income
rate = 0.05
projected_savings = monthly_savings * 12 + monthly_savings * 12 * 0.05
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savingsafter one year, with interest, is: ${projected_savings}.")