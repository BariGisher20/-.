from pprint import pprint


nested_list = [
 ['a', 'b', 'c'],
 ['d', 'e', 'f', 'h', False],
 [1, 2, None],
]


def flat_generator(a: list) -> list:
    for item in a:
        for i in item:
            return i


for item in flat_generator(nested_list):
    pprint(item)
