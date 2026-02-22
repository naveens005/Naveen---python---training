orderamount = float(input('enter order amount:'))
customertype= input('enter customer type:')
deliverydistance= int(input('enter delivery dist in km:'))
paymentmethod=input('enter payment mode online/cod')
billamount=0
if orderamount >= 1000:
    discount_amount = orderamount*(10/100)
    billamount= orderamount - discount_amount
if orderamount >= 500 and orderamount <= 999:
    discount_amount=orderamount*(5/100)
    billamount= orderamount - discount_amount
print("after discount",billamount)
if customertype=='prime' and orderamount>=1000:
   billamount=billamount - (orderamount*(5/100)) 
print('checking for prime customer', billamount)

if deliverydistance <=  5:
    billamount+=40
    print("after deliverydistance",billamount)
elif deliverydistance > 5:
    billamount+=70
    print("after deliverydistance",billamount)

if paymentmethod=="cod" and orderamount>=500:
    billamount+=25
    print("while cod",billamount)