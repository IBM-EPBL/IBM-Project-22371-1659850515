import random
def alert(t):
  if t>30:
    print("SET alert on")
  else:
    print("SET alert off")
      

while(1):
  readtemp=random.randint(25,100)
  humidity=random.randint(0,100)
  print(readtemp,humidity)
  
  alert(readtemp)
  print("\n")
