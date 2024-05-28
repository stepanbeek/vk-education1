#12
def average(numbers):
    nums = [int(num) for num in numbers.split()]
    return sum(nums) / len(nums)

while True:
    sequence = input()
    if sequence == "":
        break
    print(average(sequence))

#13
def process_string(input_str):
    if input_str.startswith("!"):
        processed_str = input_str[1:].upper()
    else:
        processed_str = input_str.lower()

    processed_str = processed_str.replace("!", "").replace("@", "").replace("#", "").replace("%", "")

    return processed_str

while True:
    input_str = input()
    if input_str == "":
        break
    print(process_string(input_str))

#14
start = 1
end = 10
step = 2

seq = range(start, end, step)
result = map(lambda x: x ** 2 if x % 2 != 0 else -x, seq)

for res in result:
    print(res)

#15
fib_cache = {}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]

    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)

    fib_cache[n] = result
    return result

n = int(input())
print(fibonacci(n))

#16
def map_custom(func, seq):
    for item in seq:
        yield func(item)
func_in, seq_in = eval(input()), eval(input())

for x in map_custom(func_in, seq_in):
    print(x)

#17
def filter_custom(func, seq):
    for item in seq:
        if func(item):
            yield item
func_in, seq_in = eval(input()), eval(input())

for x in filter_custom(func_in, seq_in):
    print(x)

#18
def cache_deco(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

#19
def repeat_deco(n=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

#20
a = int(input())

def f():
    global a
    a += 10

f()

print(a)

#21
from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
    return sorted(d, key=d.get, reverse=True)

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

#22
def f():
    def g():
        b = int(input())
        def h():
            nonlocal b
            b += 10
        h()
        print(b)
    g()
f()

#23
from typing import List

def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    return [i for i, (n1, n2) in enumerate(zip(nums1, nums2)) if n1 < n2]

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)