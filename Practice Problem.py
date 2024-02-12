
CustStatus = str(input("Write 'new' if new customer, write 'old' if existing customer: "))

deposit = float(input("Insert the value of your deposit: "))


if CustStatus == "old":
    if deposit < 1000:
        ir = .03
    elif deposit <= 10000:
        ir = .0325
    elif deposit > 10000:
        ir = .035
elif CustStatus == "new":
    ir = .03

depositf = int((1+ir)*deposit)

print(f"Your deposit is worth {depositf} after 1 year")