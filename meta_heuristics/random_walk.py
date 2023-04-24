from math import sqrt, sin
import random
def objective(x1,x2):
     return -(x2 + 47) * sin(sqrt(abs(x2 + x1/2 + 47))) - x1 * sin(sqrt(abs(x1 - (x2 + 47))))


best = [random.uniform(-512,512),random.uniform(-512,512)]
step_size = 0.01

for x in range(0,10000):
    tmp1 = best[0] + random.uniform(-512,512) * step_size
    tmp2 = best[1] + random.uniform(-512,512) * step_size
    best = [tmp1,tmp2]
    print(objective(tmp1,tmp2))

print('Result:')
print('x:', best)
print('Fitness:', objective(best[0],best[1]))