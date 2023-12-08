"""Day four"""
from collections import defaultdict
import helper
import numpy as np


def day_4_0():
    """Solve first task"""
    data: list = helper.parse_input("source")
    games: dict = {int(game.split(":")[0].split(" ")[-1]): [game.split(":")[1].split("|")[0],
                                                            game.split(":")[1].split("|")[1]] for game in data}
    for game in games:
        games[game][0] = [x.strip() for x in games[game][0].split(" ") if x]
        games[game][1] = [x.strip() for x in games[game][1].split(" ") if x]
        count: int = len([i for i in games[game][0] if i in games[game][1]])
        value: int = 0 if not count else 1
        for val in range(1, count):
            value *= 2
        games[game].append(value)
    result: int = 0
    for game in games:
        result += games[game][2]

    return result

def day_4_1():
    """Solve first task"""
    data: list = helper.parse_input("source")
    games: dict = {int(game.split(":")[0].split(" ")[-1]): [game.split(":")[1].split("|")[0],
                                                            game.split(":")[1].split("|")[1], 1] for game in data}
    print(games)
    full_stop: bool = False
    count = 0
    for game in games:
        games[game][0] = [x.strip() for x in games[game][0].split(" ") if x]
        games[game][1] = [x.strip() for x in games[game][1].split(" ") if x]
        value: list = [len([i for i in games[game][0] if i in games[game][1]])]
        for a in range(games[game][2]):
            for i in range(1, value[0] + 1):
                check = True
                if game + 1 < len(games):
                    games[game + i][2] += 1
                    check &= bool(len([i for i in games[game][0] if i in games[game][1]]))
                full_stop = False if check else True
            if full_stop:
                break
    result: list = [0]
    for game in games:
        result[0] += games[game][2]
    print(games)
    return result


if __name__ == "__main__":
    # print(day_4_0())
    print(day_4_1())
