import numpy as np


def read_input(input_file_dir):
    with open(input_file_dir, "r") as file:
        lines = file.readlines()

    arrays = list()
    for line in lines:
        current = np.fromstring(line, dtype=int, sep=" ")
        arrays.append(current)

    return np.array(arrays, dtype=object)


def is_safe(report):

    if len(report) == 1:
        return 1

    diffs = np.diff(report)

    is_asc = np.all(diffs >= 1) and np.all(diffs <= 3)
    is_desc = np.all(diffs <= -1) and np.all(diffs >= -3)

    if is_asc or is_desc:
        return 1
    else:
        return 0


def is_fault_tolerant(report):
    not_damped_safety_level = is_safe(report)

    if not_damped_safety_level == 0:
        for level in range(len(report)):
            if is_safe(np.delete(report, [level])):
                return 1
        return 0

    return not_damped_safety_level


def how_many_reports_are_safe(reports):
    return np.sum([is_safe(r) for r in reports])


def problem_dampener(reports):
    return np.sum([is_fault_tolerant(r) for r in reports])


input = read_input("Q2\input.txt")

print(how_many_reports_are_safe(input))
print(problem_dampener(input))
