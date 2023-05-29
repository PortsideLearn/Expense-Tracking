import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

# Создаем соединение с базой данных
conn = sqlite3.connect('expenses.db')

# Создаем таблицу, если она не существует
conn.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    category TEXT NOT NULL,
                    amount REAL NOT NULL)''')

# Закрываем соединение
conn.close()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управление расходами")

        # Создаем виджеты для ввода данных
        self.date_input = QLineEdit()
        self.category_input = QLineEdit()
        self.amount_input = QLineEdit()

        # Создаем метки для ввода данных
        self.date_label = QLabel("Дата (гггг-мм-дд):")
        self.category_label = QLabel("Категория:")
        self.amount_label = QLabel("Сумма (руб.):")

        # Создаем кнопку добавления расходов
        self.add_button = QPushButton("Добавить расход")
        self.add_button.clicked.connect(self.add_expense)

        # Создаем горизонтальные блоки для меток и виджетов ввода данных
        date_layout = QHBoxLayout()
        date_layout.addWidget(self.date_label)
        date_layout.addWidget(self.date_input)

        category_layout = QHBoxLayout()
        category_layout.addWidget(self.category_label)
        category_layout.addWidget(self.category_input)

        amount_layout = QHBoxLayout()
        amount_layout.addWidget(self.amount_label)
        amount_layout.addWidget(self.amount_input)

        # Создаем вертикальный блок для всех виджетов
        main_layout = QVBoxLayout()
        main_layout.addLayout(date_layout)
        main_layout.addLayout(category_layout)
        main_layout.addLayout(amount_layout)
        main_layout.addWidget(self.add_button)

        # Устанавливаем основной макет
        self.setLayout(main_layout)

    def add_expense(self):
        # Получаем данные из полей ввода
        date = self.date_input.text()
        category = self.category_input.text()
        amount = float(self.amount_input.text())

        # Создаем соединение с базой данных
        conn = sqlite3.connect('expenses.db')

        # Добавляем запись в таблицу расходов
        conn.execute("INSERT INTO expenses (date, category, amount) VALUES (?, ?, ?)", (date, category, amount))

        # Закрываем соединение и коммитим изменения
        conn.commit()
        conn.close()

        # Очищаем поля ввода
        self.date_input.clear()
        self.category_input.clear()
        self.amount_input.clear()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
