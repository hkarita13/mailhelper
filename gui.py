import json
import time
import pyautogui
import pandas as pd
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLabel, QComboBox, QFileDialog, QInputDialog, QLineEdit, QMessageBox, QSpinBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QFontDatabase
from screeninfo import get_monitors
from logic import run_scenario, save_scenario, load_scenario
import keyboard
import mouse
import os

# Словари с переводами
TRANSLATIONS = {
    "RU": {
        "window_title": "Помощник рассылки",
        "select_action": "Выберите действие:",
        "click_coords": "Click (coordinates) (Клик по координатам)",
        "click_record": "Click (record) (Запись клика)",
        "wait": "Wait (Ожидание)",
        "input": "Input (Ввод текста)",
        "input_csv": "Input CSV (Ввод из CSV)",
        "add_action": "Добавить действие",
        "delete_step": "Удалить выбранный шаг",
        "typing_speed": "Скорость ввода (мс):",
        "execution_mode": "Режим выполнения:",
        "once": "Один раз",
        "iterations": "Итерации",
        "loop": "Цикл",
        "iterations_count": "Кол-во итераций",
        "start": "Старт",
        "save_scenario": "Сохранить сценарий",
        "load_scenario": "Загрузить сценарий",
        "screen_select": "Выбор экрана:",
        "help": "Помощь",
        "enter_x": "Введите X",
        "enter_y": "Введите Y",
        "coord_x": "Координата X:",
        "coord_y": "Координата Y:",
        "wait_time": "Время ожидания",
        "enter_ms": "Введите время в миллисекундах:",
        "enter_text": "Введите текст",
        "text_input": "Текст для ввода (используйте \\n для новой строки):",
        "select_csv": "Выберите CSV файл",
        "recording": "Запись клика... (кликните в нужном месте)",
        "edit_step": "Редактирование шага",
        "modify_step": "Измените шаг:",
        "error": "Ошибка",
        "csv_error": "Не удалось прочитать CSV файл: ",
        "error_occurred": "Произошла ошибка: ",
        "language": "Язык:",
        "help_text": """
Помощник рассылки - программа для автоматизации действий с мышью и клавиатурой.

Основные функции:
• Запись и выполнение кликов мышью
• Ввод текста с настраиваемой скоростью
• Работа с CSV-файлами
• Сохранение и загрузка сценариев

Режимы выполнения:
• Один раз - выполнение сценария один раз
• Итерации - выполнение сценария указанное количество раз
• Цикл - бесконечное повторение сценария

Горячие клавиши:
• F6 - запись клика мышью
• Esc - экстренная остановка сценария

Управление сценарием:
• Добавление действий через выпадающий список
• Перетаскивание действий для изменения порядка
• Двойной клик для редактирования
• Кнопка удаления для удаления выбранного действия

Специальные возможности:
• Задержки между действиями
• Настраиваемая скорость ввода текста
• Поддержка переноса строки (\\n)
• Работа с CSV-файлами для массового ввода

Формат CSV-файла:
• Каждая строка - отдельная итерация
• Значения разделяются запятыми
• Автоматический переход между полями (Tab)
• Автоматический переход на новую строку (Enter)

Безопасность:
• Возможность экстренной остановки (Esc)
• Проверка корректности CSV-файлов
• Обработка ошибок при выполнении

Создано Hidetoshi Karita
"""
    },
    "EN": {
        "window_title": "Mailing Assistant",
        "select_action": "Select action:",
        "click_coords": "Click (coordinates)",
        "click_record": "Click (record)",
        "wait": "Wait",
        "input": "Input",
        "input_csv": "Input (CSV)",
        "add_action": "Add action",
        "delete_step": "Delete selected step",
        "typing_speed": "Typing speed (ms):",
        "execution_mode": "Execution mode:",
        "once": "Once",
        "iterations": "Iterations",
        "loop": "Loop",
        "iterations_count": "Iterations count",
        "start": "Start",
        "save_scenario": "Save scenario",
        "load_scenario": "Load scenario",
        "screen_select": "Select screen:",
        "help": "Help",
        "enter_x": "Enter X",
        "enter_y": "Enter Y",
        "coord_x": "X coordinate:",
        "coord_y": "Y coordinate:",
        "wait_time": "Wait time",
        "enter_ms": "Enter time in milliseconds:",
        "enter_text": "Enter text",
        "text_input": "Text to input (use \\n for new line):",
        "select_csv": "Select CSV file",
        "recording": "Recording click... (click anywhere)",
        "edit_step": "Edit step",
        "modify_step": "Modify step:",
        "error": "Error",
        "csv_error": "Could not read CSV file: ",
        "error_occurred": "An error occurred: ",
        "language": "Language:",
        "help_text": """
Mailing Helper - a program for automating mouse and keyboard actions.

Main functions:
• Recording and executing mouse clicks
• Text input with adjustable speed
• Working with CSV files
• Saving and loading scenarios

Execution modes:
• Once - single execution of the scenario
• Iterations - executing the scenario a specified number of times
• Loop - infinite repetition of the scenario

Hotkeys:
• F6 - record mouse click
• Esc - emergency stop of the scenario

Scenario management:
• Adding actions through the dropdown list
• Drag and drop actions to change order
• Double-click to edit
• Delete button to remove selected action

Special features:
• Delays between actions
• Adjustable text input speed
• Line break support (\\n)
• CSV file support for mass input

CSV file format:
• Each row - separate iteration
• Values separated by commas
• Automatic field navigation (Tab)
• Automatic new line (Enter)

Safety:
• Emergency stop capability (Esc)
• CSV file validation
• Error handling during execution

Created by Hidetoshi Karita
"""
    }
}

class DragDropListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragEnabled(True)
        self.setDragDropMode(QListWidget.InternalMove)
        self.setSelectionMode(QListWidget.SingleSelection)
        self.setDefaultDropAction(Qt.MoveAction)

class MailingHelperApp(QWidget):
    def __init__(self):
        super().__init__()
        self.recording = False
        self.typing_speed = 50  # Скорость ввода по умолчанию (мс)
        self.current_lang = "RU"  # Язык по умолчанию
        self.translations = TRANSLATIONS[self.current_lang]
        self.load_styles()
        self.initUI()
        self.setup_shortcuts()
        self.setup_recording()

    def load_styles(self):
        """Загружает стили в стиле CS 1.6"""
        style = """
            * {
                font-family: "Fifaks 1.0 dev1";
            }
            
            QWidget {
                background-color: #4a5942;
                color: #dedfd6;
                border: none;
                font-size: 14px;
            }
            
            QPushButton {
                background-color: #4a5942;
                color: #dedfd6;
                padding: 4px 5px 3px;
                font-size: 16px;
                line-height: 15px;
                border: 1px solid;
                border-top-color: #8c9284;
                border-left-color: #8c9284;
                border-right-color: #292c21;
                border-bottom-color: #292c21;
            }
            
            QPushButton:hover {
                color: #ffffff;
            }
            
            QPushButton:pressed {
                border-top-color: #292c21;
                border-left-color: #292c21;
                border-right-color: #8c9284;
                border-bottom-color: #8c9284;
                padding: 5px 4px 2px 6px;
            }
            
            QPushButton:disabled {
                color: #292c21;
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #75806f, stop:1 transparent);
            }
            
            QListWidget {
                background-color: #3e4637;
                border: 1px solid;
                border-top-color: #292c21;
                border-left-color: #292c21;
                border-right-color: #8c9284;
                border-bottom-color: #8c9284;
                padding: 5px;
            }
            
            QListWidget::item {
                background-color: #4a5942;
                color: #dedfd6;
                padding: 4px 5px;
                margin: 2px;
                border: 1px solid;
                border-top-color: #8c9284;
                border-left-color: #8c9284;
                border-right-color: #292c21;
                border-bottom-color: #292c21;
            }
            
            QListWidget::item:selected {
                background-color: #3e4637;
                color: #c4b550;
                border-top-color: #292c21;
                border-left-color: #292c21;
                border-right-color: #8c9284;
                border-bottom-color: #8c9284;
            }
            
            QComboBox {
                background-color: #3e4637;
                color: #dedfd6;
                padding: 4px 5px;
                border: 1px solid;
                border-top-color: #292c21;
                border-left-color: #292c21;
                border-right-color: #8c9284;
                border-bottom-color: #8c9284;
                font-family: "Fifaks 1.0 dev1";
            }
            
            QComboBox QAbstractItemView {
                background-color: #3e4637;
                color: #dedfd6;
                selection-background-color: #4a5942;
                selection-color: #c4b550;
                border: 1px solid #292c21;
                font-family: "Fifaks 1.0 dev1";
            }
            
            QComboBox:hover {
                color: #ffffff;
            }
            
            QComboBox::drop-down {
                border: none;
                width: 20px;
            }
            
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #dedfd6;
                width: 0;
                height: 0;
            }
            
            QLabel {
                color: #dedfd6;
                background: none;
                border: none;
            }
            
            QLineEdit, QSpinBox {
                background-color: #3e4637;
                color: #dedfd6;
                padding: 4px 5px;
                border: 1px solid;
                border-top-color: #292c21;
                border-left-color: #292c21;
                border-right-color: #8c9284;
                border-bottom-color: #8c9284;
            }
            
            QLineEdit:focus, QSpinBox:focus {
                border: 1px solid #c4b550;
            }
            
            QSpinBox::up-button, QSpinBox::down-button {
                background-color: #4a5942;
                border: 1px solid;
                border-top-color: #8c9284;
                border-left-color: #8c9284;
                border-right-color: #292c21;
                border-bottom-color: #292c21;
                width: 15px;
            }
            
            QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {
                border-top-color: #292c21;
                border-left-color: #292c21;
                border-right-color: #8c9284;
                border-bottom-color: #8c9284;
            }
            
            QMessageBox {
                background-color: #4a5942;
            }
            
            QMessageBox QLabel {
                color: #dedfd6;
                font-size: 14px;
            }
            
            QMessageBox QPushButton {
                min-width: 80px;
            }
            
            /* Стиль для кнопки записи в активном состоянии */
            QPushButton[recording="true"] {
                background-color: #8b0000;
                color: #ffffff;
                border-top-color: #ff0000;
                border-left-color: #ff0000;
                border-right-color: #4a0000;
                border-bottom-color: #4a0000;
            }
        """
        self.setStyleSheet(style)

    def setup_shortcuts(self):
        """Настройка горячих клавиш"""
        self.save_btn.setShortcut("Ctrl+S")
        self.load_btn.setShortcut("Ctrl+O")
        self.steps_list.setFocusPolicy(Qt.StrongFocus)
        self.steps_list.keyPressEvent = self.handle_key_press

    def handle_key_press(self, event):
        """Обработка нажатия клавиш в списке шагов"""
        if event.key() == Qt.Key_Delete:
            self.delete_action()
        else:
            QListWidget.keyPressEvent(self.steps_list, event)

    def setup_recording(self):
        """Настройка записи кликов"""
        self.record_timer = QTimer()
        self.record_timer.timeout.connect(self.check_mouse_click)
        keyboard.on_press_key("f6", lambda _: self.toggle_recording())

    def toggle_recording(self):
        """Включает/выключает режим записи кликов"""
        if not self.recording:
            self.recording = True
            self.record_btn.setText("Остановить запись (F6)")
            self.record_btn.setStyleSheet("background-color: red;")
            self.record_timer.start(100)  # Проверка каждые 100мс
            QMessageBox.information(self, "Запись кликов", 
                "Режим записи кликов включен.\nНажимайте F6 для остановки.")
        else:
            self.recording = False
            self.record_btn.setText("Запись действий (F6)")
            self.record_btn.setStyleSheet("")
            self.record_timer.stop()
            QMessageBox.information(self, "Запись кликов", 
                "Режим записи кликов выключен.")

    def check_mouse_click(self):
        """Проверяет нажатие кнопки мыши"""
        if mouse.is_pressed(button='left'):
            x, y = pyautogui.position()
            # Удаляем временную метку записи
            self.steps_list.takeItem(self.steps_list.count() - 1)
            # Добавляем записанный клик
            self.steps_list.addItem(f"Click: ({x}, {y})")
            time.sleep(0.1)  # Небольшая задержка для предотвращения множественных кликов
            # Автоматически останавливаем запись после клика
            self.recording = False
            self.record_timer.stop()

    def show_help(self):
        """Показывает окно с описанием работы программы"""
        QMessageBox.information(self, "Помощь", self.translations["help_text"])

    def toggle_iterations_input(self):
        """Включает поле ввода итераций, если выбран режим 'Итерации'"""
        if self.mode_combo.currentText() == "Итерации":
            self.iterations_input.setEnabled(True)
        else:
            self.iterations_input.setDisabled(True)

    def start_scenario(self):
        """Запускает выполнение сценария с выбранным режимом"""
        mode = self.mode_combo.currentText()
        iterations = 1  # По умолчанию 1 раз

        if mode == "Итерации":
            try:
                iterations = int(self.iterations_input.text())
                if iterations <= 0:
                    raise ValueError
            except ValueError:
                return  # Игнорируем запуск, если введено некорректное число

        run_scenario(self.steps_list, mode, iterations, self.typing_speed)

    def change_language(self, index):
        """Меняет язык интерфейса"""
        self.current_lang = "EN" if index == 1 else "RU"
        self.translations = TRANSLATIONS[self.current_lang]
        self.update_ui_texts()
        self.translate_list_items()

    def translate_list_items(self):
        """Переводит существующие действия в списке при смене языка"""
        # Действия всегда остаются на английском
        pass

    def update_ui_texts(self):
        """Обновляет тексты в интерфейсе при смене языка"""
        self.setWindowTitle(self.translations["window_title"])
        self.action_label.setText(self.translations["select_action"])
        self.action_combo.clear()
        self.action_combo.addItems([
            self.translations["click_coords"],
            self.translations["click_record"],
            self.translations["wait"],
            self.translations["input"],
            self.translations["input_csv"]
        ])
        self.add_action_btn.setText(self.translations["add_action"])
        self.delete_action_btn.setText(self.translations["delete_step"])
        self.mode_label.setText(self.translations["execution_mode"])
        self.mode_combo.clear()
        self.mode_combo.addItems([
            self.translations["once"],
            self.translations["iterations"],
            self.translations["loop"]
        ])
        self.iterations_input.setPlaceholderText(self.translations["iterations_count"])
        self.start_btn.setText(self.translations["start"])
        self.save_btn.setText(self.translations["save_scenario"])
        self.load_btn.setText(self.translations["load_scenario"])
        self.help_btn.setText(self.translations["help"])
        self.screen_label.setText(self.translations["screen_select"])
        self.lang_label.setText(self.translations["language"])

    def initUI(self):
        self.setWindowTitle(self.translations["window_title"])
        self.setGeometry(100, 100, 800, 600)
        
        # Главный макет
        main_layout = QHBoxLayout()
        
        # Левая панель (список шагов)
        self.steps_list = DragDropListWidget()
        self.steps_list.itemDoubleClicked.connect(self.edit_action)
        main_layout.addWidget(self.steps_list, 2)
        
        # Правая панель (панели действий и управления)
        right_layout = QVBoxLayout()
        
        # Выбор языка
        lang_layout = QHBoxLayout()
        self.lang_label = QLabel(self.translations["language"])
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["Русский", "English"])
        self.lang_combo.currentIndexChanged.connect(self.change_language)
        lang_layout.addWidget(self.lang_label)
        lang_layout.addWidget(self.lang_combo)
        
        # Панель выбора действий
        actions_layout = QVBoxLayout()
        self.action_label = QLabel(self.translations["select_action"])
        self.action_combo = QComboBox()
        self.action_combo.addItems([
            self.translations["click_coords"],
            self.translations["click_record"],
            self.translations["wait"],
            self.translations["input"],
            self.translations["input_csv"]
        ])
        self.add_action_btn = QPushButton(self.translations["add_action"])
        self.add_action_btn.clicked.connect(self.add_action)
        self.delete_action_btn = QPushButton(self.translations["delete_step"])
        self.delete_action_btn.clicked.connect(self.delete_action)
        
        # Настройка скорости ввода
        speed_layout = QHBoxLayout()
        speed_label = QLabel(self.translations["typing_speed"])
        self.speed_spinbox = QSpinBox()
        self.speed_spinbox.setRange(1, 500)  # Минимальное значение 1 мс
        self.speed_spinbox.setValue(50)
        self.speed_spinbox.valueChanged.connect(self.update_typing_speed)
        speed_layout.addWidget(speed_label)
        speed_layout.addWidget(self.speed_spinbox)
        
        actions_layout.addLayout(lang_layout)
        actions_layout.addWidget(self.action_label)
        actions_layout.addWidget(self.action_combo)
        actions_layout.addWidget(self.add_action_btn)
        actions_layout.addWidget(self.delete_action_btn)
        actions_layout.addLayout(speed_layout)
        
        # Панель управления
        controls_layout = QVBoxLayout()
        # Выбор режима выполнения
        self.mode_label = QLabel(self.translations["execution_mode"])
        self.mode_combo = QComboBox()
        self.mode_combo.addItems([
            self.translations["once"],
            self.translations["iterations"],
            self.translations["loop"]
        ])
        self.iterations_input = QLineEdit()
        self.iterations_input.setPlaceholderText(self.translations["iterations_count"])
        self.iterations_input.setDisabled(True)
        
        # Создаем кнопки
        self.start_btn = QPushButton(self.translations["start"])
        self.save_btn = QPushButton(self.translations["save_scenario"])
        self.load_btn = QPushButton(self.translations["load_scenario"])
        
        # Подключаем сигналы
        self.start_btn.clicked.connect(self.start_scenario)
        self.save_btn.clicked.connect(lambda: save_scenario(self.steps_list))
        self.load_btn.clicked.connect(lambda: load_scenario(self.steps_list))

        # Активируем поле ввода, если выбраны "Итерации"
        self.mode_combo.currentIndexChanged.connect(self.toggle_iterations_input)
        
        # Заполняем список экранов
        self.screen_label = QLabel(self.translations["screen_select"])
        self.screen_combo = QComboBox()
        self.load_screens()
        
        self.help_btn = QPushButton(self.translations["help"])
        self.help_btn.clicked.connect(self.show_help)
        
        # Добавляем элементы в макет
        controls_layout.addWidget(self.mode_label)
        controls_layout.addWidget(self.mode_combo)
        controls_layout.addWidget(self.iterations_input)
        controls_layout.addWidget(self.start_btn)
        controls_layout.addWidget(self.save_btn)
        controls_layout.addWidget(self.load_btn)
        controls_layout.addWidget(self.screen_label)
        controls_layout.addWidget(self.screen_combo)
        controls_layout.addWidget(self.help_btn)
        
        right_layout.addLayout(actions_layout)
        right_layout.addLayout(controls_layout)
        
        main_layout.addLayout(right_layout, 1)
        
        self.setLayout(main_layout)
    
    def load_screens(self):
        """ Загружает список доступных экранов в выпадающий список """
        self.screen_combo.clear()
        screens = [f"{i + 1}: {monitor.width}x{monitor.height}" for i, monitor in enumerate(get_monitors())]
        self.screen_combo.addItems(screens)
    
    def add_action(self):
        """Добавляет новое действие в список шагов"""
        action_type = self.action_combo.currentText()
        try:
            if "Click (coordinates)" in action_type:
                x, ok_x = QInputDialog.getInt(self, self.translations["enter_x"], 
                    self.translations["coord_x"])
                y, ok_y = QInputDialog.getInt(self, self.translations["enter_y"], 
                    self.translations["coord_y"])
                if ok_x and ok_y:
                    self.steps_list.addItem(f"Click: ({x}, {y})")
            elif "Click (record)" in action_type:
                self.recording = True
                self.record_timer.start(100)
                self.steps_list.addItem("Recording click... (click anywhere)")
            elif "Wait" in action_type:
                time, ok = QInputDialog.getInt(self, self.translations["wait_time"], 
                    self.translations["enter_ms"])
                if ok:
                    self.steps_list.addItem(f"Wait: {time} ms")
            elif "Input" in action_type and "CSV" not in action_type:
                text, ok = QInputDialog.getMultiLineText(self, self.translations["enter_text"], 
                    self.translations["text_input"])
                if ok and text:
                    self.steps_list.addItem(f"Input: {text}")
            elif "Input CSV" in action_type:
                file_path, _ = QFileDialog.getOpenFileName(self, self.translations["select_csv"], 
                    "", "CSV Files (*.csv)")
                if file_path:
                    try:
                        df = pd.read_csv(file_path)
                        self.steps_list.addItem(f"Input CSV: {file_path}")
                    except Exception as e:
                        QMessageBox.warning(self, self.translations["error"], 
                            f"{self.translations['csv_error']}{str(e)}")
        except Exception as e:
            QMessageBox.warning(self, self.translations["error"], 
                f"{self.translations['error_occurred']}{str(e)}")
    
    def edit_action(self, item):
        """Позволяет редактировать существующий шаг по двойному клику"""
        text, ok = QInputDialog.getText(self, "Редактирование шага", "Измените шаг:", text=item.text())
        if ok and text:
            item.setText(text)
    
    def delete_action(self):
        """Удаляет выбранный шаг"""
        selected_item = self.steps_list.currentItem()
        if selected_item:
            self.steps_list.takeItem(self.steps_list.row(selected_item))

    def update_typing_speed(self, value):
        """Обновляет скорость ввода текста"""
        self.typing_speed = value