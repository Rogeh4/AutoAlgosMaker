import os

def get_str_interval(text, str_from, str_to):
    res = text.split(str_from)[1].split(str_to)[0]
    return res



def create_file(folder_path: str, filename: str, code: str) -> str:
    # Создаем папку
    os.makedirs(folder_path, exist_ok=True)
    full_path = os.path.join(folder_path, filename)

    # Сохраняем код
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(code)
    return full_path

if __name__ == '__main__':
    create_file("7_yurenka_", "hello", 'print("hello world")')