import sys
import math


def get_coef(index, prompt):
    '''
    Args:
        index (int): номер параметра в командной строке (1, 2, 3)
        prompt (str): приглашение для ввода коэффициента

    Returns:
        float: коэффициент биквадратного уравнения
    '''
    # Пробуем взять из командной строки
    try:
        coef_str = sys.argv[index]
    except IndexError:
        coef_str = None

    # Если значение из argv некорректно — сообщаем и уходим в цикл ввода
    if coef_str is not None:
        try:
            return float(coef_str.replace(',', '.'))
        except ValueError:
            print(f'Значение "{coef_str}" в командной строке некорректно, '
                  f'введите коэффициент заново.')

    # Ввод с клавиатуры, пока не получим корректное число
    while True:
        print(prompt)
        coef_str = input()
        try:
            return float(coef_str.replace(',', '.'))
        except ValueError:
            print('Ошибка: это не число. Попробуйте ещё раз.')


def get_roots(a, b, c):
    '''
    Вычисление действительных корней биквадратного уравнения
        a*x^4 + b*x^2 + c = 0

    Args:
        a (float): коэффициент A
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: список действительных корней
    '''
    # 1) Замена t = x^2, решаем a*t^2 + b*t + c = 0
    t_roots = []
    if a == 0:
        if b != 0:
            t_roots.append(-c / b)
    else:
        D = b * b - 4 * a * c
        if D == 0.0:
            t_roots.append(-b / (2.0 * a))
        elif D > 0.0:
            sqD = math.sqrt(D)
            t_roots.append((-b + sqD) / (2.0 * a))
            t_roots.append((-b - sqD) / (2.0 * a))

    # 2) Из корней по t получаем корни по x, отбрасывая t < 0
    result = []
    for t in t_roots:
        if t < 0:
            continue
        if t == 0:
            result.append(0.0)
        else:
            r = math.sqrt(t)
            result.append(r)
            result.append(-r)

    # 3) Убираем дубликаты и сортируем
    unique = []
    for r in result:
        if not any(abs(r - u) < 1e-9 for u in unique):
            unique.append(r)
    return sorted(unique)


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент A:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    print(f'\nУравнение: {a}x^4 + {b}x^2 + {c} = 0')

    roots = get_roots(a, b, c)
    if len(roots) == 0:
        print('Нет действительных корней')
    else:
        print('Действительные корни:')
        for r in roots:
            print(f'  x = {r:.6f}')


if __name__ == "__main__":
    main()
