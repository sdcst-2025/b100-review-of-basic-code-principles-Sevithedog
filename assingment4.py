"""
### Name: Finlay Mitchner
### Assignment 4
#### Calculation of a debt repayment with recurring payments
This is the reverse of assignments 2 and 3

Calculate how long it will take to completely pay off a debt if regular payments are made.  Note that each year, the debt will increase by the amount of loan interest, but will decrease with youre recurring payment. 

Criteria:
Your program should ask the user for
* an initial debt
* the annual interest rate
* the annual payment
* the program will state how long it will take for the debt to be repaid.
* extra: Calculate the total amount of interest that is paid along with the debt repayment

Sample:
Joey takes a car loan to buy a new Tesla for $62000
The loan has an annual interest rate of .75% per month.  He makes monthly payments of $1000.
How many months will it take him to pay off the car.  How much interest has he paid in that time?

84 months
He will have paid 21711.60 in interest
"""

import time
import os
print("Debt repayment calculator")
time.sleep(1.5)
os.system('cls')
d = float(input("Enter initial debt: "))
os.system('cls')
r = float(input("Enter annual interest on debt as a percent: "))/100
os.system('cls')
p = float(input("Enter ammount repaid annually: "))
os.system('cls')
count = 0
tpaid = 0
d0 = d
while d > 0:
    d = d+d*r
    if d >= p:
        tpaid = tpaid + p 
    elif d < p:
        tpaid = tpaid + d
    d = d - p
    count += 1 
print(f"The dept will take {round(count,2)}yrs to repay. \nTotal paid: {round(tpaid,2)} \nInterest paid: {round(tpaid-d0,2)}")
    