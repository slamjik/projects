# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 715)
        MainWindow.setStyleSheet("background: rgb(250, 250, 150);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget1 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget1.setGeometry(QtCore.QRect(0, 0, 931, 771))
        self.tabWidget1.setStyleSheet("")
        self.tabWidget1.setObjectName("tabWidget1")
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setStyleSheet("")
        self.mainTab.setObjectName("mainTab")
        self.norm_progress = QtWidgets.QProgressBar(self.mainTab)
        self.norm_progress.setGeometry(QtCore.QRect(130, 130, 591, 23))
        self.norm_progress.setStyleSheet("color:black;\n"
"background: rgb(100, 250, 100);")
        self.norm_progress.setMinimum(0)
        self.norm_progress.setProperty("value", 0)
        self.norm_progress.setObjectName("norm_progress")
        self.label_9 = QtWidgets.QLabel(self.mainTab)
        self.label_9.setGeometry(QtCore.QRect(330, 100, 211, 21))
        self.label_9.setStyleSheet("font-size: 15px;")
        self.label_9.setObjectName("label_9")
        self.label_2 = QtWidgets.QLabel(self.mainTab)
        self.label_2.setGeometry(QtCore.QRect(860, 0, 61, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.all_spending_table = QtWidgets.QTableWidget(self.mainTab)
        self.all_spending_table.setGeometry(QtCore.QRect(130, 180, 611, 391))
        self.all_spending_table.setMaximumSize(QtCore.QSize(621, 16777215))
        self.all_spending_table.setStyleSheet("")
        self.all_spending_table.setObjectName("all_spending_table")
        self.all_spending_table.setColumnCount(6)
        self.all_spending_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.all_spending_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_spending_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_spending_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_spending_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_spending_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_spending_table.setHorizontalHeaderItem(5, item)
        self.clearSpendingButton = QtWidgets.QPushButton(self.mainTab)
        self.clearSpendingButton.setGeometry(QtCore.QRect(140, 580, 131, 41))
        self.clearSpendingButton.setStyleSheet("color:black;\n"
"background: rgb(100, 250, 100);\n"
"border: 1px solid black;\n"
"border-radius: 15px;")
        self.clearSpendingButton.setObjectName("clearSpendingButton")
        self.deleteLastSpendingButton = QtWidgets.QPushButton(self.mainTab)
        self.deleteLastSpendingButton.setGeometry(QtCore.QRect(280, 580, 171, 41))
        self.deleteLastSpendingButton.setStyleSheet("color:black;\n"
"background: rgb(100, 250, 100);\n"
"border: 1px solid black;\n"
"border-radius: 15px;")
        self.deleteLastSpendingButton.setObjectName("deleteLastSpendingButton")
        self.saveUpdatesButton = QtWidgets.QPushButton(self.mainTab)
        self.saveUpdatesButton.setGeometry(QtCore.QRect(600, 580, 131, 41))
        self.saveUpdatesButton.setStyleSheet("color:black;\n"
"background: rgb(100, 250, 100);\n"
"border: 1px solid black;\n"
"border-radius: 15px;")
        self.saveUpdatesButton.setObjectName("saveUpdatesButton")
        self.updateTableButton = QtWidgets.QPushButton(self.mainTab)
        self.updateTableButton.setGeometry(QtCore.QRect(460, 580, 131, 41))
        self.updateTableButton.setStyleSheet("color:black;\n"
"background: rgb(100, 250, 100);\n"
"border: 1px solid black;\n"
"border-radius: 15px;")
        self.updateTableButton.setObjectName("updateTableButton")
        self.importFromCSVFileButton = QtWidgets.QPushButton(self.mainTab)
        self.importFromCSVFileButton.setGeometry(QtCore.QRect(140, 630, 311, 41))
        self.importFromCSVFileButton.setStyleSheet("color:black;\n"
"background: rgb(100, 250, 100);\n"
"border: 1px solid black;\n"
"border-radius: 15px;")
        self.importFromCSVFileButton.setObjectName("importFromCSVFileButton")
        self.cancelTableUpdateButton = QtWidgets.QPushButton(self.mainTab)
        self.cancelTableUpdateButton.setGeometry(QtCore.QRect(460, 630, 271, 41))
        self.cancelTableUpdateButton.setStyleSheet("color:black;\n"
"background: rgb(100, 250, 100);\n"
"border: 1px solid black;\n"
"border-radius: 15px;")
        self.cancelTableUpdateButton.setObjectName("cancelTableUpdateButton")
        self.all_spending_table.raise_()
        self.norm_progress.raise_()
        self.label_9.raise_()
        self.label_2.raise_()
        self.clearSpendingButton.raise_()
        self.deleteLastSpendingButton.raise_()
        self.saveUpdatesButton.raise_()
        self.updateTableButton.raise_()
        self.importFromCSVFileButton.raise_()
        self.cancelTableUpdateButton.raise_()
        self.tabWidget1.addTab(self.mainTab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.export_stats_button = QtWidgets.QPushButton(self.tab_2)
        self.export_stats_button.setGeometry(QtCore.QRect(150, 50, 221, 51))
        self.export_stats_button.setStyleSheet("border-radius: 15px;\n"
"border: 2px solid white;\n"
"color:black;\n"
"background: rgb(100, 250, 100);")
        self.export_stats_button.setObjectName("export_stats_button")
        self.export_stats_input = QtWidgets.QLineEdit(self.tab_2)
        self.export_stats_input.setGeometry(QtCore.QRect(10, 50, 131, 51))
        self.export_stats_input.setStyleSheet("border-radius: 15px;\n"
"border: 2px solid black;")
        self.export_stats_input.setObjectName("export_stats_input")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(10, 20, 321, 21))
        self.label_25.setStyleSheet("font-size: 15px;")
        self.label_25.setObjectName("label_25")
        self.calculate_statistics_button = QtWidgets.QPushButton(self.tab_2)
        self.calculate_statistics_button.setGeometry(QtCore.QRect(10, 110, 361, 51))
        self.calculate_statistics_button.setStyleSheet("border-radius: 15px;\n"
"border: 2px solid white;\n"
"color:black;\n"
"background: rgb(100, 250, 100);")
        self.calculate_statistics_button.setObjectName("calculate_statistics_button")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(10, 190, 231, 271))
        self.frame_2.setStyleSheet("border-radius: 15px;\n"
"border: 2px solid black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.spending_name_2 = QtWidgets.QLineEdit(self.frame_2)
        self.spending_name_2.setGeometry(QtCore.QRect(10, 30, 211, 41))
        self.spending_name_2.setStyleSheet("")
        self.spending_name_2.setObjectName("spending_name_2")
        self.spending_price_2 = QtWidgets.QLineEdit(self.frame_2)
        self.spending_price_2.setGeometry(QtCore.QRect(10, 100, 211, 41))
        self.spending_price_2.setStyleSheet("")
        self.spending_price_2.setObjectName("spending_price_2")
        self.add_spending_button_2 = QtWidgets.QPushButton(self.frame_2)
        self.add_spending_button_2.setGeometry(QtCore.QRect(10, 210, 211, 51))
        self.add_spending_button_2.setStyleSheet("color:black;\n"
"background: rgb(100, 250, 100);")
        self.add_spending_button_2.setObjectName("add_spending_button_2")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(10, 80, 211, 16))
        self.label_10.setStyleSheet("\n"
"border: none;")
        self.label_10.setObjectName("label_10")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 211, 20))
        self.label_3.setStyleSheet("\n"
"border: none;")
        self.label_3.setObjectName("label_3")
        self.label_23 = QtWidgets.QLabel(self.frame_2)
        self.label_23.setGeometry(QtCore.QRect(10, 140, 211, 16))
        self.label_23.setStyleSheet("\n"
"border: none;")
        self.label_23.setObjectName("label_23")
        self.spending_category_2 = QtWidgets.QComboBox(self.frame_2)
        self.spending_category_2.setGeometry(QtCore.QRect(10, 160, 211, 41))
        self.spending_category_2.setStyleSheet("color: black;\n"
"")
        self.spending_category_2.setObjectName("spending_category_2")
        self.spending_category_2.addItem("")
        self.spending_category_2.addItem("")
        self.spending_category_2.addItem("")
        self.spending_category_2.addItem("")
        self.spending_category_2.addItem("")
        self.spending_category_2.addItem("")
        self.spending_category_2.addItem("")
        self.spending_category_2.addItem("")
        self.spending_category_2.addItem("")
        self.spending_category_2.addItem("")
        self.spending_category_2.addItem("")
        self.frame_3 = QtWidgets.QFrame(self.tab_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 480, 231, 181))
        self.frame_3.setStyleSheet("border-radius: 15px;\n"
"border: 2px solid black;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.day_spending_2 = QtWidgets.QLineEdit(self.frame_3)
        self.day_spending_2.setGeometry(QtCore.QRect(10, 40, 211, 41))
        self.day_spending_2.setStyleSheet("")
        self.day_spending_2.setText("")
        self.day_spending_2.setObjectName("day_spending_2")
        self.update_norm_button_2 = QtWidgets.QPushButton(self.frame_3)
        self.update_norm_button_2.setGeometry(QtCore.QRect(10, 100, 211, 51))
        self.update_norm_button_2.setStyleSheet("color:black;\n"
"background: rgb(100, 250, 100);")
        self.update_norm_button_2.setObjectName("update_norm_button_2")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 211, 20))
        self.label_16.setStyleSheet("color: black;\n"
"border: none;")
        self.label_16.setObjectName("label_16")
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(260, 190, 581, 221))
        self.frame.setStyleSheet("border-radius: 15px;\n"
"border: 2px solid black;\n"
"color: black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.last_month_2 = QtWidgets.QLabel(self.frame)
        self.last_month_2.setGeometry(QtCore.QRect(300, 170, 271, 41))
        self.last_month_2.setStyleSheet("font-size: 15px;\n"
"")
        self.last_month_2.setObjectName("last_month_2")
        self.last_week_2 = QtWidgets.QLabel(self.frame)
        self.last_week_2.setGeometry(QtCore.QRect(300, 120, 271, 41))
        self.last_week_2.setStyleSheet("font-size: 15px;\n"
"")
        self.last_week_2.setObjectName("last_week_2")
        self.today_2 = QtWidgets.QLabel(self.frame)
        self.today_2.setGeometry(QtCore.QRect(10, 70, 271, 41))
        self.today_2.setStyleSheet("font-size: 15px;\n"
"")
        self.today_2.setObjectName("today_2")
        self.yesterday_2 = QtWidgets.QLabel(self.frame)
        self.yesterday_2.setGeometry(QtCore.QRect(300, 70, 271, 41))
        self.yesterday_2.setStyleSheet("font-size: 15px;\n"
"")
        self.yesterday_2.setObjectName("yesterday_2")
        self.this_month_2 = QtWidgets.QLabel(self.frame)
        self.this_month_2.setGeometry(QtCore.QRect(10, 170, 271, 41))
        self.this_month_2.setStyleSheet("font-size: 15px;\n"
"")
        self.this_month_2.setObjectName("this_month_2")
        self.this_week_2 = QtWidgets.QLabel(self.frame)
        self.this_week_2.setGeometry(QtCore.QRect(10, 120, 271, 41))
        self.this_week_2.setStyleSheet("font-size: 15px;\n"
"")
        self.this_week_2.setObjectName("this_week_2")
        self.daily_norm_2 = QtWidgets.QLabel(self.frame)
        self.daily_norm_2.setGeometry(QtCore.QRect(10, 20, 271, 41))
        self.daily_norm_2.setStyleSheet("font-size: 15px;")
        self.daily_norm_2.setObjectName("daily_norm_2")
        self.frame_4 = QtWidgets.QFrame(self.tab_2)
        self.frame_4.setGeometry(QtCore.QRect(260, 430, 651, 231))
        self.frame_4.setStyleSheet("border-radius: 15px;\n"
"border: 2px solid black;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.min_sum = QtWidgets.QLabel(self.frame_4)
        self.min_sum.setGeometry(QtCore.QRect(10, 70, 301, 41))
        self.min_sum.setStyleSheet("font-size: 15px;\n"
"")
        self.min_sum.setObjectName("min_sum")
        self.all_spent = QtWidgets.QLabel(self.frame_4)
        self.all_spent.setGeometry(QtCore.QRect(10, 20, 631, 41))
        self.all_spent.setStyleSheet("font-size: 15px;\n"
"")
        self.all_spent.setObjectName("all_spent")
        self.middle_sum = QtWidgets.QLabel(self.frame_4)
        self.middle_sum.setGeometry(QtCore.QRect(10, 120, 341, 41))
        self.middle_sum.setStyleSheet("font-size: 15px;\n"
"")
        self.middle_sum.setObjectName("middle_sum")
        self.max_sum = QtWidgets.QLabel(self.frame_4)
        self.max_sum.setGeometry(QtCore.QRect(10, 170, 311, 41))
        self.max_sum.setStyleSheet("font-size: 15px;\n"
"")
        self.max_sum.setObjectName("max_sum")
        self.app_used = QtWidgets.QLabel(self.frame_4)
        self.app_used.setGeometry(QtCore.QRect(330, 70, 311, 41))
        self.app_used.setStyleSheet("font-size: 15px;\n"
"")
        self.app_used.setObjectName("app_used")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(860, 0, 61, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("icon.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.tabWidget1.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "?????????????????? ???? ?????????????? ??????????"))
        item = self.all_spending_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "?????? ??????????"))
        item = self.all_spending_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "???????? ??????????"))
        item = self.all_spending_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "?????????????????? ??????????"))
        item = self.all_spending_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "???????? ??????????"))
        item = self.all_spending_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "?????????? ??????????"))
        item = self.all_spending_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "?????????? ??????????"))
        self.clearSpendingButton.setText(_translate("MainWindow", "???????????????? ?????? ??????????"))
        self.deleteLastSpendingButton.setText(_translate("MainWindow", "?????????????? ?????????????????? ??????????"))
        self.saveUpdatesButton.setText(_translate("MainWindow", "?????????????????? ??????????????????"))
        self.updateTableButton.setText(_translate("MainWindow", "???????????????? ????????????"))
        self.importFromCSVFileButton.setText(_translate("MainWindow", "?????????????????????????? ???????????? ???? CSV-??????????"))
        self.cancelTableUpdateButton.setText(_translate("MainWindow", "???????????????? ?????????????????? ?? ??????????????"))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.mainTab), _translate("MainWindow", "??????????????"))
        self.export_stats_button.setText(_translate("MainWindow", "???????????????????????????? ?????????? ???????????????????? ?? CSV"))
        self.label_25.setText(_translate("MainWindow", "?????? ?????????? ?????? ????????????????????(?? ??????????????????????)"))
        self.calculate_statistics_button.setText(_translate("MainWindow", "???????????????????? ????????????????????"))
        self.add_spending_button_2.setText(_translate("MainWindow", "???????????????? ??????????"))
        self.label_10.setText(_translate("MainWindow", "???????? ??????????:"))
        self.label_3.setText(_translate("MainWindow", "?????? ??????????:"))
        self.label_23.setText(_translate("MainWindow", "?????????????????? ??????????:"))
        self.spending_category_2.setItemText(0, _translate("MainWindow", "?????? ??????????????????"))
        self.spending_category_2.setItemText(1, _translate("MainWindow", "????????????????"))
        self.spending_category_2.setItemText(2, _translate("MainWindow", "????????"))
        self.spending_category_2.setItemText(3, _translate("MainWindow", "?????????????? ??????????????"))
        self.spending_category_2.setItemText(4, _translate("MainWindow", "????????????????????"))
        self.spending_category_2.setItemText(5, _translate("MainWindow", "????????????"))
        self.spending_category_2.setItemText(6, _translate("MainWindow", "??????????????"))
        self.spending_category_2.setItemText(7, _translate("MainWindow", "????????????????"))
        self.spending_category_2.setItemText(8, _translate("MainWindow", "??????????????????????"))
        self.spending_category_2.setItemText(9, _translate("MainWindow", "??????????"))
        self.spending_category_2.setItemText(10, _translate("MainWindow", "????????????..."))
        self.update_norm_button_2.setText(_translate("MainWindow", "???????????????? ??????????"))
        self.label_16.setText(_translate("MainWindow", "?????????????? ?????????? ????????:"))
        self.last_month_2.setText(_translate("MainWindow", "?? ?????????????? ????????????: 0??"))
        self.last_week_2.setText(_translate("MainWindow", "???? ?????????????? ????????????: 0??"))
        self.today_2.setText(_translate("MainWindow", "??????????????: 0??"))
        self.yesterday_2.setText(_translate("MainWindow", "??????????: 0??"))
        self.this_month_2.setText(_translate("MainWindow", "?? ???????? ????????????: 0??"))
        self.this_week_2.setText(_translate("MainWindow", "???? ???????? ????????????: 0??"))
        self.daily_norm_2.setText(_translate("MainWindow", "?????????????? ??????????: 0??"))
        self.min_sum.setText(_translate("MainWindow", "??????. ?????????????????????? ??????????: 0??"))
        self.all_spent.setText(_translate("MainWindow", "?????????? ?????????????????? ???? ?????? ??????????: 0??"))
        self.middle_sum.setText(_translate("MainWindow", "?????????????? ?????????????????????? ??????????: 0??"))
        self.max_sum.setText(_translate("MainWindow", "????????. ?????????????????????? ??????????: 0??"))
        self.app_used.setText(_translate("MainWindow", "???????????????????? ????????????????????????: 0 ????????"))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tab_2), _translate("MainWindow", "??????????????"))
