# Compare the Triplets
def compareTriplets(a,b):
  Alice_point=0
  Bob_point=0
  for i in range(len(a)):
    if a[i]>b[i]:
      Alice_point+=1
    elif a[i]<b[i]:
       Bob_point+=1
  return Alice_point,Bob_point






try:
# 5 6 7 , 3 6 10
  a=list(map(int,input("").split())) # input numbers in a
  b=list(map(int,input("").split())) # input numbers in b
  if len(a)!=3 and len(b)!=3:
    print("Error")
  else:
    result=compareTriplets(a,b)
    print(result[0],result[1])
except ValueError:
  print("Invalid integer")
