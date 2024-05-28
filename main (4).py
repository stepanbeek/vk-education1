#33
import os

text = input()

def write_and_read(text):
    file_path = os.path.join("/tmp", "temp_file.txt")
    
    # Write text to file
    with open(file_path, "w") as file:
        file.write(text)
    
    # Read text from file
    with open(file_path, "r") as file:
        text_from_file = file.read()
    
    # Remove the temporary file
    os.remove(file_path)
    
    return text_from_file

print(write_and_read(text))
#34
numerator, denominator = int(input()), int(input())

def changed_div(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return denominator
    else:
        return denominator / result

print(changed_div(numerator, denominator))
#36
from itertools import zip_longest
from typing import List, Tuple


def fill_missing_values(values_list_1: List[int], values_list_2: List[int]) -> List[Tuple[int, int]]:
    result = []
    for val1, val2 in zip_longest(values_list_1, values_list_2, fillvalue=1):
        result.append((val1, val2))
    return result


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
#37
import datetime

days, seconds = int(input()), int(input())

def shift_time(days: int, seconds: int):
    base_time = datetime.datetime(2023, 1, 1, 12, 30, 0)
    delta = datetime.timedelta(days=days, seconds=seconds)
    shifted_time = base_time + delta
    return shifted_time.day, shifted_time.second

print(shift_time(days, seconds))
#39
import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
    months = [int(date.split('-')[1]) for date in dates]
    month_counts = Counter(months)
    most_common = month_counts.most_common(n)
    return [month for month, _ in most_common]


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    queue = deque(nums)
    n = n % len(queue)  
        queue.appendleft(queue.pop())
    return list(queue)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

#40
from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    queue = deque(nums)
    n = n % len(queue)  # Если n больше длины списка, берем остаток от деления
    for _ in range(n):
        queue.appendleft(queue.pop())
    return list(queue)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)