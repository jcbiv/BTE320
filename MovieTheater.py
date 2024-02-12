ticket = 10
people = 20
FixCost = 200

for adspend in range (0, 225, 25):
    
    people += 2 * round((adspend**.5))
    
    print(f"Adspend: {adspend}")
    
    print(f"People: {people}")
    
    revenue = people * ticket

    Profit = revenue - FixCost - adspend

    print(f"profit: {Profit}")
    print("_________________")

    people = 20
