# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formUi/login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import views.img_logo

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(571, 410)
        Form.setStyleSheet("QWidget{\n"
"background-color: rgb(50, 50, 50);\n"
"font-size:12px;\n"
"font-family: Arial;\n"
"}\n"
"QWidget#widget2{\n"
"    border:1px solid white;\n"
"    border-radius:10px;\n"
"    \n"
"    \n"
"    background-color: rgb(76, 76, 76);\n"
"\n"
"}\n"
"QLabel#label_2{\n"
"color:rgb(163, 163, 163);\n"
"}\n"
"QLabel#label{\n"
"color:rgb(163, 163, 163);\n"
"}\n"
"QLabel#label_2:hover{\n"
"color: rgb(67, 161, 94);\n"
"}\n"
"QLabel#label:hover{\n"
"color: rgb(67, 161, 94);\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"background-color: rgb(67, 161, 94);\n"
"border-radius: 10px;\n"
"color:rgb(0, 22, 0);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border-radius:10px;\n"
"    background-color: rgb(67, 67, 67);\n"
"    color:#fff;\n"
"    padding-left:5px;\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"    border:1px solid #919191;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"    border:1px solid #919191;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"    color:#fff;\n"
"background-color: rgb(76, 76, 76);\n"
"    \n"
"}\n"
"QLabel#label_3{\n"
"    font-size: 26px;\n"
"    font-weight:bold;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"border:1px solid green;\n"
"}\n"
"")
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(30, 20, 511, 371))
        self.widget2.setObjectName("widget2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 220, 231, 31))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit.setGeometry(QtCore.QRect(140, 170, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setGeometry(QtCore.QRect(190, 20, 151, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.widget2)
        self.pushButton.setGeometry(QtCore.QRect(170, 280, 161, 31))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.widget2)
        self.label.setGeometry(QtCore.QRect(150, 330, 71, 16))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.widget2)
        self.label_4.setGeometry(QtCore.QRect(190, 60, 141, 101))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setPixmap(QtGui.QPixmap(":/logo/user.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.widget2)
        self.label_2.setGeometry(QtCore.QRect(250, 330, 131, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LOGIN"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Contraseña"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Usuario"))
        self.label_3.setText(_translate("Form", "Bienvenido"))
        self.pushButton.setText(_translate("Form", "Aceptar"))
        self.label.setText(_translate("Form", "Registrarse"))
        self.label_2.setText(_translate("Form", "Recuperar Contraseña"))
#import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
