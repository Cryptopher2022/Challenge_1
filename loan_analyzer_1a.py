# This program is intended for Lenders of microloans.  You can evaluate one loan or 
# several loans all at once.  A company with a portolio of loans might use this to 
# evaluate the value of each loan or the entire portolio of loans. Alternatively, this
# program can be used by an investor to evaluate the value of the portfolio to assist
# in determining if an investment should be made.  


import csv
from email.policy import default
from multiprocessing.sharedctypes import Value
from pathlib import Path

# Part 1: In this first part of the program, these calculations will automate Automate the Calculations.
# The loans will be provided in a list for evaluation of the 1. Number of Loans 2. The summed total of 
# all of the portolio of loans and the average loan amounts across the entire portolio of loans.  

# The first input provided is a list of the loan costs.  
loan_costs = [500, 600, 200, 1000, 450]

# This section will determine the number of loans in the portfolio.  
number_of_loans = len(loan_costs)
print(number_of_loans)


# This section will determine the total loan cost within the entire portolio.  
loan_total = sum(loan_costs)
print(loan_total)

# This piece of code will find the average loan cost across the entire portolio of loans. 
average_loan = (loan_total/number_of_loans)
print(average_loan)

# In this section, a dictionary is used to provide the input data for a variety of calculations.  
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# in this section, the Present Value (fair_value) of the loan is calculated and compared to the Future Value.  
future_value = loan.get("future_value")
print(f"The Future Value of this loan is", future_value)

remaining_months = loan.get("remaining_months")
print (f"The number of remaining months on the loan is", remaining_months)

fair_value = future_value/(1 + (.2/12))**remaining_months
print(f"The Fair Value of this loan is $", fair_value)

# This section uses the get() function to "get" the loan price from the dictionary and then compare the fair_value to 
# the future value.  
loan_price = loan.get("loan_price")

if fair_value > loan_price:     print("The fair value of this loan $",fair_value, "is worth purchasing versus the cost of $", loan_price)
else: print("The fair value of this loan $", fair_value, " is not worth purchasing versus the cost of $", loan_price)

# A new dictionary of information conveys the parameters for a given loan.  
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
# The person evaluating these loans has set their "hurdle rate" at 20%.  This section "gets" the remaining months
# for this loan.  From that point, the program has the adequate information needed to determine the Present Value.  
annual_discount_rate = .2
remaining_months =  new_loan.get("remaining_months")
present_value = future_value/(1 + (annual_discount_rate/12))**remaining_months

# The Present Value is then printed.  
print(f"The present value of the loan is: ${present_value}")

# In this section a dictionary is used to pass information for a portfolio of loans to be evaluated.  
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# The new variable "inexpensive_loans" is defined and set at zero or empty.  `
import csv
from pathlib import Path
inexpensive_loans = []

# The next section loops through all the loans and appends any that cost $500 or less to the `inexpensive_loans` list

for choices in loans:
    
    if choices["loan_price"] <= 500:
        inexpensive_loans.append(choices)
        print(f"These are the loans selected through criterial input into the program", choices)

# In this section, the results will be exported to the CSV file.  
# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path (output_path = Path("inexpensive_loans.csv")) to export the results. 

output_path = Path("inexpensive_loans.csv")

print("Writing the data to a CSV file...")

with open(output_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=":")

    csvwriter.writerow(header)

    for item in inexpensive_loans:
        csvwriter.writerow(item.values())

