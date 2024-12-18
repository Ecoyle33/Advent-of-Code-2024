import re

"""Read file, extract the two numbers from the mul(x,y) section whenever a match is found via regex, move to the next section"""


def multiply(x, y):
    return x * y


def read_input(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()

    return lines


def sum_multiplication(memory):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    total = 0

    for element in memory:
        multiplication = re.findall(pattern, element)

        for x, y in multiplication:
            total += int(x) * int(y)
    return total


input_text = read_input("Q3\input.txt")

print(sum_multiplication(input_text))
