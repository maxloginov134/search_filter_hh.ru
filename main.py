import pathlib

from classes.database import DBManager
from classes.headhunter import HeadHunter
from utils.config import config
from utils.utils import read_file
dir_path = pathlib.Path.cwd()
PATH_TO_DB_CONFIG = pathlib.Path(dir_path, 'data_files', 'database.ini')
PATH_TO_EMP_JSON = pathlib.Path(dir_path, 'data_files', 'employers.json')


def main():
    print('Добро пожаловать в сервис вакансий компаний: Альфа-банк,  Сбер,  Тинькофф,  Ozon,  Газпром,  Почта,'
          '  Яндекс,  Metro,  ВТБ,  Северсталь')
    print()
    print('Ожидайте, база данных создается...')
    params = config(PATH_TO_DB_CONFIG)
    db = DBManager('vacancies_db', params)

    db.create_database()
    employers = read_file(PATH_TO_EMP_JSON)
    db.insert_to_employers(employers)

    for i in range(len(employers)):
        head_hunter = HeadHunter(employers[i][0]).get_vacancies()
        db.insert_to_vacancies(head_hunter)
    print('База данных создана')
    while True:
        print('Введите цифру согласно меню')
        print(f"""
        1. Получить список всех компаний и количество вакансий у каждой компании
        2. Получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
        3. Получить среднюю зарплату по вакансиям
        4. Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям
        5. получает список всех вакансий, в названии которых содержатся слово
        0. Выход из программы""")
        print()
        user_input = input('Введите цифру: ')
        if user_input == '1':
            db.get_companies_and_vacancies_count()
        elif user_input == '2':
            db.get_all_vacancies()
        elif user_input == '3':
            db.get_avg_salary()
        elif user_input == '4':
            db.get_vacancies_with_higher_salary()
        elif user_input == '5':
            word_input = input('Введите слово: ')
            db.get_vacancies_with_keyword(word_input)
        elif user_input == '0':
            break
        else:
            print('Некорректный ввод')


if __name__ == '__main__':
    main()
