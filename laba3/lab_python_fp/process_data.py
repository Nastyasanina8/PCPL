import json
import sys

from print_result import print_result
from cm_timer import cm_timer_1
from unique import Unique
from gen_random import gen_random

path = sys.argv[1] if len(sys.argv) > 1 else 'data_light.json'

with open(path, encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    """Отсортированный список профессий без повторов (регистр игнорируется)."""
    return sorted(Unique((item['job-name'] for item in arg), ignore_case=True), key=str.lower)


@print_result
def f2(arg):
    """Только профессии, начинающиеся со слова «программист»."""
    return list(filter(lambda s: s.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    """К каждой профессии добавляем «с опытом Python»."""
    return list(map(lambda s: f'{s} с опытом Python', arg))


@print_result
def f4(arg):
    """Генерируем зарплату 100 000–200 000 и присоединяем к названию."""
    arg = list(arg)
    salaries = gen_random(len(arg), 100000, 200000)
    return [f'{spec}, зарплата {sal} руб.' for spec, sal in zip(arg, salaries)]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))