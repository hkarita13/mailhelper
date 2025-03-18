# Mailing Helper (Помощник для рассылок)

## Описание
Mailing Helper - это программа для автоматизации действий с почтовыми рассылками. Она позволяет записывать последовательность действий пользователя и воспроизводить их для автоматизации рутинных задач.

## Возможности
- Запись действий пользователя (клики мыши, нажатия клавиш)
- Воспроизведение записанных действий
- Работа с Excel файлами
- Двуязычный интерфейс (русский/английский)
- Уникальный шрифт Fifaks для лучшей читаемости
- Поддержка горячих клавиш

## Требования к системе
- Windows 10/11
- Python 3.8 или выше
- Microsoft Visual C++ Redistributable (скачать: https://aka.ms/vs/17/release/vc_redist.x64.exe)

## Установка и сборка
### Сборка из исходного кода
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/mailing-helper.git
   cd mailing-helper
   ```

2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # для Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Соберите программу:
   ```bash
   python build.py
   ```

5. Готовый EXE файл будет находиться в папке `dist`

### Готовая версия
Если вы не хотите собирать программу самостоятельно, вы можете скачать готовый EXE файл из раздела Releases.

## Использование
### Основные функции
1. **Запись действий (F6)**
   - Нажмите F6 для начала записи
   - Выполните необходимые действия
   - Нажмите F6 снова для остановки записи

2. **Воспроизведение (F7)**
   - Нажмите F7 для воспроизведения записанных действий
   - Программа повторит все записанные действия в точности

3. **Работа с Excel**
   - Программа поддерживает работу с Excel файлами
   - Можно автоматизировать действия с данными из таблиц

4. **Переключение языка**
   - В интерфейсе доступен переключатель языка
   - Поддерживаются русский и английский языки

### Горячие клавиши
- F6 - Начать/Остановить запись
- F7 - Воспроизвести записанные действия

## Решение проблем
Если программа не запускается:
1. Убедитесь, что установлен Microsoft Visual C++ Redistributable
2. Проверьте, не блокирует ли антивирус
3. Попробуйте запустить от имени администратора
4. Проверьте, что файл полностью скачан (размер около 65 МБ)

## Разработка
### Структура проекта
- `main.py` - программа entry point
- `gui.py` - графический интерфейс
- `build.py` - EXE build script
- `fonts/` - fonts folder
- `requirements.txt` - project dependencies

### Сборка для разработки
Для запуска программы в режиме разработки:
```bash
python main.py
```

## Благодарности
- Дизайн интерфейса основан на [cs16.css](https://github.com/ekmas/cs16.css) от [@ekmas](https://github.com/ekmas)
- Шрифт Fifaks 1.0 dev1 взят с [fonts-online.ru](https://fonts-online.ru/fonts/fifaks-10-dev1)

## Автор
Создано Hidetoshi Karita

---

# Mailing Helper

## Description
Mailing Helper is a program for automating mailing-related actions. It allows recording user actions and playing them back to automate routine tasks.

## Features
- Record user actions (mouse clicks, keyboard presses)
- Play back recorded actions
- Excel file support
- Bilingual interface (Russian/English)
- Unique Fifaks font for better readability
- Hotkey support

## System Requirements
- Windows 10/11
- Python 3.8 or higher
- Microsoft Visual C++ Redistributable (download: https://aka.ms/vs/17/release/vc_redist.x64.exe)

## Installation and Building
### Building from Source
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mailing-helper.git
   cd mailing-helper
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # for Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Build the program:
   ```bash
   python build.py
   ```

5. The EXE file will be in the `dist` folder

### Ready Version
If you don't want to build the program yourself, you can download the ready EXE file from the Releases section.

## Usage
### Main Functions
1. **Record Actions (F6)**
   - Press F6 to start recording
   - Perform necessary actions
   - Press F6 again to stop recording

2. **Playback (F7)**
   - Press F7 to play back recorded actions
   - The program will repeat all recorded actions exactly

3. **Excel Support**
   - The program supports working with Excel files
   - Can automate actions with table data

4. **Language Switch**
   - Language switcher available in the interface
   - Supports Russian and English languages

### Hotkeys
- F6 - Start/Stop recording
- F7 - Play back recorded actions

## Troubleshooting
If the program doesn't start:
1. Make sure Microsoft Visual C++ Redistributable is installed
2. Check if antivirus is blocking it
3. Try running as administrator
4. Verify the file is fully downloaded (size about 65 MB)

## Development
### Project Structure
- `main.py` - program entry point
- `gui.py` - graphical interface
- `build.py` - EXE build script
- `fonts/` - fonts folder
- `requirements.txt` - project dependencies

### Development Build
To run the program in development mode:
```bash
python main.py
```

## Acknowledgments
- Interface design is based on [cs16.css](https://github.com/ekmas/cs16.css) by [@ekmas](https://github.com/ekmas)
- Fifaks 1.0 dev1 font is taken from [fonts-online.ru](https://fonts-online.ru/fonts/fifaks-10-dev1)

## Author
Created by Hidetoshi Karita 