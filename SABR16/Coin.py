import random
import time
import sys
import pandas as pd

def type(phrase: str) -> None:
    for char in phrase:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def flipCoin(n: int) -> None:
    coins = {"Heads": 0, "Tails": 0}
    print("Flipping coins", end="")
    for _ in range(3):
        type(".")
        time.sleep(1)
    print("\n")
    for _ in range(n):
        coins[random.choice(["Heads", "Tails"])] += 1
    print(f"The coin was flipped {n} times and the results are Heads: {coins['Heads']} and Tails: {coins['Tails']}. The coin landed on tails {coins['Tails']/n*100}% of the time.")
    
if __name__ == "__main__":
    input = int(input("How many times would you like to flip the coin? "))
    flipCoin(input)