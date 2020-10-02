# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lootowanie.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pynput import mouse


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(352, 236)
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(10, 100, 31, 31))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(50, 100, 31, 31))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(90, 100, 31, 31))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_8 = QtWidgets.QToolButton(Form)
        self.toolButton_8.setGeometry(QtCore.QRect(230, 100, 31, 31))
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_6 = QtWidgets.QToolButton(Form)
        self.toolButton_6.setGeometry(QtCore.QRect(140, 100, 31, 31))
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_7 = QtWidgets.QToolButton(Form)
        self.toolButton_7.setGeometry(QtCore.QRect(270, 100, 31, 31))
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_9 = QtWidgets.QToolButton(Form)
        self.toolButton_9.setGeometry(QtCore.QRect(180, 100, 31, 31))
        self.toolButton_9.setObjectName("toolButton_9")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 20, 20, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(90, 20, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 20, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(130, 90, 3, 61))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(220, 90, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.toolButton_4 = QtWidgets.QToolButton(Form)
        self.toolButton_4.setGeometry(QtCore.QRect(310, 100, 31, 31))
        self.toolButton_4.setObjectName("toolButton_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 62, 71, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(50, 150, 31, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 150, 31, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 150, 31, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(150, 200, 70, 17))
        self.checkBox.setObjectName("checkBox")

        def on_click(x, y, button, pressed):
            with open("coord.txt", "w") as c:
                if button == mouse.Button.left:
                    print(x, y)
                    c.write(f'{x}, {y}')
                    return False
            c.close()

        listener = mouse.Listener(on_click=on_click)
        listener.start()
        ## listener.join()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", "pos1"))
        self.toolButton_2.setText(_translate("Form", "pos2"))
        self.toolButton_3.setText(_translate("Form", "pos3"))
        self.toolButton_8.setText(_translate("Form", "pos8"))
        self.toolButton_6.setText(_translate("Form", "pos6"))
        self.toolButton_7.setText(_translate("Form", "pos7"))
        self.toolButton_9.setText(_translate("Form", "pos9"))
        self.label.setText(_translate("Form", "+"))
        self.comboBox.setItemText(0, _translate("Form", "Shift"))
        self.comboBox_2.setItemText(0, _translate("Form", "Right"))
        self.comboBox_2.setItemText(1, _translate("Form", "Left"))
        self.toolButton_4.setText(_translate("Form", "pos4"))
        self.label_2.setText(_translate("Form", "Coordinates"))
        self.lineEdit.setText(_translate("Form", "F12"))
        self.lineEdit_2.setText(_translate("Form", "F11"))
        self.lineEdit_3.setText(_translate("Form", "F10"))
        self.checkBox.setText(_translate("Form", "RUN?"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
