## Для настройки проекта нам понадобятся:

# PyCharm CE
Качаем последнюю версию под свою ОС PyCharm Community Edition
https://www.jetbrains.com/pycharm/download/other.html#version20243

# install git
## for linux
Терминал: `$ sudo apt install git`

## for mac
Терминал: `$ git --version` (если он не установлен, то система сама предложит установить его)

## for windows
Для установки Git в Windows также имеется несколько способов. Официальная сборка доступна для скачивания на официальном
сайте Git. Просто перейдите на страницу https://git-scm.com/download/win, и загрузка запустится автоматически. Обратите
внимание, что это отдельный проект, называемый Git для Windows; для получения дополнительной информации о нём перейдите
на https://gitforwindows.org.
Для автоматической установки вы можете использовать
пакет [Git Chocolatey](https://community.chocolatey.org/packages/git). Обратите внимание, что пакет Chocolatey
поддерживается сообществом.

# git clone project
В консоли git/терминале: `git clone https://github.com/KostyaShorokhov/PythonProject.git`
Или в самой ide file -> project from version control ->
подставялем https://github.com/KostyaShorokhov/PythonProject.git -> указываем директорию куда сокпировать -> clone

# python 3.13

## for windows
1. Скачайте установщик:
   Перейдите на официальный сайт Python: https://www.python.org/downloads/windows/.
   Найдите версию Python 3.13 и загрузите установщик для Windows (файл с расширением .exe).
2. Запустите установщик:
   Найдите скачанный файл и запустите его.
3. Установка:
   В установщике выберите "Customize installation" (или "Настроить установку") для более гибкой настройки, или "Install
   Now" (или "Установить сейчас") для установки по умолчанию.
   Обязательно отметьте галочку "Add Python to PATH": (или "Добавить Python в PATH"). Это позволит запускать Python из
   любой командной строки, включая PowerShell.
   Остальные настройки можно оставить по умолчанию, либо настроить по своему усмотрению.
   Нажмите "Install" (или "Установить").
4. Проверка установки:
   Откройте PowerShell.
   Введите команду python --version (или python3 --version).
   Если Python установлен правильно, вы увидите версию Python 3.13.
5. Установка pip (если не установлен):
   Проверить можно набрав в командной строке pip --version
   Pip, менеджер пакетов Python, обычно устанавливается вместе с Python, но если его нет, выполните команду в
   PowerShell: python -m ensurepip --upgrade.

## for mac
Установка через brew (вообще в этом случае имеет смысл им и пользоваться в любых программах, простой и легкий способ
установки программ)
Установить homebrew
В терминале выполнить команду:
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
Далее используем brew для установки python: `brew install python`.
Проверка установленной версии: `python --version` -> Python {version}

## for linux
Большинство дистрибутивов Linux поставляются с предустановленным Python, но если его нет или установлена устаревшая
версия, выполните следующие шаги:
Ubuntu / Debian. Откройте терминал и выполните следующую команду: `sudo apt update && sudo apt install python3`. Проверка
установленной версии: `python --version` -> Python {version}
Fedora / CentOS. Используя стандартный менеджер пакетов, выполните: `sudo dnf install python3`. Проверка установленной
версии: `python --version` -> Python {version}

# установка библиотек
Устанавливаем через менеджер пакетов pip в консоли IDE: `pip install pytest`, `pip install requests`
Устанавливаем Allure (для Windows) в консоли: `iwr -useb get.scoop.sh | iex` -> `scoop install allure`

## запуск тестов
pytest -> старт всех тестов
allure serve ./ui_tests/reports -> формирование отчета аллюр из указанно папки