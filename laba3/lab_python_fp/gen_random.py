import random


def gen_random(num_count, begin, end):
    """Генератор num_count случайных целых чисел в [begin, end].

    Args:
        num_count (int): сколько чисел выдать
        begin (int): нижняя граница (включительно)
        end (int): верхняя граница (включительно)

    Yields:
        int: случайное число из диапазона
    """
    yield from (random.randint(begin, end) for _ in range(num_count))


if __name__ == '__main__':
    print('5 чисел от 1 до 3:')
    print(list(gen_random(5, 1, 3)))

    print('10 чисел от 1 до 100:')
    print(list(gen_random(10, 1, 100)))