#saranya assignment-2
import random
for i in range(1,100):
    t=random.randint(1,100)
    h=random.randint(1,100)
    print(t)
    print(h)
    
    if(t>50):
       print("temperature is high")
       print("humidity is high")
       print("alaram on")
    else:
        print("alaram off")

