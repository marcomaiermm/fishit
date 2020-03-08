# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        #Window.resize(338, 85)
        Window.setFixedSize(338, 85)
        Window.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Window.setAcceptDrops(False)
        self.fish_button = QtWidgets.QPushButton(Window)
        self.fish_button.setGeometry(QtCore.QRect(10, 10, 81, 23))
        self.fish_button.setObjectName("fish_button")
        self.stop_button = QtWidgets.QPushButton(Window)
        self.stop_button.setGeometry(QtCore.QRect(104, 10, 81, 23))
        self.stop_button.setObjectName("stop_button")
        self.status_label = QtWidgets.QLabel(Window)
        self.status_label.setGeometry(QtCore.QRect(200, 10, 41, 21))
        self.status_label.setObjectName("status_label")
        self.status_edit = QtWidgets.QLabel(Window)
        self.status_edit.setGeometry(QtCore.QRect(250, 10, 71, 21))
        self.status_edit.setText("")
        self.status_edit.setObjectName("status_edit")
        self.time_label = QtWidgets.QLabel(Window)
        self.time_label.setGeometry(QtCore.QRect(110, 50, 41, 21))
        self.time_label.setObjectName("time_label")
        self.time_edit = QtWidgets.QLabel(Window)
        self.time_edit.setGeometry(QtCore.QRect(150, 50, 91, 21))
        self.time_edit.setText("")
        self.time_edit.setObjectName("time_edit")
        self.catched_edit = QtWidgets.QLabel(Window)
        self.catched_edit.setGeometry(QtCore.QRect(250, 30, 71, 21))
        self.catched_edit.setText("")
        self.catched_edit.setObjectName("catched_edit")
        self.catched_label = QtWidgets.QLabel(Window)
        self.catched_label.setGeometry(QtCore.QRect(200, 30, 51, 21))
        self.catched_label.setObjectName("catched_label")
        self.duration = QtWidgets.QComboBox(Window)
        self.duration.setGeometry(QtCore.QRect(10, 50, 69, 22))
        self.duration.setObjectName("duration")
        self.duration.addItem("")
        self.duration.addItem("")
        self.duration.addItem("")
        self.duration.addItem("")
        self.duration.addItem("")
        self.duration.addItem("")
        self.duration.addItem("")
        self.duration.addItem("")
        self.duration.addItem("")
        self.duration.addItem("")

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Fishit"))
        self.fish_button.setText(_translate("Window", "Fish"))
        self.stop_button.setText(_translate("Window", "Stop"))
        self.status_label.setText(_translate("Window", "Status:"))
        self.time_label.setText(_translate("Window", "Time:"))
        self.catched_label.setText(_translate("Window", "Catched:"))
        self.duration.setItemText(0, _translate("Window", "5"))
        self.duration.setItemText(1, _translate("Window", "10"))
        self.duration.setItemText(2, _translate("Window", "15"))
        self.duration.setItemText(3, _translate("Window", "20"))
        self.duration.setItemText(4, _translate("Window", "25"))
        self.duration.setItemText(5, _translate("Window", "30"))
        self.duration.setItemText(6, _translate("Window", "45"))
        self.duration.setItemText(7, _translate("Window", "60"))
        self.duration.setItemText(8, _translate("Window", "120"))
        self.duration.setItemText(9, _translate("Window", "180"))
