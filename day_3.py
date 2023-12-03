"""Day three"""
import helper
import numpy as np


def day_3_0():
    """Solve first task"""
    data: list = helper.parse_input("source_training", strip_lines=False)
    engine_data: np.array = populate_array(np.array(data))
    numbers: list = []
    where_am_i: list = [0, 0]
    for row in range(engine_data.shape[0]):
        for column in range(engine_data.shape[1]):
            if helper.is_it_int(engine_data[row][where_am_i[1]]):
                flag = False

                addition, location, flag = check_my_nbrs((row, where_am_i[1]+1), engine_data)
                numbers.append(engine_data[row][where_am_i[1]] + addition)
                where_am_i[1] += location
            where_am_i[1] += 1
            if where_am_i[1] >= engine_data.shape[1] - 1:
                break
        where_am_i[0] += 1
        where_am_i[1] = 0
    return numbers



def day_3_1():
    """Solve second task"""


def populate_array(data: np.array) -> np.array:
    """Populate numpy array.

    :param data: array for conversion
    """
    engine_data = np.empty((len(data), len(data[0][0])), dtype=str)
    for row in range(engine_data.shape[0]):
        for column in range(engine_data.shape[1]):
            engine_data[row][column] = data[row][0][column]
    return engine_data


def check_my_nbrs(start: tuple[int, int], array: np.array) -> [str, int, bool]:
    """Check if next cells contain int.

    :param start: starting cell
    :param array: np array for check
    """
    result: list = [""]
    location: int = 0
    flag: bool = False
    for column in range(start[1], array.shape[1]):
        if helper.is_it_int(array[start[0]][column]):
            result[0] = result[0] + array[start[0]][column]
            location += 1
        else:
            break
    return result[0], location, flag


def look_around(position: list[int, int], dimensions: tuple[int, int]) -> bool:
    """Look around and search for special chars.

    :param position: current position
    :param dimensions: boundaries for search
    """
    # if position[0]


if __name__ == "__main__":
    print(day_3_0())
