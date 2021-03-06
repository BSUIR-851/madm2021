# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hierarchy_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_hierarchy(object):
    def setupUi(self, form_hierarchy):
        form_hierarchy.setObjectName("form_hierarchy")
        form_hierarchy.resize(510, 540)
        form_hierarchy.setMinimumSize(QtCore.QSize(510, 540))
        form_hierarchy.setMaximumSize(QtCore.QSize(510, 540))
        form_hierarchy.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pb_classificate = QtWidgets.QPushButton(form_hierarchy)
        self.pb_classificate.setGeometry(QtCore.QRect(200, 500, 110, 32))
        self.pb_classificate.setObjectName("pb_classificate")
        self.gb_input_data = QtWidgets.QGroupBox(form_hierarchy)
        self.gb_input_data.setGeometry(QtCore.QRect(10, 0, 491, 101))
        self.gb_input_data.setObjectName("gb_input_data")
        self.le_amount_of_objects = QtWidgets.QLineEdit(self.gb_input_data)
        self.le_amount_of_objects.setGeometry(QtCore.QRect(160, 30, 141, 21))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        self.le_amount_of_objects.setFont(font)
        self.le_amount_of_objects.setReadOnly(False)
        self.le_amount_of_objects.setObjectName("le_amount_of_objects")
        self.lb_amount_of_objects = QtWidgets.QLabel(self.gb_input_data)
        self.lb_amount_of_objects.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.lb_amount_of_objects.setObjectName("lb_amount_of_objects")
        self.lb_classification_criterion = QtWidgets.QLabel(self.gb_input_data)
        self.lb_classification_criterion.setGeometry(QtCore.QRect(10, 60, 141, 16))
        self.lb_classification_criterion.setObjectName("lb_classification_criterion")
        self.cb_classification_criterion = QtWidgets.QComboBox(self.gb_input_data)
        self.cb_classification_criterion.setGeometry(QtCore.QRect(160, 60, 141, 26))
        self.cb_classification_criterion.setObjectName("cb_classification_criterion")
        self.lb_chart = QtWidgets.QLabel(form_hierarchy)
        self.lb_chart.setGeometry(QtCore.QRect(20, 120, 151, 16))
        self.lb_chart.setObjectName("lb_chart")
        self.verticalLayoutWidget = QtWidgets.QWidget(form_hierarchy)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 491, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vl_chart_view = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vl_chart_view.setContentsMargins(0, 0, 0, 0)
        self.vl_chart_view.setObjectName("vl_chart_view")

        self.retranslateUi(form_hierarchy)
        QtCore.QMetaObject.connectSlotsByName(form_hierarchy)

    def retranslateUi(self, form_hierarchy):
        _translate = QtCore.QCoreApplication.translate
        form_hierarchy.setWindowTitle(_translate("form_hierarchy", "Hierarchy method"))
        self.pb_classificate.setText(_translate("form_hierarchy", "Classificate"))
        self.gb_input_data.setTitle(_translate("form_hierarchy", "Input data:"))
        self.le_amount_of_objects.setText(_translate("form_hierarchy", "3"))
        self.le_amount_of_objects.setPlaceholderText(_translate("form_hierarchy", "3"))
        self.lb_amount_of_objects.setText(_translate("form_hierarchy", "Amount of objects:"))
        self.lb_classification_criterion.setText(_translate("form_hierarchy", "Classification criterion:"))
        self.lb_chart.setText(_translate("form_hierarchy", "Chart:"))
