from pprint import pprint


nested_list = [
 ['a', 'b', 'c'],
 ['d', 'e', 'f', 'h', False],
 [1, 2, None]
]


class MyList:
    def __init__(self, main_list):
        self.main_list = main_list

    def __iter__(self):
        self.main_list_cursor = -1
        self.inner_list_cursor = -1
        return self

    def __next__(self):
        self.inner_list_cursor += 1
        if self.inner_list_cursor == len(self.main_list[self.main_list_cursor]):
            self.main_list_cursor += 1
            self.inner_list_cursor = 0
        if self.main_list_cursor == len(self.main_list):
            raise StopIteration
        return self.main_list[self.main_list_cursor][self.inner_list_cursor]


flat_list = []
for item in MyList(nested_list):
    flat_list.append(item)
pprint(flat_list)


