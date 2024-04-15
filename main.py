import numpy as np

# Initial values
principal = 1192500
annual_interest_rate = 0.0587
loan_term_years = 30

# Calculate monthly interest rate and total payments
monthly_interest_rate = annual_interest_rate / 12
total_payments = loan_term_years * 12

# Calculate monthly payment manually
monthly_payment = principal * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -total_payments))

# Create lists to hold per month calculations
month_list = []
payment_list = []
interest_list = []
principal_list = []
balance_list = []

# Start loop
for month in range(1, total_payments+1):
    interest_payment = principal * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance = principal - principal_payment

    # Append values to lists
    month_list.append(month)
    payment_list.append(monthly_payment)
    interest_list.append(interest_payment)
    principal_list.append(principal_payment)
    balance_list.append(remaining_balance)

    # Update principal for next month
    principal = remaining_balance

# Print results
for i in range(total_payments):
    print(f"Month {month_list[i]}: Payment = {payment_list[i]}, Interest = {interest_list[i]}, Principal = {principal_list[i]}, Remaining Balance = {balance_list[i]}")
