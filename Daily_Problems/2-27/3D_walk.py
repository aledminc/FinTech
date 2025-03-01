import random

# moves = [-1, 1] for each -> (vertical up and down) (forward and back) (left and right)

move_dict = {"left": -1, "right": 1, "up": 1, "down": -1, "forward": 1, "backward": -1}
sims = 10000
back_to_origin = 0

for i in range(sims):

    forback = 0
    horizontal = 0
    vertical = 0
    steps = 2000

    for j in range(steps):
        if horizontal == 0 and vertical == 0 and forback == 0 and j > 0:
            back_to_origin += 1
            break
        move = random.choice(list(move_dict.keys()))
        if move == "left" or move == "right":   
            horizontal += move_dict[move]
        elif move == "up" or move == "down":
            vertical += move_dict[move]
        else:
            forback += move_dict[move]

    
print("The chances the bird returns to tree is: " + str(back_to_origin/sims))

# According to Polya's Theorem of random walks, random 3D walks have a 34% of returning
# back to their start. My sim with current parameters returns 33.6%, but as runtime increases
# it converges on 34%