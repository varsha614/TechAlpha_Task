import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QAction, QPainter
from PySide6.QtWidgets import (QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout,
                               QWidget)
from PySide6.QtCharts import QChartView, QPieSeries, QChart


class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.items = 0
        self._data = {}
        

        # Left Widget
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Description", "Price"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Chart
        self.chart_view = QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        # Right Widget
        self.description = QLineEdit()
        self.description.setStyleSheet("border: 1px solid black;")
        self.price = QLineEdit()
        self.price.setStyleSheet("border: 1px solid black;")
        self.add = QPushButton("Add")
        self.add.setStyleSheet("border: 1px solid black;")
        self.clear = QPushButton("Clear")
        self.clear.setStyleSheet("border: 1px solid black;")
        self.quit = QPushButton("Quit")
        self.quit.setStyleSheet("border: 1px solid black;")
        self.plot = QPushButton("Plot")
        self.plot.setStyleSheet("border: 1px solid black;")

        self.add.setEnabled(False)

        self.right = QVBoxLayout()
        self.right.addWidget(QLabel("Description"))
        self.right.addWidget(self.description)
        self.right.addWidget(QLabel("Price"))
        self.right.addWidget(self.price)
        self.right.addWidget(self.add)
        self.right.addWidget(self.plot)
        self.right.addWidget(self.chart_view)
        self.right.addWidget(self.clear)
        self.right.addWidget(self.quit)

        # Total Expenses Label
        self.total_label = QLabel("Total Expenses: $0.00")
        self.total_label.setStyleSheet("border: 1px solid black; padding: 5px;  background-color: lightblue; font-weight: bold;")
        self.right.addWidget(self.total_label)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addLayout(self.right)
        self.setLayout(self.layout)

        self.add.clicked.connect(self.add_element)
        self.quit.clicked.connect(self.quit_application)
        self.plot.clicked.connect(self.plot_data)
        self.clear.clicked.connect(self.clear_table)
        self.description.textChanged[str].connect(self.check_disable)
        self.price.textChanged[str].connect(self.check_disable)

        self.fill_table()

    @Slot()
    def add_element(self):
        des = self.description.text()
        price = self.price.text()

        try:
            price_item = QTableWidgetItem(f"{float(price):.2f}")
            price_item.setTextAlignment(Qt.AlignRight)

            self.table.insertRow(self.items)
            description_item = QTableWidgetItem(des)

            self.table.setItem(self.items, 0, description_item)
            self.table.setItem(self.items, 1, price_item)

            self.description.setText("")
            self.price.setText("")

            self.items += 1

            # Update total expenses
            self.update_total()
        except ValueError:
            print("That is not an invalid input:", price, "Make sure to enter a price!")

    @Slot()
    def check_disable(self, x):
        if not self.description.text() or not self.price.text():
            self.add.setEnabled(False)
        else:
            self.add.setEnabled(True)

    @Slot()
    def plot_data(self):
        series = QPieSeries()
        for i in range(self.table.rowCount()):
            text = self.table.item(i, 0).text()
            number = float(self.table.item(i, 1).text())
            series.append(text, number)

        chart = QChart()
        chart.addSeries(series)
        chart.legend().setAlignment(Qt.AlignLeft)
        self.chart_view.setChart(chart)

    @Slot()
    def quit_application(self):
        QApplication.quit()

    def fill_table(self, data=None):
        data = self._data if not data else data
        for desc, price in data.items():
            description_item = QTableWidgetItem(desc)
            price_item = QTableWidgetItem(f"{price:.2f}")
            price_item.setTextAlignment(Qt.AlignRight)
            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, description_item)
            self.table.setItem(self.items, 1, price_item)
            self.items += 1

        # Update total expenses
        self.update_total()

    @Slot()
    def clear_table(self):
        self.table.setRowCount(0)
        self.items = 0

        # Update total expenses
        self.update_total()

    def update_total(self):
        total = sum(float(self.table.item(i, 1).text()) for i in range(self.table.rowCount()))
        self.total_label.setText(f"Total Expenses: ${total:.2f}")


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Expense tracker")

        
       
        # Menu
        self.menu = self.menuBar()
        self.menu.setStyleSheet("background-color: lightblue;")
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(exit_action)
        self.setCentralWidget(widget)
       
        
    @Slot()
    def exit_app(self, checked):
        QApplication.quit()


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)
    # QWidget
    widget = Widget()
    # QMainWindow using QWidget as central widget
    window = MainWindow(widget)
    window.resize(800, 600)
    window.show()

    # Execute application
    sys.exit(app.exec())

