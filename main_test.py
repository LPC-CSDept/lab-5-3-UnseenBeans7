import random
import main


def mineven(numbers):
    evenlst = [v for v in numbers if v % 2 == 0]
    return min(evenlst)


def test_main():
    N = random.randint(5, 20)
    numbers = [random.randint(-50, 50) for v in range(N)]
    print(numbers)
    target = mineven(numbers)
    ret = main.mineven(numbers)
    print(ret)
    assert ret == target
