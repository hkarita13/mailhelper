import PyInstaller.__main__
import os

# Получаем путь к текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Пути к файлам
main_script = os.path.join(current_dir, 'main.py')

# Параметры компиляции
PyInstaller.__main__.run([
    'main.py',  # Основной скрипт
    '--name=MailingHelper',  # Имя выходного файла
    '--onefile',  # Создать один EXE файл
    '--noconsole',  # Без консольного окна
    '--add-data=fonts;fonts',  # Добавить папку со шрифтами
    '--clean',  # Очистить временные файлы
    '--windowed',  # Создать Windows приложение
    '--hidden-import=keyboard',  # Добавить скрытые импорты
    '--hidden-import=mouse',
    '--hidden-import=pyautogui',
    '--hidden-import=pandas',
    '--hidden-import=screeninfo',
]) 