def Calcmpg(m,g):
  mpg= (m/g)
  return mpg
  


count=0
ans="a"
while (ans != "z"):
  c=(input("Enter city"))
  m=int (input("Enter miles"))
  g=int (input("Enter gallons used"))
  count=count+1
  bmw=Calcmpg(m,g)
  ans=input("and press z")

print(c)
print(m)
print(bmw)