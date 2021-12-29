from typing import Any
from pprint import pprint


nested_list = [
 ['a', 'b', 'c'],
 ['d', 'e', 'f', 'h', False],
 [1, 2, None],
]


class MyList(list):
    def __iter__(self):
        self.main_cursor = -1
        return self

    def __next__(self):
        self.main_cursor += 1
        if len(self) == self.main_cursor:
            raise StopIteration
        return self[self.main_cursor]


class Item(list):
    def __iter__(self):
        self.inner_cursor = -1
        return self

    def __next__(self):
        self.inner_cursor += 1
        if len(self) == self.inner_cursor:
            raise StopIteration
        return str(self[self.inner_cursor])


my_list = MyList(nested_list)
flat_list = []
for item in my_list:
    my_item = Item(item)
    for i in item:
        # pprint(i)
        flat_list.append(i)
pprint(flat_list)


