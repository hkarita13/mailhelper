import os
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase, QFont
from gui import MailingHelperApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Регистрируем шрифт
    font_path = os.path.join(os.path.dirname(__file__), "fonts", "Fifaks10Dev1.ttf")
    font_id = QFontDatabase.addApplicationFont(font_path)
    if font_id == -1:
        print(f"Ошибка загрузки шрифта: {font_path}")
    else:
        print(f"Шрифт успешно загружен: {font_path}")
        print(f"ID шрифта: {font_id}")
        print(f"Доступные семейства шрифтов: {QFontDatabase.applicationFontFamilies(font_id)}")
        # Устанавливаем шрифт глобально
        app.setFont(QFont("Fifaks 1.0 dev1", 14))
    
    window = MailingHelperApp()
    window.show()
    sys.exit(app.exec_())
