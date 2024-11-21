import random
from collections import defaultdict
import pandas as pd

def world_cup_simulator(games: int, teams: dict[str, float]) -> None:
    results = defaultdict(int)
    for _ in range(games):
        points = 0
        for _ in range(3):
            chance = random.random()
            outcome = []
            if chance <= teams["team1"]:
                points += 3
            elif chance >= teams["team2"] + teams["team1"]:
                points += 1
        results[points] += 1
        points = 0
    for key, item in results.items():
            results[key] = str(item/games * 100)[:5] + "%"
    print(pd.DataFrame(results.items(), columns = ["Points", "Chance"]).sort_values(by="Points").to_string(index=False))
        


if __name__ == "__main__":
    games = int(input("How many games would you like to simulate? "))
    team1 = float(input("What is the probability of team 1 winning? "))
    team2 = float(input("What is the probability of team 2 winning? "))
    world_cup_simulator(games, {"team1": team1, "team2": team2})
    