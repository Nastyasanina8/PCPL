import time
from contextlib import contextmanager


class cm_timer_1:
    """Контекстный менеджер на основе класса."""

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f'time: {elapsed:.1f}')
        return False


@contextmanager
def cm_timer_2():
    """Контекстный менеджер на основе contextlib.contextmanager."""
    start = time.time()
    yield                       
    elapsed = time.time() - start
    print(f'time: {elapsed:.1f}')


if __name__ == '__main__':
    from time import sleep

    with cm_timer_1():
        sleep(5.5)

    with cm_timer_2():
        sleep(5.5)