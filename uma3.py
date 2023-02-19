import os
import time
import random

def draw(uma, kuu, colors):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('start:  --------------  :gorl')  
    for j in range(0,5):
        print('uma',j+1,kuu[(uma[j])],colors[j],'ウマ',colors[6])
    print('start:  --------------  :gorl')

uma = [0] * 6
kuu = ['  ' * i for i in range(8)] 
colors = [f"\033[{i+31}m" for i in range(7)]  #python 3.6以降 

ran = 0
while uma[ran] < 7: 
    ran = random.randint(0,4)
    draw(uma, kuu, colors)
    uma[ran] +=1
    time.sleep(1)

draw(uma, kuu, colors)
print (ran+1,colors[0],'の優勝です',colors[6])
