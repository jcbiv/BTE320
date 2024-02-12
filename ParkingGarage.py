fee = float(5)

for hour in range(1,9,1):

    fee +=2.5

    if fee <= 10.0:
        minfee = 10.0
        print(f"{hour} ${minfee}")

    elif fee <= 20.0:
        print(f"{hour} ${fee}")
    else:
        fee = 20.0
        print(f"{hour} ${fee}")
    