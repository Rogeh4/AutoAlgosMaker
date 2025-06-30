from OpenRouterFuncs import make_answer_string
from ParserFuncs import *
from utilits import create_file
import os

def main(surname, main_folder= "result", log=False):
    if log: print("started main")
    # Создаем основную папку для всех лаб
    if not os.path.exists(main_folder):
        os.makedirs(main_folder)

    # Получаем ссылки на каждую лабораторную urls - словарь вида lab_num : url
    urls = get_urls()
    if log:
        print("urls: ")
        for i in urls:
            print(f"{i} : {urls[i]}")
    # Перебираем все ссылки в urls
    for lab_num, url in urls.items():
        # название директории со всеми заданиями (теперь внутри основной папки)
        filename = os.path.join(main_folder, str(lab_num) + "_" + surname)

        if log: print(f"\nLab {lab_num}: {url} Parsing...\n\n")

        # Достаем текст всей лабы, доп условие (requirements) и дробим текст на задания
        text = url_parser(url)
        requirements = make_requirements(text)
        tasks = make_tasks(text)

        if log: print(f"Lab {lab_num} Parsing Complete:\n"
                      f"Tasks: {list(tasks.keys())}\n"
                      f"Requirements: {requirements}\n")

        # Создаем папку для лабы, если ее нет
        if not os.path.exists(filename):
            os.makedirs(filename)

        # Решаем по очереди задачи, если уже есть то пропускаем
        for task_name, task in tasks.items():
            if log: print(f"Solving Task ({task_name})...")
            task_path = os.path.join(filename, task_name)
            if os.path.exists(task_path):
                if log: print(f"Lab {lab_num}: {task_name} Already Exists\n")
                continue
            answer = make_answer_string(task, requirements)

            if log: print(f"Task Solved\n")

            create_file(filename, task_name, answer)


if __name__ == "__main__":
    log = bool(input("Нажмите enter что бы отключить логи"))
    main_folder = input("Введите название папки с ответами")
    surname = input("Введите вашу фамилию")
    main(surname, main_folder=main_folder, log=log)
