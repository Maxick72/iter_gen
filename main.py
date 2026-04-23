# Домашнее задание к лекции 2. «Iterators. Generators. Yield»
import types
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor_list = 0
        self.cursor_element = -1
        return self

    def __next__(self):
        self.cursor_element += 1
        if self.cursor_element >= len(self.list_of_list [self.cursor_list]):
            self.cursor_list += 1
            self.cursor_element = 0
        if self.cursor_list >= len(self.list_of_list):
            raise StopIteration
        item =  self.list_of_list [self.cursor_list][self.cursor_element]
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()


def flat_generator(list_of_lists):

    for list_element in list_of_lists:
        for item in list_element:
            yield item


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
        flat_generator(list_of_lists_1),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
            assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


test_2()


class FlatIterator:
    def __init__(self, list_of_list):
        self.flat_list = []
        self._flatten(list_of_list)
        self.cursor = 0

    def _flatten(self, item):
        if isinstance(item, list):
            for sub_item in item:
                self._flatten(sub_item)
        else:
            self.flat_list.append(item)

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor >= len(self.flat_list):
            raise StopIteration

        result = self.flat_list[self.cursor]
        self.cursor += 1
        return result

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

if __name__ == '__main__':
    test_3()


def flat_generator2(list_of_lists):

    for list_element in list_of_lists:
        if isinstance(list_element, list):
            yield from flat_generator2(list_element)
        else:
            yield list_element

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator2(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator2(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator2(list_of_lists_2), types.GeneratorType)


test_4()


