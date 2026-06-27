"""7.

A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)"""
n = int(input("Enter number of players: "))

players = []

for i in range(n):
    player_id, player_name, runs = input().split()

    player = (int(player_id), player_name, int(runs))
    players.append(player)

print("\nAll Players:")
for player in players:
    print(player)

# Highest Scorer
highest = players[0]

for player in players:
    if player[2] > highest[2]:
        highest = player

print("\nHighest Scorer:")
print(highest)

# Lowest Scorer
lowest = players[0]

for player in players:
    if player[2] < lowest[2]:
        lowest = player

print("\nLowest Scorer:")
print(lowest)

# Total Runs
total_runs = 0

for player in players:
    total_runs += player[2]

print("\nTotal Runs:")
print(total_runs)

# Average Runs
average_runs = total_runs / n

print("\nAverage Runs:")
print(average_runs)

# Players scoring more than 50 runs
print("\nPlayers Scoring More Than 50 Runs:")
for player in players:
    if player[2] > 50:
        print(player)