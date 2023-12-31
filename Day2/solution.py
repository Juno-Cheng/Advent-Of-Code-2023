import string
import random

mapping = {
        "blue": 14, "red": 12, "green": 13
    }

#=================================Part 1===================================
def parse_game_data(game_data):
    games = {}
    for line in game_data.split('\n'):
        if not line.strip():
            continue
        game_id, subsets = line.split(':')
        print(f"Game_id = {game_id} : Subset = {subsets}")

        game_id = int(game_id.split()[1])
        subsets = subsets.split(';')
        print(f"Line = {line} : Game_id = {game_id} : Subset = {subsets}")
        games[game_id] = [subset.strip() for subset in subsets]
    print(f"Games = {games}")
    return games

def is_game_possible(game, red, green, blue):
    for subset in game:
        counts = {'red': 0, 'green': 0, 'blue': 0}
        for color_count in subset.split(','):
            count, color = color_count.strip().split()
            counts[color] += int(count)
            if counts['red'] > red or counts['green'] > green or counts['blue'] > blue:
                return False
    return True

def sum_possible_game_ids(game_data, red, green, blue):
    games = parse_game_data(game_data)
    total = 0
    for game_id, game in games.items():
        if is_game_possible(game, red, green, blue):
            total += game_id
    return total


#=================================Part 2===================================

def parse_game_data(game_data):
    games = {}
    for line in game_data.strip().split('\n'):
        game_id, subsets = line.split(':')
        game_id = int(game_id.split()[1])
        subsets = [subset.strip() for subset in subsets.split(';')]
        games[game_id] = subsets
    return games

def find_minimum_cubes(games):
    min_cubes = {}
    for game_id, subsets in games.items():
        counts = {'red': 0, 'green': 0, 'blue': 0}
        for subset in subsets:
            for color_count in subset.split(','):
                count, color = map(str.strip, color_count.split())
                counts[color] = max(counts[color], int(count))
        min_cubes[game_id] = counts
    return min_cubes

def calculate_power_and_sum(game_data):
    games = parse_game_data(game_data)
    min_cubes = find_minimum_cubes(games)
    total_power = 0
    for counts in min_cubes.values():
        power = counts['red'] * counts['green'] * counts['blue']
        total_power += power
    return total_power


#=================================Main===================================
game_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
 
total_power = calculate_power_and_sum(game_data)
print(f"The total power is: {total_power}")