# mortgage.py
#
# Exercise 1.7

#from http.client import PAYMENT_REQUIRED


principal = 500000.0
rate = 0.05
standard_payment = 2684.11
total_paid = 0.0
numPayments = 0

#user settable values
extra_payment_start_month = 60
extra_payment_end_month = 360
extra_payment = 1000.0

while principal > 0:
    
    #make sure last payment isn't overpayment
    if principal < standard_payment: 
        payment = principal
        principal = 0 # so we don't continually pay fractions of cents...
        extra_payment = 0
    else:
        payment = standard_payment
        principal = principal * (1 + rate/ 12) - payment
    
    total_paid = total_paid + payment

    #Dave may pay extra in some months
    if numPayments >= extra_payment_start_month and numPayments <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    numPayments = numPayments + 1
    print(numPayments, round(total_paid,2), principal)

print("Total paid", round(total_paid,2))
print('Months', numPayments)
