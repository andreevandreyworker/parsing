import requests
from bs4 import BeautifulSoup


def get_departments(url):
    # Выполняем GET-запрос к указанному URL
    response = requests.get(url)

    # Проверяем, успешен ли запрос
    if response.status_code != 200:
        print(f"Ошибка при получении данных: {response.status_code}")
        return []

    # Парсим HTML-код страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все элементы, содержащие названия кафедр
    # Предположим, что кафедры находятся в элементах <li> с классом "department"
    departments = soup.find_all('div', class_='main__content')

    # Извлекаем текст из найденных элементов
    department_names = [dept.get_text(strip=True) for dept in departments]

    return department_names


def save_departments_to_file(departments, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for department in departments:
            file.write(department + ' ' + "\n")


if __name__ == "__main__":
    url = 'https://omgtu.ru/general_information/the-structure/the-department-of-university.php'  # Замените на актуальный URL
    departments = get_departments(url)

    if departments:
        save_departments_to_file(departments, 'departments.txt')
        print(f"Список кафедр сохранен в файл 'departments.txt'.")
    else:
        print("Кафедры не найдены.")