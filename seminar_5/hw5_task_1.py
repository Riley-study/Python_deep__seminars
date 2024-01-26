# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# ('C:/Users/User/Documents/', 'example', '.txt')

# def get_file_info(file_path: str) -> tuple[str]:
#     first_split = file_path.split("/")
#     second_split = first_split.pop()
#     last_dot_index = second_split.rfind('.')
#     file_name = second_split[:last_dot_index]
#     file_extension = second_split[last_dot_index:]
#     if first_split:
#         path = '/'.join(first_split) + '/'
#     else:
#         path = ''
#     return (path, file_name, file_extension,)

def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)


# file_path = "C:/Users/User/Documents/example.txt"
# file_path = 'C:/Projects/project1/code/script.py'
# file_path = '/home/user/docs/my.file.with.dots.txt'
file_path = 'file_in_current_directory.txt'
# file_path = '/home/user/docs/my.file.with.dots.txt'
print(get_file_info(file_path))
