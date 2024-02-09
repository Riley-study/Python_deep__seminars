fn1 = 'def get_dir_size():'
fn2 = 'def save_results_to_json():'
fn3 = 'def save_results_to_csv():'
fn4 = 'def save_results_to_pickle():'
fn5 = 'def traverse_directory():'

with open('../__init__.py', 'w', encoding='utf-8') as file:
    file.write(fn1 + '\n')
    file.write(fn2 + '\n')
    file.write(fn3 + '\n')
    file.write(fn4 + '\n')
    file.write(fn5 + '\n')


