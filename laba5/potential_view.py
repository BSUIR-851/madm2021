# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'potential_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_potential(object):
    def setupUi(self, form_potential):
        form_potential.setObjectName("form_potential")
        form_potential.resize(510, 750)
        form_potential.setMinimumSize(QtCore.QSize(510, 750))
        form_potential.setMaximumSize(QtCore.QSize(510, 750))
        form_potential.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pb_train = QtWidgets.QPushButton(form_potential)
        self.pb_train.setGeometry(QtCore.QRect(200, 160, 110, 32))
        self.pb_train.setObjectName("pb_train")
        self.gb_input_learning_data = QtWidgets.QGroupBox(form_potential)
        self.gb_input_learning_data.setGeometry(QtCore.QRect(10, 0, 490, 151))
        self.gb_input_learning_data.setObjectName("gb_input_learning_data")
        self.gb_class_0 = QtWidgets.QGroupBox(self.gb_input_learning_data)
        self.gb_class_0.setGeometry(QtCore.QRect(10, 20, 231, 121))
        self.gb_class_0.setObjectName("gb_class_0")
        self.gb_class_0_point_0 = QtWidgets.QGroupBox(self.gb_class_0)
        self.gb_class_0_point_0.setGeometry(QtCore.QRect(10, 20, 101, 91))
        self.gb_class_0_point_0.setObjectName("gb_class_0_point_0")
        self.le_class_0_point_0_y = QtWidgets.QLineEdit(self.gb_class_0_point_0)
        self.le_class_0_point_0_y.setGeometry(QtCore.QRect(30, 55, 61, 21))
        self.le_class_0_point_0_y.setReadOnly(False)
        self.le_class_0_point_0_y.setClearButtonEnabled(True)
        self.le_class_0_point_0_y.setObjectName("le_class_0_point_0_y")
        self.le_class_0_point_0_x = QtWidgets.QLineEdit(self.gb_class_0_point_0)
        self.le_class_0_point_0_x.setGeometry(QtCore.QRect(30, 25, 61, 21))
        self.le_class_0_point_0_x.setInputMethodHints(QtCore.Qt.ImhNone)
        self.le_class_0_point_0_x.setReadOnly(False)
        self.le_class_0_point_0_x.setClearButtonEnabled(True)
        self.le_class_0_point_0_x.setObjectName("le_class_0_point_0_x")
        self.lb_class_0_point_0_x = QtWidgets.QLabel(self.gb_class_0_point_0)
        self.lb_class_0_point_0_x.setGeometry(QtCore.QRect(10, 27, 16, 16))
        self.lb_class_0_point_0_x.setObjectName("lb_class_0_point_0_x")
        self.lb_class_0_point_0_y = QtWidgets.QLabel(self.gb_class_0_point_0)
        self.lb_class_0_point_0_y.setGeometry(QtCore.QRect(10, 57, 16, 16))
        self.lb_class_0_point_0_y.setObjectName("lb_class_0_point_0_y")
        self.gb_class_0_point_1 = QtWidgets.QGroupBox(self.gb_class_0)
        self.gb_class_0_point_1.setGeometry(QtCore.QRect(120, 20, 101, 91))
        self.gb_class_0_point_1.setObjectName("gb_class_0_point_1")
        self.le_class_0_point_1_y = QtWidgets.QLineEdit(self.gb_class_0_point_1)
        self.le_class_0_point_1_y.setGeometry(QtCore.QRect(30, 55, 61, 21))
        self.le_class_0_point_1_y.setReadOnly(False)
        self.le_class_0_point_1_y.setClearButtonEnabled(True)
        self.le_class_0_point_1_y.setObjectName("le_class_0_point_1_y")
        self.le_class_0_point_1_x = QtWidgets.QLineEdit(self.gb_class_0_point_1)
        self.le_class_0_point_1_x.setGeometry(QtCore.QRect(30, 25, 61, 21))
        self.le_class_0_point_1_x.setInputMethodHints(QtCore.Qt.ImhNone)
        self.le_class_0_point_1_x.setReadOnly(False)
        self.le_class_0_point_1_x.setClearButtonEnabled(True)
        self.le_class_0_point_1_x.setObjectName("le_class_0_point_1_x")
        self.lb_class_0_point_1_x = QtWidgets.QLabel(self.gb_class_0_point_1)
        self.lb_class_0_point_1_x.setGeometry(QtCore.QRect(10, 27, 16, 16))
        self.lb_class_0_point_1_x.setObjectName("lb_class_0_point_1_x")
        self.lb_class_0_point_1_y = QtWidgets.QLabel(self.gb_class_0_point_1)
        self.lb_class_0_point_1_y.setGeometry(QtCore.QRect(10, 57, 16, 16))
        self.lb_class_0_point_1_y.setObjectName("lb_class_0_point_1_y")
        self.gb_class_1 = QtWidgets.QGroupBox(self.gb_input_learning_data)
        self.gb_class_1.setGeometry(QtCore.QRect(250, 20, 231, 121))
        self.gb_class_1.setObjectName("gb_class_1")
        self.gb_class_1_point_0 = QtWidgets.QGroupBox(self.gb_class_1)
        self.gb_class_1_point_0.setGeometry(QtCore.QRect(10, 20, 101, 91))
        self.gb_class_1_point_0.setObjectName("gb_class_1_point_0")
        self.le_class_1_point_0_y = QtWidgets.QLineEdit(self.gb_class_1_point_0)
        self.le_class_1_point_0_y.setGeometry(QtCore.QRect(30, 55, 61, 21))
        self.le_class_1_point_0_y.setReadOnly(False)
        self.le_class_1_point_0_y.setClearButtonEnabled(True)
        self.le_class_1_point_0_y.setObjectName("le_class_1_point_0_y")
        self.le_class_1_point_0_x = QtWidgets.QLineEdit(self.gb_class_1_point_0)
        self.le_class_1_point_0_x.setGeometry(QtCore.QRect(30, 25, 61, 21))
        self.le_class_1_point_0_x.setInputMethodHints(QtCore.Qt.ImhNone)
        self.le_class_1_point_0_x.setReadOnly(False)
        self.le_class_1_point_0_x.setClearButtonEnabled(True)
        self.le_class_1_point_0_x.setObjectName("le_class_1_point_0_x")
        self.lb_class_1_point_0_x = QtWidgets.QLabel(self.gb_class_1_point_0)
        self.lb_class_1_point_0_x.setGeometry(QtCore.QRect(10, 27, 16, 16))
        self.lb_class_1_point_0_x.setObjectName("lb_class_1_point_0_x")
        self.lb_class_1_point_0_y = QtWidgets.QLabel(self.gb_class_1_point_0)
        self.lb_class_1_point_0_y.setGeometry(QtCore.QRect(10, 57, 16, 16))
        self.lb_class_1_point_0_y.setObjectName("lb_class_1_point_0_y")
        self.gb_class_1_point_1 = QtWidgets.QGroupBox(self.gb_class_1)
        self.gb_class_1_point_1.setGeometry(QtCore.QRect(120, 20, 101, 91))
        self.gb_class_1_point_1.setObjectName("gb_class_1_point_1")
        self.le_class_1_point_1_y = QtWidgets.QLineEdit(self.gb_class_1_point_1)
        self.le_class_1_point_1_y.setGeometry(QtCore.QRect(30, 55, 61, 21))
        self.le_class_1_point_1_y.setReadOnly(False)
        self.le_class_1_point_1_y.setClearButtonEnabled(True)
        self.le_class_1_point_1_y.setObjectName("le_class_1_point_1_y")
        self.le_class_1_point_1_x = QtWidgets.QLineEdit(self.gb_class_1_point_1)
        self.le_class_1_point_1_x.setGeometry(QtCore.QRect(30, 25, 61, 21))
        self.le_class_1_point_1_x.setInputMethodHints(QtCore.Qt.ImhNone)
        self.le_class_1_point_1_x.setReadOnly(False)
        self.le_class_1_point_1_x.setClearButtonEnabled(True)
        self.le_class_1_point_1_x.setObjectName("le_class_1_point_1_x")
        self.lb_class_1_point_1_x = QtWidgets.QLabel(self.gb_class_1_point_1)
        self.lb_class_1_point_1_x.setGeometry(QtCore.QRect(10, 27, 16, 16))
        self.lb_class_1_point_1_x.setObjectName("lb_class_1_point_1_x")
        self.lb_class_1_point_1_y = QtWidgets.QLabel(self.gb_class_1_point_1)
        self.lb_class_1_point_1_y.setGeometry(QtCore.QRect(10, 57, 16, 16))
        self.lb_class_1_point_1_y.setObjectName("lb_class_1_point_1_y")
        self.lb_graphic = QtWidgets.QLabel(form_potential)
        self.lb_graphic.setGeometry(QtCore.QRect(20, 250, 151, 16))
        self.lb_graphic.setObjectName("lb_graphic")
        self.pb_classificate = QtWidgets.QPushButton(form_potential)
        self.pb_classificate.setGeometry(QtCore.QRect(200, 711, 110, 32))
        self.pb_classificate.setObjectName("pb_classificate")
        self.le_result = QtWidgets.QLineEdit(form_potential)
        self.le_result.setGeometry(QtCore.QRect(210, 686, 101, 21))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        self.le_result.setFont(font)
        self.le_result.setReadOnly(True)
        self.le_result.setObjectName("le_result")
        self.lb_result = QtWidgets.QLabel(form_potential)
        self.lb_result.setGeometry(QtCore.QRect(160, 686, 51, 16))
        self.lb_result.setObjectName("lb_result")
        self.gv_graphic = QtWidgets.QGraphicsView(form_potential)
        self.gv_graphic.setGeometry(QtCore.QRect(10, 270, 490, 350))
        self.gv_graphic.setObjectName("gv_graphic")
        self.gb_point = QtWidgets.QGroupBox(form_potential)
        self.gb_point.setGeometry(QtCore.QRect(155, 626, 201, 51))
        self.gb_point.setObjectName("gb_point")
        self.le_point_y = QtWidgets.QLineEdit(self.gb_point)
        self.le_point_y.setGeometry(QtCore.QRect(130, 25, 61, 21))
        self.le_point_y.setReadOnly(False)
        self.le_point_y.setClearButtonEnabled(True)
        self.le_point_y.setObjectName("le_point_y")
        self.le_point_x = QtWidgets.QLineEdit(self.gb_point)
        self.le_point_x.setGeometry(QtCore.QRect(30, 25, 61, 21))
        self.le_point_x.setInputMethodHints(QtCore.Qt.ImhNone)
        self.le_point_x.setReadOnly(False)
        self.le_point_x.setClearButtonEnabled(True)
        self.le_point_x.setObjectName("le_point_x")
        self.lb_point_x = QtWidgets.QLabel(self.gb_point)
        self.lb_point_x.setGeometry(QtCore.QRect(10, 27, 16, 16))
        self.lb_point_x.setObjectName("lb_point_x")
        self.lb_point_y = QtWidgets.QLabel(self.gb_point)
        self.lb_point_y.setGeometry(QtCore.QRect(110, 27, 16, 16))
        self.lb_point_y.setObjectName("lb_point_y")
        self.lb_separated_function = QtWidgets.QLabel(form_potential)
        self.lb_separated_function.setGeometry(QtCore.QRect(20, 200, 131, 16))
        self.lb_separated_function.setObjectName("lb_separated_function")
        self.le_separated_function = QtWidgets.QLineEdit(form_potential)
        self.le_separated_function.setGeometry(QtCore.QRect(10, 220, 491, 21))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        self.le_separated_function.setFont(font)
        self.le_separated_function.setReadOnly(True)
        self.le_separated_function.setObjectName("le_separated_function")

        self.retranslateUi(form_potential)
        QtCore.QMetaObject.connectSlotsByName(form_potential)

    def retranslateUi(self, form_potential):
        _translate = QtCore.QCoreApplication.translate
        form_potential.setWindowTitle(_translate("form_potential", "Potential method"))
        self.pb_train.setText(_translate("form_potential", "Train"))
        self.gb_input_learning_data.setTitle(_translate("form_potential", "Input learning data:"))
        self.gb_class_0.setTitle(_translate("form_potential", "Class 0:"))
        self.gb_class_0_point_0.setTitle(_translate("form_potential", "Point 0:"))
        self.le_class_0_point_0_y.setText(_translate("form_potential", "2"))
        self.le_class_0_point_0_y.setPlaceholderText(_translate("form_potential", "2"))
        self.le_class_0_point_0_x.setText(_translate("form_potential", "3"))
        self.le_class_0_point_0_x.setPlaceholderText(_translate("form_potential", "3"))
        self.lb_class_0_point_0_x.setText(_translate("form_potential", "X:"))
        self.lb_class_0_point_0_y.setText(_translate("form_potential", "Y:"))
        self.gb_class_0_point_1.setTitle(_translate("form_potential", "Point 1:"))
        self.le_class_0_point_1_y.setText(_translate("form_potential", "0"))
        self.le_class_0_point_1_y.setPlaceholderText(_translate("form_potential", "0"))
        self.le_class_0_point_1_x.setText(_translate("form_potential", "-5"))
        self.le_class_0_point_1_x.setPlaceholderText(_translate("form_potential", "-5"))
        self.lb_class_0_point_1_x.setText(_translate("form_potential", "X:"))
        self.lb_class_0_point_1_y.setText(_translate("form_potential", "Y:"))
        self.gb_class_1.setTitle(_translate("form_potential", "Class 1:"))
        self.gb_class_1_point_0.setTitle(_translate("form_potential", "Point 0:"))
        self.le_class_1_point_0_y.setText(_translate("form_potential", "-7"))
        self.le_class_1_point_0_y.setPlaceholderText(_translate("form_potential", "-7"))
        self.le_class_1_point_0_x.setText(_translate("form_potential", "4"))
        self.le_class_1_point_0_x.setPlaceholderText(_translate("form_potential", "4"))
        self.lb_class_1_point_0_x.setText(_translate("form_potential", "X:"))
        self.lb_class_1_point_0_y.setText(_translate("form_potential", "Y:"))
        self.gb_class_1_point_1.setTitle(_translate("form_potential", "Point 1:"))
        self.le_class_1_point_1_y.setText(_translate("form_potential", "1"))
        self.le_class_1_point_1_y.setPlaceholderText(_translate("form_potential", "1"))
        self.le_class_1_point_1_x.setText(_translate("form_potential", "1"))
        self.le_class_1_point_1_x.setPlaceholderText(_translate("form_potential", "1"))
        self.lb_class_1_point_1_x.setText(_translate("form_potential", "X:"))
        self.lb_class_1_point_1_y.setText(_translate("form_potential", "Y:"))
        self.lb_graphic.setText(_translate("form_potential", "Graphic:"))
        self.pb_classificate.setText(_translate("form_potential", "Classificate"))
        self.lb_result.setText(_translate("form_potential", "Result:"))
        self.gb_point.setTitle(_translate("form_potential", "Point:"))
        self.le_point_y.setText(_translate("form_potential", "1"))
        self.le_point_y.setPlaceholderText(_translate("form_potential", "1"))
        self.le_point_x.setText(_translate("form_potential", "1"))
        self.le_point_x.setPlaceholderText(_translate("form_potential", "1"))
        self.lb_point_x.setText(_translate("form_potential", "X:"))
        self.lb_point_y.setText(_translate("form_potential", "Y:"))
        self.lb_separated_function.setText(_translate("form_potential", "Separated function:"))
