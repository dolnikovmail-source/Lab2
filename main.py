
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, 
    QVBoxLayout, QWidget, QLabel
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    """Главное окно приложения 'Медиатек'."""
    
    def __init__(self):
        super().__init__()
        # Установка заголовка и стартовых размеров окна
        self.setWindowTitle("Медиатек")
        self.resize(360, 260)
        
        self.init_ui()

    def init_ui(self):
        """Инициализация виджетов и компоновки (layout)."""
        # Центральный виджет окна
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Вертикальный макет размещения
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Информационная метка
        self.title_label = QLabel("Панель управления мультимедиа")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_label)

        # Создание трех кнопок по Варианту 1
        self.btn_open = QPushButton("Открыть файл")
        self.btn_save = QPushButton("Сохранить")
        self.btn_exit = QPushButton("Выход")

        # Подключение сигналов нажатия к соответствующим слотам
        self.btn_open.clicked.connect(self.on_open_clicked)
        self.btn_save.clicked.connect(self.on_save_clicked)
        self.btn_exit.clicked.connect(self.on_exit_clicked)

        # Добавление кнопок в макет
        layout.addWidget(self.btn_open)
        layout.addWidget(self.btn_save)
        layout.addWidget(self.btn_exit)

        # Установка макета для центрального виджета
        central_widget.setLayout(layout)

    # Слоты (обработчики событий нажатия)
    def on_open_clicked(self):
        """Обработка кнопки 'Открыть файл'."""
        print("[Событие] Нажата кнопка: 'Открыть файл'")

    def on_save_clicked(self):
        """Обработка кнопки 'Сохранить'."""
        print("[Событие] Нажата кнопка: 'Сохранить'")

    def on_exit_clicked(self):
        """Обработка кнопки 'Выход'."""
        print("[Событие] Нажата кнопка: 'Выход'. Закрытие приложения...")
        self.close()


def main():
    """Точка входа в программу."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()