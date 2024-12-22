def calculate_monthly_savings(monthly_income, monthly_expenses):
    return monthly_income - monthly_expenses

def calculate_projected_annual_savings(monthly_savings):
    annual_savings = monthly_savings * 12
    interest = annual_savings * 0.05
    return annual_savings + interest

def main():
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your total monthly expenses: "))

    monthly_savings = calculate_monthly_savings(monthly_income, monthly_expenses)
    projected_annual_savings = calculate_projected_annual_savings(monthly_savings)

    print(f"Your monthly savings are ${monthly_savings:.2f}.")
    print(f"Projected savings after one year is ${projected_annual_savings:.2f}.")

if __name__ == "__main__":
    main()