hoursworked= input("Enter hours : ")
hourlypay= input("Enter amount : ")
taxrate= 18

print("Hours Worked: ", hoursworked)
print("Hourly pay rate: ", hourlypay)

grosspay = float(hoursworked) * float(hourlypay);
print("gross pay : " , grosspay)
taxamount = int(grosspay) * float(taxrate / 100)
print("tax rate: ", taxrate)
print("tax amount: ", taxamount)


takehomepay = int(grosspay) - int(taxamount)
print("tax home pay: ", takehomepay)
