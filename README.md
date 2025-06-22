## Для настройки проекта нам понадобятся: 
# PyCharm CE
Качаем последнюю версию под свою ОС PyCharm Community Edition
https://www.jetbrains.com/pycharm/download/other.html#version20243


# python 3.13
Настройка
1. Скачайте установщик:
Перейдите на официальный сайт Python: https://www.python.org/downloads/windows/. 
Найдите версию Python 3.13 и загрузите установщик для Windows (файл с расширением .exe). 
2. Запустите установщик:
Найдите скачанный файл и запустите его. 
3. Установка:
В установщике выберите "Customize installation" (или "Настроить установку") для более гибкой настройки, или "Install Now" (или "Установить сейчас") для установки по умолчанию. 
Обязательно отметьте галочку "Add Python to PATH": (или "Добавить Python в PATH"). Это позволит запускать Python из любой командной строки, включая PowerShell. 
Остальные настройки можно оставить по умолчанию, либо настроить по своему усмотрению. 
Нажмите "Install" (или "Установить"). 
4. Проверка установки:
Откройте PowerShell. 
Введите команду python --version (или python3 --version). 
Если Python установлен правильно, вы увидите версию Python 3.13. 
5. Установка pip (если не установлен):
Проверить можно набрав в командной строке pip --version
Pip, менеджер пакетов Python, обычно устанавливается вместе с Python, но если его нет, выполните команду в PowerShell: python -m ensurepip --upgrade.

# установка библиотек
Устанавливаем через менеджер пакетов pip в консоли IDE: `pip install pytest`, `pip install requests`
Устанавливаем Allure (для Windows) в консоли: `iwr -useb get.scoop.sh | iex` -> `scoop install allure`



## запуск тестов 
pytest -> старт всех тестов
allure serve ./ui_tests/reports -> формирование отчета аллюр из указанно папки