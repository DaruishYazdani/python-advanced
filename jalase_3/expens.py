commoditys = {}
product_nume = int(input("ENTER THE NUMBER OF GOODS:"))

for i in range(product_nume):
    commodity = int(input("Enter the purchase now:"))
    amount = float(input("enter the amount now:"))
    if commodity in commoditys:
        commoditys[commodity] += amount
    else : 
        commoditys[commodity] = amount
All_costs = sum(commoditys.values())
remaining = float(input("Enter the monthly budget:"))

if All_costs > remaining:
    print("Error!!!--The cost balance is more than the balance!")
else:
    print("You can buy, your budget is enough")