"""Day one"""
import helper


def day_1_0():
    """Solve first task"""
    lines = helper.parse_input("source")
    nmrs = []
    for line in lines:
        line_nmrs = [char for char in line if helper.is_it_int(char)]
        nmrs.append(line_nmrs)
    result = 0
    for digits in nmrs:
        result += int(digits[0] + digits[-1])
    return result


def day_1_1():
    """Solve first task"""
    lines = helper.parse_input("source")
    nmrs = []
    for line in lines:
        line = helper.word_to_digit_converter(line)
        line_nmrs = [char for char in line if helper.is_it_int(char)]
        nmrs.append(line_nmrs)
    result = 0
    for digits in nmrs:
        if digits:
            result += int(digits[0] + digits[-1])
    return result


if __name__ == "__main__":
    print(day_1_1())
