"""Day five"""
from collections import defaultdict
import helper
from itertools import groupby
import string


def day_5_0():
    """Solve first task"""
    data: list = helper.parse_input("source")
    seeds: list = data.pop(0).split(" ")[1:]
    data = [list(group) for k, group in groupby(data, bool) if k]
    seed_to_soil: list = [coord.split(" ") for coord in data.pop(0) if coord[0] not in string.ascii_letters]
    soil_to_fertilizer: list = [coord.split(" ") for coord in data.pop(0) if coord[0] not in string.ascii_letters]
    fertilizer_to_water: list = [coord.split(" ") for coord in data.pop(0) if coord[0] not in string.ascii_letters]
    water_to_light: list = [coord.split(" ") for coord in data.pop(0) if coord[0] not in string.ascii_letters]
    light_to_tem: list = [coord.split(" ") for coord in data.pop(0) if coord[0] not in string.ascii_letters]
    temp_to_humidity: list = [coord.split(" ") for coord in data.pop(0) if coord[0] not in string.ascii_letters]
    humidity_to_loc: list = [coord.split(" ") for coord in data.pop(0) if coord[0] not in string.ascii_letters]
    locs: list = []
    for seed in seeds:
        soil = checker(seed_to_soil, int(seed))
        fert = checker(soil_to_fertilizer, int(soil))
        water = checker(fertilizer_to_water, int(fert))
        light = checker(water_to_light, int(water))
        temp = checker(light_to_tem, int(light))
        hum = checker(temp_to_humidity, int(temp))
        locs.append(checker(humidity_to_loc, int(hum)))
    return min(locs)


def checker(data: list, item: int) -> int:
    """Data checker"""
    for line in data:
        if int(line[1]) <= item < int(line[1]) + int(line[2]):
            return item + (int(line[0]) - int(line[1]))
    return item


if __name__ == "__main__":
    print(day_5_0())
