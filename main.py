import random


def mineven(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        
    minval = even_list[0]
    for num in even_list:
        if num < minval:
            minval = num
            
    del(numbers[numbers.index(minval)])
            
    

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
