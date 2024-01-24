# Напишите функцию key_params, принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def key_params(**kwargs) -> dict():
    dict_res = {}
    for key, value in kwargs.items():
        if isinstance(value, list | set | dict):
            dict_res[str(value)] = key
        else:
            dict_res[value] = key

    return dict_res



params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)


# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}