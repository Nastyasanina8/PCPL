from gen_random import gen_random


class Unique(object):
    """Итератор, возвращающий только уникальные элементы.

    """

    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self._iterator = iter(items)
        self._seen = set()

    def _normalize(self, value):
        """Ключ для проверки на дубликат.

        """
        if self.ignore_case and isinstance(value, str):
            return value.lower()
        return value

    def __next__(self):
        while True:
            value = next(self._iterator)
            key = self._normalize(value)
            if key not in self._seen:
                self._seen.add(key)
                return value

    def __iter__(self):
        return self


if __name__ == '__main__':
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print('Список с повторами:')
    print(list(Unique(data1)))

    data2 = gen_random(10, 1, 3)
    print('Генератор случайных 1..3:')
    print(list(Unique(data2)))

    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print('Без ignore_case:')
    print(list(Unique(data3)))
    print('С ignore_case=True:')
    print(list(Unique(data3, ignore_case=True)))