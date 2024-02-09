# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями. В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.
import csv
import json


def csv_to_json_v2(csv_in: str, json_out: str):
    with (
        open(csv_in, 'r', newline='', encoding='utf-8') as f_in,
        open(json_out, 'w', encoding='utf-8') as f_out
    ):
        data = csv.reader(f_in)
        all_data = []
        for en, lst in enumerate(data):
            if en == 0:
                continue
            l, i, n = lst
            all_data.append({
                'level': l,
                'id': f'{i:>010}', # i.zfill(10)
                'name': n.capitalize(),
                'hash': hash(i+n)
            })
        print(all_data)
        json.dump(all_data, f_out, indent=4)


# красивая и универсальная функция, оставлю на память
def csv_to_json(csv_in: str, json_out: str):
    with (
        open(csv_in, 'r', newline='', encoding='utf-8') as f_in,
        open(json_out, 'w', encoding='utf-8') as f_out
    ):
        data = csv.reader(f_in)
        all_data = []
        for en, lst in enumerate(data):
            if en == 0:
                field_names = lst
                continue
            all_data.append(
                dict(zip(field_names, lst))
            )
        print(all_data)
        json.dump(all_data, f_out, indent=4)


if __name__ == '__main__':
    csv_to_json_v2('data_task3.csv', 'data_task4.json')
