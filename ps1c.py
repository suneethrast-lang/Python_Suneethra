#Collaboraters
'''
Yoshithaa Shree
Vaibhav
Ratinakumar
Sadhana
'''

import math
#Input from the user
starting_salary=float(input("Enter enter the annual salary:"))

#Given values
semi_annual_raise=0.07
total_cost=1000000
down_payment=(0.25*total_cost)
savings=0
step=0

#Values required for the bisectional search
low_bound=0.0 #Low_bound==>Zero savings
high_bound=1.0 #High Bound==>Full savings, i.e.,the annual salary
mid=(low_bound+high_bound)/2
months=36
rate=mid
best_rate=None 

def calculate_savings(rate): #To calculate the entire savings of the person, for 3 years
    savings = 0.0
    annual_salary = starting_salary
    monthly_salary = annual_salary / 12

    for month in range(1, months + 1):
        savings+=savings*(0.04/12)   
        savings += monthly_salary * rate
        if month % 6 == 0: #Increase in the semi-annual salary
            annual_salary += annual_salary * semi_annual_raise
            monthly_salary = annual_salary / 12
    return savings

if(calculate_savings(1.0)<down_payment): #Checking for the impossible condition
    print("It is not possible to pay the down payment in three years")
else:
    while True: #Traversing inside a loop, till the condition is proven to be false(Infinte in this case, the loop(Infinte) will break inside the loop, from the if condition)
        mid=(low_bound+high_bound)/2
        savings = calculate_savings(mid)
        step+=1

        if (abs(savings - down_payment) <= 100): #Check for the main condition, of the accuracy  of within 100 bucks
            best_rate=mid
            break
        elif savings < down_payment: #if the down payment is higher than the savings, the range from left side
            low_bound = mid
        else: #if the down payment is higher than the savings, the range from right side
            high_bound = mid

print("Best savings rate:", round(best_rate, 4))
print("Steps in bisection search:", step)

