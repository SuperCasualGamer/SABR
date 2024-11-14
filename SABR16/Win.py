import random
from collections import defaultdict
import pandas as pd

def chanceOfWinning(schedule: list[str], teams: dict) -> list:
    chance = []
    for team in schedule:
        chance.append((teams["Steelers"] + (1 - teams[team])) / 2)
    return chance
 
def simulateGame(schedule: list[str], teams: dict, n: int, wins: int) -> None:
    chances = chanceOfWinning(schedule, teams)
    outcomes = defaultdict(int)
    playoffs = 0
    # list of win chance of the steelers per team in schedule in order
    for _ in range(n):
        start = wins
        for chance in chances:
            if random.random() <= chance:
                wins += 1
        if wins >= 9:
            playoffs += 1
        outcomes[wins] += 1
        wins = start
    for key, item in outcomes.items():
        outcomes[key] = str(item/n*100)[0:5]
    print(f"The Steelers made the playoffs {playoffs} times out of the {n} simulations. Their chance of getting into the playoffs is {playoffs/n*100}%. The outcomes are as follows:")
    print(pd.DataFrame(outcomes.items(), columns = ["Outcome", "Frequency"]).sort_values(by="Outcome").to_string(index=False))
            
    
if __name__ == "__main__":
    teams = {"Steelers": 0.778, "Bengals": 0.400, "Browns": 0.222, "Ravens": 0.700, "Chiefs": 1.000, "Eagles": 0.778}
    schedule = ["Ravens", "Browns", "Bengals", "Browns", "Eagles", "Ravens", "Chiefs", "Bengals"]
    wins = int(input("How many wins do the Steelers have? "))
    input = int(input("How many times would you like to simulate the game? "))
    simulateGame(schedule, teams, input, wins)