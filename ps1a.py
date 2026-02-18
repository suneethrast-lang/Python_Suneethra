#taking input from the user
annual_salary=float(input("Enter enter the annual salary:"))
portion_saved=float(input("Enter the percent salary to save, as a decimal per count:"))
invest_money=float(input("Enter the investment money per year:"))
total_cost=float(input("Enter the cost of the dream house:"))

#Finding and calculating the essential values for the month calculation
month=0
down_payment=(total_cost*0.25)
monthly_salary = annual_salary / 12

while current_savings < down_payment:
    current_savings += current_savings * (0.04 / 12) #Inputing the investment savings
    current_savings += monthly_salary * portion_saved #Saving the savings amount, from the monthly and investment return money
    months += 1

print(f"The no.of months left for the down payment repayment is {month}")