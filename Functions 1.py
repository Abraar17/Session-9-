def CompExtPrice(qty, unitprice):
  extprice = qty * unitprice
  if extprice > 10000:
    discamt = extprice * 0.10
  else:
    discamt = 0
  newExtPrice = extprice - discamt
  return newExtPrice


totalextprice = 0

answer = input("Do you want to this yes or no")
while answer == "yes":
  qty = int(input("Please enter qty"))
  price = int(input("Please eneter price"))
  extprice = CompExtPrice(qty, price)

  print(qty)
  print(price)
  print(extprice)
  totalextprice = totalextprice + extprice
  answer = input("Do you want to continue yes or no")

print(totalextprice)
