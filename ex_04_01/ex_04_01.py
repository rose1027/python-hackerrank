def computepay(h,r):
    r = 1.5*r
    h = h-40
    pay = h*r
    return pay

def regularpay(h,r):
    payment = h*r
    return payment



hrs = input("Enter Hours:")
rts = input("Enter Rates:")
hours = float(hrs)
rates = float(rts)
if hours <= 40:
    totalpay = regularpay(hours, rates)
    print('Pay', totalpay)
else:
    totalpay = 40*rates + computepay(hours,rates)
    print('Pay', totalpay)
