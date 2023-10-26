def CalcBatAvg(hits,atBat):
  if(atBat==0):
    return 0
  else:
    batavg=hits/atBat
    return batavg


count=0
ans="a"
while (ans != "z"):
  lt=(input("Enter last name"))
  h=int (input("Enter num of hits"))
  bk=int (input("Enter bats at key"))
  count=count+1
  batavg=CalcBatAvg(h,bk)
  ans=input("and press z")

print(lt)
print(batavg)
print(count) 