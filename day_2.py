"""Day two"""
import helper
import re


def day_2_0():
    """Solve first task"""
    id_sum: int = 0
    games: dict = {gms.split(":")[0]: gms.split(":")[1] for gms in helper.parse_input("source")}
    max_counts: dict = {"blue": 14,
                        "red": 12,
                        "green": 13
                        }
    for game in games:
        cubes: dict = {"blue": 0,
                       "red": 0,
                       "green": 0
                       }
        for draw in [x for x in re.split("[;,]", games[game]) if x]:
            value, key = draw.strip().split(" ")
            cubes[key] = int(value) if int(value) > cubes[key] else cubes[key]
        playable: bool = True if cubes["blue"] <= max_counts["blue"] and cubes["green"] <= max_counts["green"] \
                                 and cubes["red"] <= max_counts["red"] else False
        if playable:
            id_sum += int(game.split(" ")[1])
    return id_sum


def day_2_1():
    """Solve second task"""
    id_sum = 0
    games = {games.split(":")[0]: games.split(":")[1] for games in helper.parse_input("source")}
    for game in games:
        cubes = {"blue": 0,
                 "red": 0,
                 "green": 0
                 }
        for draw in [x for x in re.split(";", games[game]) if x]:
            for game_round in [x for x in re.split(",", draw) if x]:
                value, key = game_round.strip().split(" ")
                cubes[key] = int(value) if int(value) > cubes[key] else cubes[key]
        id_sum += (int(cubes["blue"]) * int(cubes["green"]) * int(cubes["red"]))
    return id_sum


if __name__ == "__main__":
    print(day_2_1())
