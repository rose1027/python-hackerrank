hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rates:")
r = float(rate)
if h<=40 :
    Pay=h*r
else:
    Payregular=40*r
    r = 1.5*r
    Paymor40 = (h-40)*r
    Pay= Payregular+ Paymor40
print(Pay)
