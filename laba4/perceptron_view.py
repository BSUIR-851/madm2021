# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'perceptron_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_perceptron(object):
    def setupUi(self, form_perceptron):
        form_perceptron.setObjectName("form_perceptron")
        form_perceptron.resize(330, 470)
        form_perceptron.setMinimumSize(QtCore.QSize(330, 470))
        form_perceptron.setMaximumSize(QtCore.QSize(330, 470))
        form_perceptron.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pb_train = QtWidgets.QPushButton(form_perceptron)
        self.pb_train.setGeometry(QtCore.QRect(110, 120, 110, 32))
        self.pb_train.setObjectName("pb_train")
        self.gb_input_learning_data = QtWidgets.QGroupBox(form_perceptron)
        self.gb_input_learning_data.setGeometry(QtCore.QRect(10, 0, 310, 110))
        self.gb_input_learning_data.setObjectName("gb_input_learning_data")
        self.lb_amount_of_vectors = QtWidgets.QLabel(self.gb_input_learning_data)
        self.lb_amount_of_vectors.setGeometry(QtCore.QRect(10, 55, 121, 16))
        self.lb_amount_of_vectors.setObjectName("lb_amount_of_vectors")
        self.le_amount_of_classes = QtWidgets.QLineEdit(self.gb_input_learning_data)
        self.le_amount_of_classes.setGeometry(QtCore.QRect(160, 22, 141, 21))
        self.le_amount_of_classes.setInputMethodHints(QtCore.Qt.ImhNone)
        self.le_amount_of_classes.setReadOnly(False)
        self.le_amount_of_classes.setClearButtonEnabled(True)
        self.le_amount_of_classes.setObjectName("le_amount_of_classes")
        self.le_amount_of_vectors = QtWidgets.QLineEdit(self.gb_input_learning_data)
        self.le_amount_of_vectors.setGeometry(QtCore.QRect(160, 52, 141, 21))
        self.le_amount_of_vectors.setReadOnly(False)
        self.le_amount_of_vectors.setClearButtonEnabled(True)
        self.le_amount_of_vectors.setObjectName("le_amount_of_vectors")
        self.lb_amount_of_classes = QtWidgets.QLabel(self.gb_input_learning_data)
        self.lb_amount_of_classes.setGeometry(QtCore.QRect(10, 25, 121, 16))
        self.lb_amount_of_classes.setObjectName("lb_amount_of_classes")
        self.lb_vector_size = QtWidgets.QLabel(self.gb_input_learning_data)
        self.lb_vector_size.setGeometry(QtCore.QRect(10, 85, 81, 16))
        self.lb_vector_size.setObjectName("lb_vector_size")
        self.le_vector_size = QtWidgets.QLineEdit(self.gb_input_learning_data)
        self.le_vector_size.setGeometry(QtCore.QRect(160, 82, 141, 21))
        self.le_vector_size.setReadOnly(False)
        self.le_vector_size.setClearButtonEnabled(True)
        self.le_vector_size.setObjectName("le_vector_size")
        self.pte_functions = QtWidgets.QPlainTextEdit(form_perceptron)
        self.pte_functions.setGeometry(QtCore.QRect(10, 170, 310, 141))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(10)
        self.pte_functions.setFont(font)
        self.pte_functions.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.pte_functions.setReadOnly(True)
        self.pte_functions.setObjectName("pte_functions")
        self.lb_functions = QtWidgets.QLabel(form_perceptron)
        self.lb_functions.setGeometry(QtCore.QRect(20, 150, 151, 16))
        self.lb_functions.setObjectName("lb_functions")
        self.le_vector = QtWidgets.QLineEdit(form_perceptron)
        self.le_vector.setGeometry(QtCore.QRect(10, 350, 311, 21))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        self.le_vector.setFont(font)
        self.le_vector.setObjectName("le_vector")
        self.lb_vector = QtWidgets.QLabel(form_perceptron)
        self.lb_vector.setGeometry(QtCore.QRect(20, 330, 71, 16))
        self.lb_vector.setObjectName("lb_vector")
        self.pb_classificate = QtWidgets.QPushButton(form_perceptron)
        self.pb_classificate.setGeometry(QtCore.QRect(110, 430, 110, 32))
        self.pb_classificate.setObjectName("pb_classificate")
        self.le_result = QtWidgets.QLineEdit(form_perceptron)
        self.le_result.setGeometry(QtCore.QRect(10, 400, 311, 21))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        self.le_result.setFont(font)
        self.le_result.setReadOnly(True)
        self.le_result.setObjectName("le_result")
        self.lb_result = QtWidgets.QLabel(form_perceptron)
        self.lb_result.setGeometry(QtCore.QRect(20, 380, 71, 16))
        self.lb_result.setObjectName("lb_result")

        self.retranslateUi(form_perceptron)
        QtCore.QMetaObject.connectSlotsByName(form_perceptron)

    def retranslateUi(self, form_perceptron):
        _translate = QtCore.QCoreApplication.translate
        form_perceptron.setWindowTitle(_translate("form_perceptron", "Perceptron method"))
        self.pb_train.setText(_translate("form_perceptron", "Train"))
        self.gb_input_learning_data.setTitle(_translate("form_perceptron", "Input learning data:"))
        self.lb_amount_of_vectors.setText(_translate("form_perceptron", "Amount of vectors:"))
        self.le_amount_of_classes.setText(_translate("form_perceptron", "3"))
        self.le_amount_of_classes.setPlaceholderText(_translate("form_perceptron", "3"))
        self.le_amount_of_vectors.setText(_translate("form_perceptron", "4"))
        self.le_amount_of_vectors.setPlaceholderText(_translate("form_perceptron", "4"))
        self.lb_amount_of_classes.setText(_translate("form_perceptron", "Amount of classes:"))
        self.lb_vector_size.setText(_translate("form_perceptron", "Vector\'s size:"))
        self.le_vector_size.setText(_translate("form_perceptron", "6"))
        self.le_vector_size.setPlaceholderText(_translate("form_perceptron", "6"))
        self.lb_functions.setText(_translate("form_perceptron", "Function\'s coefficients:"))
        self.le_vector.setPlaceholderText(_translate("form_perceptron", "1 2 3"))
        self.lb_vector.setText(_translate("form_perceptron", "Vector:"))
        self.pb_classificate.setText(_translate("form_perceptron", "Classificate"))
        self.lb_result.setText(_translate("form_perceptron", "Result:"))
