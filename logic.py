import json
import time
import pyautogui
import pandas as pd
import keyboard
from PyQt5.QtWidgets import QFileDialog, QMessageBox

def type_text(text, typing_speed=50):
    """Вводит текст с поддержкой русского языка и переносов строк"""
    # Заменяем \n на реальный перенос строки
    text = text.replace("\\n", "\n")
    
    # Вводим текст посимвольно
    for char in text:
        if keyboard.is_pressed("esc"):
            return False  # Сигнал об остановке
        if char == "\n":
            keyboard.press_and_release("enter")
            time.sleep(typing_speed / 1000)  # Задержка после переноса строки
        else:
            keyboard.write(char)
            time.sleep(typing_speed / 1000)  # Задержка между символами
    return True

def parse_step(step_text):
    """Парсит текст шага и возвращает тип действия и параметры"""
    step_text = step_text.strip()
    
    # Поддержка обоих форматов (старого русского и нового английского)
    if "Click:" in step_text or "Клик:" in step_text:
        coords = step_text.split("(")[1].split(")")[0]
        x, y = map(int, coords.split(","))
        return "click", (x, y)
    elif "Wait:" in step_text or "Ожидание:" in step_text:
        time_str = step_text.split(":")[1].strip()
        time_ms = int(time_str.replace("ms", "").replace("мс", "").strip())
        return "wait", time_ms
    elif "Input:" in step_text or "Ввод:" in step_text:
        text = step_text.split(":", 1)[1].strip()
        return "input", text
    elif "Input CSV:" in step_text or "Ввод (CSV):" in step_text:
        # Парсим параметры CSV
        parts = step_text.split("|")
        file_path = parts[0].split(":", 1)[1].strip()
        template = parts[1].split(":", 1)[1].strip()
        columns = parts[2].split(":", 1)[1].strip().split(",")
        return "csv", (file_path, template, columns)
    else:
        return None, None

def run_scenario(steps_list, mode="once", iterations=1, typing_speed=50):
    """Запускает сценарий с указанным режимом выполнения"""
    def execute_steps(csv_row_index=None):
        csv_files = {}  # Словарь для хранения загруженных CSV файлов
        
        for i in range(steps_list.count()):
            if keyboard.is_pressed("esc"):
                QMessageBox.information(None, "Остановка", "Сценарий остановлен пользователем")
                return False
                
            step = steps_list.item(i).text()
            action_type, params = parse_step(step)
            
            if action_type == "click":
                x, y = params
                pyautogui.click(x, y)
            elif action_type == "wait":
                time.sleep(params / 1000)  # Конвертируем мс в секунды
            elif action_type == "input":
                if not type_text(params, typing_speed):
                    return False
            elif action_type == "csv":
                try:
                    file_path, template, columns = params
                    
                    # Загружаем CSV файл только один раз
                    if file_path not in csv_files:
                        csv_files[file_path] = pd.read_csv(file_path)
                    
                    df = csv_files[file_path]
                    
                    # Проверяем, есть ли строка с таким индексом
                    if csv_row_index is not None and csv_row_index < len(df):
                        row = df.iloc[csv_row_index]
                        
                        # Заменяем шаблоны на значения
                        text = template
                        for column in columns:
                            if column in row:
                                text = text.replace(f"{{{{{column}}}}}", str(row[column]))
                                
                        if not type_text(text, typing_speed):
                            return False
                            
                        keyboard.press_and_release("enter")
                    else:
                        QMessageBox.warning(None, "Ошибка", f"В CSV файле нет строки с индексом {csv_row_index}")
                        return False
                        
                except Exception as e:
                    QMessageBox.warning(None, "Ошибка", f"Ошибка при чтении CSV: {str(e)}")
                    return False
        return True

    try:
        if mode == "Один раз" or mode == "Once":
            execute_steps(csv_row_index=0)
        elif mode == "Итерации" or mode == "Iterations":
            for i in range(iterations):
                if not execute_steps(csv_row_index=i):
                    break
        elif mode == "Цикл" or mode == "Loop":
            i = 0
            while True:
                if not execute_steps(csv_row_index=i):
                    break
                i += 1
    except Exception as e:
        QMessageBox.warning(None, "Ошибка", f"Произошла ошибка: {str(e)}")

def save_scenario(steps_list):
    """Сохраняет текущий сценарий в JSON"""
    file_path, _ = QFileDialog.getSaveFileName(None, "Сохранить сценарий", "", "JSON Files (*.json)")
    if file_path:
        steps = [steps_list.item(i).text() for i in range(steps_list.count())]
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(steps, f, ensure_ascii=False, indent=4)

def load_scenario(steps_list):
    """Загружает сценарий из JSON"""
    file_path, _ = QFileDialog.getOpenFileName(None, "Загрузить сценарий", "", "JSON Files (*.json)")
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            steps = json.load(f)
            steps_list.clear()
            steps_list.addItems(steps)
