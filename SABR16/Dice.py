import random
import time
import sys
from collections import defaultdict
import pandas as pd

def type(phrase: str) -> None:
    for char in phrase:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
        
def rollDice(n: int, num_dice: int) -> None:
    rolls = defaultdict(int)
    print("Rolling Dice", end="")
    for _ in range(3):
        type(".")
        time.sleep(1)
    print("\n")
    for _ in range(n):
        curr = random.randint(1,6)
        for __ in range(num_dice - 1):
            curr += random.randint(1,6)
        rolls[curr] += 1
    if num_dice == 1:
        print(f"The dice was rolled {n} times and the dice landed on 7 {(rolls[7] / (n)) *100}% of the time. The results are as follows:")
    print(f"The dice were rolled {n} times and the dice landed on {max(rolls, key=rolls.get)} {(rolls[max(rolls, key=rolls.get)] / (n)) *100}% of the time. The results are as follows:")
    print(pd.DataFrame(rolls.items(), columns = ["Sum", "Frequency"]).sort_values(by="Sum").to_string(index=False))
    #The most common number is seven because it has the most combonations that add up to seven when two fair dice are rolled.
    
if __name__ == "__main__":
    num_dice = int(input("How many dice would you like to roll? "))
    input = int(input("How many times would you like to roll the dice? "))
    rollDice(input, num_dice)