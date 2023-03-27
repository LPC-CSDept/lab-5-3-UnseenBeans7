import random


def mineven(numbers):
    ##################################################
    # make your code
    ##################################################

    return minval


def main():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = mineven(numbers)
    print(numbers)
    print(result)

    numbers = [1, 3, 5, 7, 10, 14, 2, 8]
    result = mineven(numbers)
    print(numbers)
    print(result)

    N = random.randint(5, 20)
    numbers = [random.randint(-50, 50) for v in range(N)]
    print(numbers)
    result = mineven(numbers)
    print(numbers)
    print(result)


if __name__ == '__main__':
    main()
