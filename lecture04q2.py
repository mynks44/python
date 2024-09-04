costofmeal= input("cost of meal : ")
tippercent= input("tip percent : ")
taxrate= 18

print("cost of meal: ", costofmeal)
print("number of tip percent: ", tippercent)

tip = float(costofmeal) * float(tippercent) / 100
print("tip amount : " , tip)
totalamount = float(costofmeal) + float(tip)
print("total amount: ", totalamount)
