import random
import main


def test_main():
    N = random.randint(5, 20)
    numbers = [random.randint(-50, 50) for v in range(N)]
    print('Original List', numbers)
    elst = [v for v in numbers if v % 2 == 0]
    target = min(elst)
    targetlen = len(numbers) - 1
    ret = main.mineven(numbers)
    print('Your function return this value: ', ret)
    print('After function call, Numbers: ', numbers)
    assert ret == target, 'Wrong return value '

    assert targetlen == len(numbers), 'The length of list is not correct'
