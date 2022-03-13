#program for calculating electricity bill in python

units = int(input("please enter the number of units you consumed in a month:"))

if(units<=100):
    pAmount=units*1.5
    fcharge=25.00

elif(units<=200):
    pAmount=(100*1.5)+(units-100)*2.5
    fcharge=(50.00)

elif(units<=300):
    pAmount=(100*1.5)+(200-100)*2.5+(units-200)*41
    fcharge=75.00

elif(units<=350):
    pAmount=(100*1.5)+(200-100)*2.5+(300-200)*4+(units-300)*5
    fcharge=100.00

else:
    pAmount=0
    fcharge=1500.00

Total=pAmount+fcharge;
print("\nElectricity Bill=%.2f"%Total)
