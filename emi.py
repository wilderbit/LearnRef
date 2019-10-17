"""
L = Loan Amount
I = Interest Rate Per Month
N = Loan Period in Months
EMI  = (Loan * I) * ((1 + I)^N) / ((1 + I)^N) - 1))

"""
import math
import csv
print("Enter Amount :: ")
L = float(input()) # 1000000
print("Enter rate of interest per year :: ")
R = float(input()) # 7.0
print("Enter number of months :: ")
N = int(input()) # 18
Amount = L
I = R / (12 * 100)
p = math.pow(1 + I, N)
emi = L * I * (p / (p - 1))
print ("EMI Amount :: ", round(emi, 2))
print ("Total Payable Interest", round(emi * N - L, 2))
with open('Data.csv', mode='w') as file:
    total_interest = 0
    total_emi_amount = 0
    total_principle = 0
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Month', 'Amount', 'Interest/Month', 'Paid Principal/Month', 'EMI', 'Remaining Amount', 'Paid On'])
    for x in range(1, N + 1):
        interest = (L * I)
        total_interest += interest
        total_emi_amount += emi
        principle = round(emi - interest, 2)
        total_principle += principle
        writer.writerow([x, round(L, 2), round(interest, 2), principle, round(emi, 2), round(L - (emi - interest), 2)])
        L = L - (emi - interest)
    writer.writerow(['Total', Amount, round(total_interest, 2), math.ceil(total_principle), round(total_emi_amount, 2)])
