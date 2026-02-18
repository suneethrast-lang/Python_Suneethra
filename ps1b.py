#taking input from the user
annual_salary=float(input("Enter enter the annual salary:"))
portion_saved=float(input("Enter the percent salary to save, as a decimal per count:"))
total_cost=float(input("Enter the cost of the dream house:"))
semi_annual_raise=float(input("Enter the semi-annual raise:"))

#Finding and calculating the essential values for the month calculation
month=0
savings=0
down_payment=(0.25*total_cost)


while(savings<down_payment):
    monthly_salary = annual_salary / 12 #Finding the monthly salary
    savings += savings * (0.04 / 12) #Inputing the investment savings
    savings += (annual_salary/12) * portion_saved #Saving the savings amount, from the monthly and investment return money
    month += 1

    if month % 6 == 0:
        annual_salary *= (1 + semi_annual_raise)

print(f"The no.of months left for the down payment repayment is {month}")