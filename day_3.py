"""Day three"""
from collections import defaultdict
import helper
import numpy as np


def day_3_0():
    """Solve first task"""
    data: list = helper.parse_input("source", strip_lines=False)
    engine_data: np.array = populate_array(np.array(data))
    numbers: list = []
    where_am_i: list[int, int] = [0, 0]
    for row in range(engine_data.shape[0]):
        for column in range(engine_data.shape[1]):
            if helper.is_it_int(engine_data[row][where_am_i[1]]):
                addition, location = check_my_nmrs((row, where_am_i[1] + 1), engine_data)
                flag = look_around(engine_data, where_am_i, location, engine_data.shape)
                if flag:
                    numbers.append(int(engine_data[row][where_am_i[1]] + addition))
                where_am_i[1] += location
            where_am_i[1] += 1
            if where_am_i[1] >= engine_data.shape[1] - 1:
                break
        where_am_i[0] += 1
        where_am_i[1] = 0
    print(numbers)
    return sum(numbers)


def day_3_1():
    """Solve second task"""
    data: list = helper.parse_input("source", strip_lines=False)
    engine_data: np.array = populate_array(np.array(data))
    numbers: list = []
    coords: defaultdict = defaultdict(list)
    where_am_i: list[int, int] = [0, 0]
    for row in range(engine_data.shape[0]):
        for column in range(engine_data.shape[1]):
            if helper.is_it_int(engine_data[row][where_am_i[1]]):
                addition, location = check_my_nmrs((row, where_am_i[1] + 1), engine_data)
                flags = look_around(engine_data, where_am_i, location, engine_data.shape, only_ast=True)
                if flags:
                    for flag in flags:
                        coords[flag].append(int(engine_data[row][where_am_i[1]] + addition))
                where_am_i[1] += location
            where_am_i[1] += 1
            if where_am_i[1] >= engine_data.shape[1] - 1:
                break
        where_am_i[0] += 1
        where_am_i[1] = 0
    for key in coords:
        if len(coords[key]) == 2:
            numbers.append((coords[key][0] * coords[key][1]))
    return sum(numbers)


def populate_array(data: np.array) -> np.array:
    """Populate numpy array.

    :param data: array for conversion
    """
    engine_data = np.empty((len(data), len(data[0][0])), dtype=str)
    for row in range(engine_data.shape[0]):
        for column in range(engine_data.shape[1]):
            engine_data[row][column] = data[row][0][column]
    return engine_data


def check_my_nmrs(start: tuple[int, int], array: np.array) -> [str, int, bool]:
    """Check if next cells contain int.

    :param start: starting cell
    :param array: np array for check
    """
    result: list = [""]
    location: int = 1
    for column in range(start[1], array.shape[1]):
        if helper.is_it_int(array[start[0]][column]):
            result[0] = result[0] + array[start[0]][column]
            location += 1
        else:
            break
    return result[0], location


def look_around(data: np.array, position: list[int, int], end: int, dim: tuple[int, int], only_ast: bool = False) \
        -> bool | list:
    """Look around and search for special chars.

    :param data: numpy array
    :param position: current position
    :param end: end position for y
    :param dim: boundaries for search
    :param only_ast: True if search only for asterix
    """
    coords = []
    mind_me: list = ["*"] if only_ast else [x for x in "@_!#$%^&*()<>?/|}{~:]+-="]
    x, y = position
    start_x = x - 1 if x > 1 else 0
    end_x = x + 2 if x + 2 < dim[0] else dim[0] - 1
    start_y = y - 1 if y > 1 else 0
    end_y = y + end + 1 if y + end + 1 < dim[1] else dim[1] - 1
    search_area = data[start_x: end_x, start_y:end_y]
    print(search_area)
    if only_ast:
        for row in range(search_area.shape[0]):
            for column in range(search_area.shape[1]):
                if search_area[row][column] == "*":
                    coords.append((row + start_x, column + start_y))
        return coords
    result = np.any(np.isin(mind_me, search_area))
    return result


if __name__ == "__main__":
    print(day_3_0())
    print(day_3_1())
