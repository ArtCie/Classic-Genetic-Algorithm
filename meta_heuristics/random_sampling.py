from math import sqrt, sin
import random
def objective(x1,x2):
     return -(x2 + 47) * sin(sqrt(abs(x2 + x1/2 + 47))) - x1 * sin(sqrt(abs(x1 - (x2 + 47))))


best = [random.uniform(-512,512),random.uniform(-512,512)]

for x in range(0,100000):
    tmp1 = random.uniform(-512,512)
    tmp2 = random.uniform(-512,512)
    if(objective(tmp1,tmp2)<objective(best[0],best[1])):
        best = [tmp1,tmp2]
    #print(objective(tmp1,tmp2))

print('Result:')
print('x:', best)
print('Fitness:', objective(best[0],best[1]))