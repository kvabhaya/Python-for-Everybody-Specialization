# Prompt the user for hours worked and hourly rate
hours_str = input("Enter hours worked: ")
rate_str = input("Enter hourly rate: ")

# Convert the input strings to float
hours = float(hours_str)
rate = float(rate_str)

# Calculate gross pay
if hours <= 40:
    gross_pay = hours * rate
else:
    regular_pay = 40 * rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (1.5 * rate)
    gross_pay = regular_pay + overtime_pay

# Display the gross pay
print(gross_pay)
