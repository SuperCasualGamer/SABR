import csv
from collections import defaultdict

with open('results.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = [row for row in csv_reader]
    data[0][0] = 'Lamar'
    
    results = defaultdict(int)
    for player in data[0]:
        results[player] += 1
    
    
    def print_data(data: list):
        if len(data) > 1 and type(data) == list: 
            for item in data[:-1]:
                print(item, end=' ')
            print(data[-1])
        elif len(data) == 1:
            print(data[0])
        else:
            print(data)
    
    def plurality(data):
        return max(results, key = lambda x: results[x])
    
    def majority(data: list):
        result = []
        for player, freq in results.items():
            if freq > len(data[0])//2:
                result.append(player)
        return result
    
    def runoff(data: list):
        return sorted(results.keys(), key = lambda x: results[x], reverse=True)[:1]
    
    def borda(data: list):
        borda_results = defaultdict(int)
        for row in range(len(data)):
            for i, player in enumerate(data[row]):
                borda_results[player] += 5 - row
        sorted_results = sorted(borda_results.keys(), key = lambda x: borda_results[x], reverse=True)[:2]
        return sorted_results[results[sorted_results[0]] < results[sorted_results[1]]]
    print("Election Results:")
    print_data(plurality(data))
    print_data(majority(data))
    print_data(runoff(data))
    print_data(borda(data))
    print('\n')
    print("Barkeley thinks he should win because he has the most number of first place votes.")
    print("Based on the voting system I think the winner should have been Magic Johnson.")
    print("Sir Charles was the winner when calculating the runoff like a normal Borda count.")
    print("Borda meant that the most number of 1st places does not mean you win.")
    print("The would be the Chiefs in the approval voing data set.")
    print("a. They equally approve of all the teams and don't really effect the outcome.")
    print("b. They approve of none of the teams and also don't really effect the outcome.")
    print("Ichiro Suzuki, CC Sabanthia, and Billy Wagner will be elected to the hall of fame because they were in 75% or more of the 394 votes.")