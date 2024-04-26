name = input('Enter your name: ')
customer_type = input("Enter Customer Type (n: new, e: existing): ")
deposit = float(input("enter deposit amound: "))

if customer_type == "n":
    interest = 0.03
else:
    if deposit <= 1000:
        interest = 0.03
    elif deposit <= 10000:
        interest = 0.0325
    elif deposit > 10000:
        interest = 0.035
    
total = (1+interest) * deposit
print(total)