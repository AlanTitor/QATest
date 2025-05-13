## Тестовое задание

## Описание

Данный проект содержит решения тестового задания, состоящего из двух частей. Код сознательно упрощен для лучшей читаемости и демонстрации базовой функциональности.

## Содержание проекта

1. **`alg.py`** - Реализация задач по работе с алгоритмами:
    - Фильтрация четных чисел
    - Поиск максимума и минимума
    - Сортирофка пузырьком

2. **`auto_test.py`** - Автоматизированный тест с использованием Selenium:
    - Проверка заголовка страницы
    - Работа с элементами DOM
    - Верификация URL

## Требования

- Python 3.9+
- Браузер Google Chrome
- ChromeDriver (Совместимая версия с вашим Chrome)

## Установка

1. **Клонирование репозитория**
    - git clone <https://github.com/AlanTitor/QATest>

2. **Установка и активация venv**
Для безопастной работы рекомендуется создать у себя на ПК venv окружение и запускать код из под него.

Windows
- py -m venv venv
- venv/Scripts/activate

Linux
- python3 -m venv venv
- venv/bin/activate

(На linux возможно придется так же еще и установить сам venv командой sudo apt install -y python3-venv)

3. **Установка зависимостей и запуск кода**

Установка selenium
- pip install selenium=4.32.0

Запуск alg.py

Windows
- py alg.py

Linux
- python3 alg.py

Запуск auto_test.py

Windows
- py auto_test.py

Linux
- python3 auto_test.py
