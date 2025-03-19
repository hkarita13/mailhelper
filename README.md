# Mailing Helper (Помощник для рассылок) v0.2 (HKMH0.2)

## Описание
Mailing Helper - это программа для автоматизации действий с почтовыми рассылками. Она позволяет записывать последовательность действий пользователя и воспроизводить их для автоматизации рутинных задач.

## Возможности
- Запись действий пользователя (клики мыши, нажатия клавиш)
- Воспроизведение записанных действий
- Работа с CSV файлами (построчный ввод с шаблонами)
- Двуязычный интерфейс (русский/английский)
- Уникальный шрифт Fifaks для лучшей читаемости
- Поддержка горячих клавиш

## Требования к системе
- Windows 10/11
- Microsoft Visual C++ Redistributable (скачать: https://aka.ms/vs/17/release/vc_redist.x64.exe)

## Установка
1. Скачайте последнюю версию программы (HKMH0.2.exe) из раздела Releases
2. Распакуйте архив в удобное место
3. Убедитесь, что установлен Microsoft Visual C++ Redistributable
4. Запустите HKMH0.2.exe

## Использование
### Основные функции
1. **Запись действий (F6)**
   - Нажмите F6 для начала записи
   - Выполните необходимые действия
   - Нажмите F6 снова для остановки записи

2. **Работа с CSV**
   - Выберите CSV файл
   - Укажите нужные столбцы
   - Создайте шаблон с переменными {{column_name}}
   - Выберите режим выполнения:
     * Один раз (первая строка)
     * Итерации (указанное количество строк)
     * Цикл (все строки по порядку)

3. **Режимы выполнения**
   - Один раз - выполнение сценария один раз
   - Итерации - выполнение сценария указанное количество раз
   - Цикл - бесконечное повторение сценария

4. **Переключение языка**
   - В интерфейсе доступен переключатель языка
   - Поддерживаются русский и английский языки

### Горячие клавиши
- F6 - Начать/Остановить запись
- Esc - Экстренная остановка сценария

### Управление сценарием
- Добавление действий через выпадающий список
- Перетаскивание действий для изменения порядка
- Двойной клик для редактирования
- Кнопка удаления для удаления выбранного действия

## Решение проблем
Если программа не запускается:
1. Убедитесь, что установлен Microsoft Visual C++ Redistributable
2. Проверьте, не блокирует ли антивирус
3. Попробуйте запустить от имени администратора

## Разработка
### Структура проекта
- `main.py` - точка входа программы
- `gui.py` - графический интерфейс
- `logic.py` - логика работы с действиями
- `build.py` - скрипт сборки EXE
- `fonts/` - папка со шрифтами
- `requirements.txt` - зависимости проекта

### Сборка из исходного кода
1. Клонируйте репозиторий
2. Установите зависимости: `pip install -r requirements.txt`
3. Установите PyInstaller: `pip install pyinstaller`
4. Запустите сборку: `python build.py`
5. Готовый EXE будет в папке `dist`

## Благодарности
- Дизайн интерфейса основан на [cs16.css](https://github.com/ekmas/cs16.css)
- Шрифт Fifaks 1.0 dev1 взят с [fonts-online.ru](https://fonts-online.ru/fonts/fifaks-10-dev1)

## Автор
Создано Hidetoshi Karita

---

# Mailing Helper v0.2 (HKMH0.2)

## Description
Mailing Helper is a program for automating mailing-related actions. It allows recording user actions and playing them back to automate routine tasks.

## Features
- Record user actions (mouse clicks, keyboard presses)
- Play back recorded actions
- CSV file support (line-by-line input with templates)
- Bilingual interface (Russian/English)
- Unique Fifaks font for better readability
- Hotkey support

## System Requirements
- Windows 10/11
- Microsoft Visual C++ Redistributable (download: https://aka.ms/vs/17/release/vc_redist.x64.exe)

## Installation
1. Download the latest version (HKMH0.2.exe) from Releases section
2. Extract the archive to a convenient location
3. Make sure Microsoft Visual C++ Redistributable is installed
4. Run HKMH0.2.exe

## Usage
### Main Functions
1. **Record Actions (F6)**
   - Press F6 to start recording
   - Perform necessary actions
   - Press F6 again to stop recording

2. **Working with CSV**
   - Select CSV file
   - Choose required columns
   - Create template with {{column_name}} variables
   - Select execution mode:
     * Once (first row)
     * Iterations (specified number of rows)
     * Loop (all rows in sequence)

3. **Execution Modes**
   - Once - single execution of the scenario
   - Iterations - executing the scenario a specified number of times
   - Loop - infinite repetition of the scenario

4. **Language Switch**
   - Language switcher available in the interface
   - Supports Russian and English languages

### Hotkeys
- F6 - Start/Stop recording
- Esc - Emergency stop of the scenario

### Scenario Management
- Adding actions through the dropdown list
- Drag and drop actions to change order
- Double-click to edit
- Delete button to remove selected action

## Troubleshooting
If the program doesn't start:
1. Make sure Microsoft Visual C++ Redistributable is installed
2. Check if antivirus is blocking it
3. Try running as administrator

## Development
### Project Structure
- `main.py` - program entry point
- `gui.py` - graphical interface
- `logic.py` - action handling logic
- `build.py` - EXE build script
- `fonts/` - fonts folder
- `requirements.txt` - project dependencies

### Building from Source
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Install PyInstaller: `pip install pyinstaller`
4. Run build: `python build.py`
5. The EXE will be in the `dist` folder

## Acknowledgments
- Interface design is based on [cs16.css](https://github.com/ekmas/cs16.css)
- Fifaks 1.0 dev1 font is taken from [fonts-online.ru](https://fonts-online.ru/fonts/fifaks-10-dev1)

## Author
Created by Hidetoshi Karita 