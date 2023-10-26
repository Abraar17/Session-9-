def Calcpayrate(hw,jc):
  merc=0
  if jc=="l":
    merc=25

  if jc=="a":
    merc=30

  if jc =="j":
    merc=50
  return merc

  


count=0
ans="a"
Overtime=0
Gp=0
while (ans != "z"):
  ln=(input("Enter lastname"))
  jc= (input("jobcode"))
  hw=int (input("Enter hours worked"))
  count=count+1
  pay=Calcpayrate(jc,hw)
  if (hw>40):
    Overtime = (hw-40)
  Gp = (Overtime * pay) + (pay * (hw-40))+Gp


  

  print (ln)
  print (gp)

