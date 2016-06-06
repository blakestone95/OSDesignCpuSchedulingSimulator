from bisect import bisect
import random
import math

things = []
choices = []
probabilities = []
i = random.randrange(10)+2
for a in range(1,i):
    things.append(random.randrange(10)+1)
total = sum(things)
    
for a in range(1,i):
    probabilities.append(math.ceil(things[a-1]/total*100/(a*2)))
    choices.append((things[a-1],probabilities[a-1]))

def weighted_choice(choices):
    values, weights = zip(*choices)
    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)
    x = random.random() * total
    i = bisect(cum_weights, x)
    return values[i]
#print(weighted_choice([("WHITE",90), ("RED",8), ("GREEN",2)]))
print(choices)
print(weighted_choice(choices))
print(weighted_choice(choices))
print(weighted_choice(choices))
print(weighted_choice(choices))
print(weighted_choice(choices))
print(weighted_choice(choices))
