import random

n = int(input("How many times would you like to run the simulation? "))

def simulate(n: int):
    perfect = 0
    for _ in range(n):
        outs = 0
        for _ in range(28):
            if random.random() >= 0.317:
                outs += 1
        if outs == 27:
            perfect += 1
            print(perfect)
    return perfect/n

#Usually 1 perfect game per season or a 0.0411522633744856% chance of having a perfect game.
print(simulate(n) * 100.0000)
