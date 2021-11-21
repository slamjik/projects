import csv
import sqlite3
from tkinter import *

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('C:/Users/Olega/OneDrive/Рабочий стол/united.ui', self)
        self.loadTable('C:/Users/Olega/OneDrive/Рабочий стол/Книга1.csv.csv')
        self.con = sqlite3.connect(r"C:\Users\Olega\OneDrive\Рабочий стол\SQLiteStudio\asdfg")
        self.cur = self.con.cursor()
        self.pushButton_2.clicked.connect(self.update_result)
        self.pushButton_3.clicked.connect(self.delete_elem)
        self.fill_the_table()

    def delete_elem(self):
        # Получаем список элементов без повторов и их id
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        # Спрашиваем у пользователя подтверждение на удаление элементов
        valid = QMessageBox.question(
            self, '', "Действительно удалить элементы с id " + ",".join(ids),
            QMessageBox.Yes, QMessageBox.No)
        # Если пользователь ответил утвердительно, удаляем элементы.
        # Не забываем зафиксировать изменения
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute('''DELETE FROM price WHERE Price IN (" + ", ".join(
                '?' * len(ids)) + ")''', ids)
            self.con.commit()

    def update_result(self):
        pass

    def fill_the_table(self):
        result = self.cur.execute(f'''SELECT * FROM price WHERE Price''').fetchall()
        self.title = [elem[0] for elem in self.cur.description]
        self.tableWidget.setRowCount(len(result))

        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(self.title)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


    def loadTable(self, table_name):
        with open(table_name, encoding="latin-1") as csvfile:
            reader = csv.reader(csvfile,
                                delimiter=';', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
    #не получилось сделать в приложение иза ограничение места в гит хабе

