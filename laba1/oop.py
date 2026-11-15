import sys
import math


class CoefficientReader:
    '''
    Класс, отвечающий только за получение корректных коэффициентов.
    '''

    @staticmethod
    def _try_parse(raw):
        try:
            return True, float(raw.replace(',', '.'))
        except (TypeError, ValueError):
            return False, None

    def read(self, name, argv_value=None):
        if argv_value is not None:
            ok, value = self._try_parse(argv_value)
            if ok:
                return value
            print(f"Коэффициент {name} в командной строке некорректен, "
                  f"введите заново.")

        while True:
            raw = input(f"Введите коэффициент {name}: ")
            ok, value = self._try_parse(raw)
            if ok:
                return value
            print("Ошибка: это не число. Попробуйте ещё раз.")


class BiquadraticEquation:
    '''

    Биквадратное уравнение A*x^4 + B*x^2 + C = 0.
    '''

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def _t_roots(self):
        """Корни квадратного уравнения относительно t = x^2."""
        a, b, c = self.a, self.b, self.c

        if a == 0:
            if b == 0:
                return []
            return [-c / b]

        d = b * b - 4 * a * c
        if d < 0:
            return []
        if d == 0:
            return [-b / (2 * a)]

        sqrt_d = math.sqrt(d)
        return [(-b - sqrt_d) / (2 * a), (-b + sqrt_d) / (2 * a)]

    def real_roots(self):
        result = []
        for t in self._t_roots():
            if t < 0:
                continue
            if t == 0:
                result.append(0.0)
            else:
                r = math.sqrt(t)
                result.extend([-r, r])

        # убираем дубликаты
        unique = []
        for r in result:
            if not any(abs(r - u) < 1e-9 for u in unique):
                unique.append(r)
        return sorted(unique)

    def __str__(self):
        return f"{self.a}x^4 + {self.b}x^2 + {self.c} = 0"


def main():
    argv = sys.argv[1:]
    reader = CoefficientReader()

    a = reader.read('A', argv[0] if len(argv) > 0 else None)
    b = reader.read('B', argv[1] if len(argv) > 1 else None)
    c = reader.read('C', argv[2] if len(argv) > 2 else None)

    equation = BiquadraticEquation(a, b, c)
    print(f"\nУравнение: {equation}")

    roots = equation.real_roots()
    if roots:
        print("Действительные корни:")
        for r in roots:
            print(f"  x = {r:.6f}")
    else:
        print("Действительных корней нет.")


if __name__ == "__main__":
    main()