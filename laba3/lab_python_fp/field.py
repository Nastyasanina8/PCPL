def field(items, *args):
    """Генератор значений (или словарей значений) по заданным ключам.

    Args:
        items (list[dict]): список словарей
        *args (str): имена полей (минимум одно)

    Yields:
        Если передан один ключ — значения этого поля (None пропускается).
        Если передано несколько ключей — словари с этими полями
        (None-поля пропускаются, полностью пустой словарь не выдаётся).
    """
    assert len(args) > 0


    if len(args) == 1:
        key = args[0]
        for item in items:
            value = item.get(key)
            if value is not None:
                yield value
    else:
        keys = args
        for item in items:
            # собираем словарь только из тех полей, что есть и не None
            result = {key: item[key] for key in keys
                      if key in item and item[key] is not None}
            if result:          # если все поля были None — пропускаем элемент
                yield result



if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
    ]

    print('Одно поле:')
    print(list(field(goods, 'title')))

    print('Два поля:')
    print(list(field(goods, 'title', 'price')))

    print('Три поля (у второго товара нет price):')
    print(list(field(goods, 'title', 'price', 'color')))