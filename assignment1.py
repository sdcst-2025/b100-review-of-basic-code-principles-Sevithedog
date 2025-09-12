"""
### Name: Finlay Mitchner
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""

import os
import time
print("Simple interest calculator")
time.sleep(1)
os.system('cls')
P = float(input("Enter principle investement: "))
os.system('cls')
r = float(input("Enter annual interest rate as a percent: "))/100
os.system('cls')
t = float(input("Enter the length of time: "))
os.system('cls')
I = P*r*t
print(f"Interest earned: ${I} \nFinal value: ${I + P}")