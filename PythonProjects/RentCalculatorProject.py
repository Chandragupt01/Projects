## Inputs we need from the user
# total rent
# Total food ordered for snacking 
# electricity units spend
# charge per unit
# no. of persons staying in flat

## outputs
# total amount you have to pay

rent=int(input("Enter Your Flat rent: "))
foodCost=int(input("Enter the amount of food ordered: "))
electricitySpend=int(input("Enter the units of Electricity spend: "))
chargePerUnit=int(input("Enter the charge per unit: "))
persons=int(input("Enter the number of persons living in flat: "))

totalElectricBill=electricitySpend*chargePerUnit
output=(foodCost+rent+totalElectricBill)//persons
print("Each person will pay= ", output)