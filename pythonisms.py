from functools import wraps
from time import sleep


class LinkedList:
    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return value_generator()

    def __len__(self):
        return len(list(iter(self)))


def custom_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_value = func(*args, **kwargs)
        return f"This is my custom decorator: {original_value}."
    return wrapper


def procrastinator_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(4)
        return func(*args, **kwargs)
    return wrapper


def additional_custom_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_value = func(*args, **kwargs)
        return f"This is my second custom decorator: {original_value}."
    return wrapper


@procrastinator_decorator
@custom_decorator
@ additional_custom_decorator
def text_test(txt):
    return txt


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


def total_of_values(ll):
    current = ll.head
    total = 0
    while current:
        total += current.value
        current = current.next
    return total


if __name__ == '__main__':
    print(text_test("This is my testing text"))
    pass
    # def gen():
    #     for i in range(10):
    #         yield i
    # num_gen = gen()
    # try:
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    # except StopIteration:
    #     print('Done itterating')
    # print(next(num_gen))
    #
    # def gen2():
    #     i = 0
    #     while True:
    #         yield i
    #         i += 1
    # print(gen2)
    #
