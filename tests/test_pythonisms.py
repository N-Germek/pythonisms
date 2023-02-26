import pytest

from pythonisms import LinkedList, text_test


# @pytest.mark.skip("pending")
def test_for_in():
    pets = LinkedList(('Kenda', 'Bean', 'Svemir'))
    pets_list = []
    for pet in pets:
        pets_list.append(pet)
    assert pets_list == ['Kenda', 'Bean', 'Svemir']


# @pytest.mark.skip("pending")
def test_list_comprehension():
    pets = LinkedList(('Kenda', 'Bean', 'Svemir'))
    capital_pets = [pet.upper() for pet in pets]
    assert capital_pets == ['KENDA', 'BEAN', 'SVEMIR']


def test_total_of_values():
    ll_values = LinkedList((1, 2, 3))
    ll_total = 0
    for i in ll_values:
        ll_total += i
    assert ll_total == 6


# @pytest.mark.skip("pending")
def test_list_cast():
    pets = ['Kenda', 'Bean', 'Svemir']
    pet = LinkedList(pets)
    assert list(pet) == pets


# @pytest.mark.skip("pending")
def test_range():
    num_range = range(1, 11)
    nums = LinkedList(num_range)
    assert len(nums) == 10


# @pytest.mark.skip("pending")
def test_filter():
    nums = LinkedList(range(1, 11))
    odds = [num for num in nums if num % 2]
    assert odds == [1, 3, 5, 7, 9]


# def test_filter():
#     nums = LinkedList(range(1, 10))
#     evens = [num for num in nums if num % 2]
#     assert evens == [2, 4, 6, 8]

# def custom_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         original_value = func(*args, **kwargs)
#         return f"This is my custom decorator: {original_value}."
#     return wrapper
def test_custom_decorator():
    pass


# @pytest.mark.skip("pending")
def test_next():
    pets = ['Svemir', 'Kenda', 'Bean']
    iterator = iter(pets)
    assert next(iterator) == 'Svemir'
    assert next(iterator) == 'Kenda'
    assert next(iterator) == 'Bean'


# @pytest.mark.skip("pending")
def test_stop_iteration():
    pets = LinkedList(['Svemir', 'Kenda', 'Bean'])
    iterator = iter(pets)
    with pytest.raises(StopIteration):
        while True:
            pets = next(iterator)


@pytest.mark.skip("pending")
def test_str():
    pets = LinkedList(['Svemir', 'Kenda', 'Bean'])
    assert str(pets) == '[ Svemir ] -> [ Kenda ] -> [ Bean ] -> None'


@pytest.mark.skip("pending")
def test_equals():
    lla = LinkedList(['Svemir', 'Kenda', 'Bean'])
    llb = LinkedList(['Svemir', 'Kenda', 'Bean'])
    assert lla == llb


@pytest.mark.skip("pending")
def test_get_item():
    animals = LinkedList(['Svemir', 'Kenda', 'Bean'])
    assert animals[0] == 'Pico'


@pytest.mark.skip("pending")
def test_get_item_out_of_range():
    animals = LinkedList(['Svemir', 'Kenda', 'Bean'])
    with pytest.raises(IndexError):
        animals[100]

