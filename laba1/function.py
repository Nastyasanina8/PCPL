import sys
import math


def parse_real(raw):
    """Возвращает кортеж (True, число) либо (False, None)."""
    try:
        return True, float(raw.replace(',', '.'))
    except (TypeError, ValueError):
        return False, None


def read_coefficient(name, argv_value=None):
    """Функция ввода коэффициента. Возвращает число (неизменяемое)."""
    if argv_value is not None:
        ok, value = parse_real(argv_value)
        if ok:
            return value
        print(f"Коэффициент {name} в командной строке некорректен, "
              f"введите заново.")

    while True:
        raw = input(f"Введите коэффициент {name}: ")
        ok, value = parse_real(raw)
        if ok:
            return value
        print("Ошибка: это не число. Попробуйте ещё раз.")


def solve_in_t(a, b, c):
    discriminant = b * b - 4 * a * c

    kind = (
        "degenerate_zero"     if a == 0 and b == 0 else
        "degenerate_linear"   if a == 0 else
        "negative"            if discriminant < 0 else
        "zero"                if discriminant == 0 else
        "positive"
    )

    match kind:
        case "degenerate_zero":
            # 0*x^4 + 0*x^2 + C = 0 — либо нет корней, либо любое x
            return () if c != 0 else ()
        case "degenerate_linear":
            return (-c / b,)
        case "negative":
            return ()
        case "zero":
            return (-b / (2 * a),)
        case "positive":
            sqrt_d = math.sqrt(discriminant)
            return ((-b - sqrt_d) / (2 * a), (-b + sqrt_d) / (2 * a))
        case _:
            raise ValueError(f"Неизвестный случай: {kind}")


def t_to_x(t):
    """Преобразует один корень по t в кортеж корней по x."""
    match t:
        case t if t < 0:
            return ()
        case 0:
            return (0.0,)
        case _:
            r = math.sqrt(t)
            return (-r, r)


def real_roots(a, b, c):
    """Композиция функций: solve_in_t -> map(t_to_x) -> flatten -> unique -> sort."""
    t_roots = solve_in_t(a, b, c)
    x_roots = sum(map(t_to_x, t_roots), ())

    # фильтрация дубликатов функционально: оставляем те, что не встречались раньше
    unique = tuple(
        r for i, r in enumerate(x_roots)
        if all(abs(r - prev) > 1e-9 for prev in x_roots[:i])
    )
    return tuple(sorted(unique))


def main():
    argv = sys.argv[1:]
    a = read_coefficient('A', argv[0] if len(argv) > 0 else None)
    b = read_coefficient('B', argv[1] if len(argv) > 1 else None)
    c = read_coefficient('C', argv[2] if len(argv) > 2 else None)

    print(f"\nУравнение: {a}x^4 + {b}x^2 + {c} = 0")

    roots = real_roots(a, b, c)

    match roots:
        case ():
            print("Действительных корней нет.")
        case _:
            print("Действительные корни:")
            for r in roots:
                print(f"  x = {r:.6f}")


if __name__ == "__main__":
    main()