import random

sims = 100000
equal_occur = 0

for i in range(sims):
    bluejays = random.randint(1, 200)
    cardinals = random.randint(1, 200)

    bird_list = ["B"] * bluejays + ["C"] * cardinals

    B_count = 0
    C_count = 0

    temp = bird_list
    random.shuffle(temp)
    
    for bird in temp:
        if bird == "B":
            B_count += 1
        if bird == "C":
            C_count += 1
        if B_count == C_count:
            equal_occur += 1
            break

print(f"Probability that at some point, same number has flown away: {equal_occur/sims}, there were {equal_occur} equal occurences over {sims} simulations")