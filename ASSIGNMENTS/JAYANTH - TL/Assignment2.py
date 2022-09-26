import random
def alarm(t):
  if t>50:
    print("alarm on")
  else:
    print("alarm off")
      

while(1):
  temp=random.randint(20,100)
  humi=random.randint(0,100)
  print(temp,humi)
  
  alarm(temp)
  print("\n")
