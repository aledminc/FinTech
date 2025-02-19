import random

nuts = 6
sims = 1000000
result = []

for i in range(sims):
    nuts = 6
    while 0 < nuts < 36:
        nuts += random.choice([1, 1, -1])
    result.append(nuts)

count = 0
for elem in result:
    if elem == 0:
        count += 1

empty_num = count/sims
print("Prob of hungry is " + str(empty_num) + " or " + str(count) + "/" + str(sims))

 
