from pprint import pprint


nested_list = [
 ['a', 'b', 'c'],
 ['d', 'e', 'f', 'h', False],
 [1, 2, None]
]


def flat_generator(main_list):
    for item in main_list:
        if isinstance(item, list):
            for value in flat_generator(item):
                yield value
        else:
            yield item


for item in flat_generator(nested_list):
    pprint(item)
