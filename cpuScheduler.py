# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cpuScheduler.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import csv

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(494, 211)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.processInput_lbl = QtWidgets.QLabel(Form)
        self.processInput_lbl.setObjectName("processInput_lbl")
        self.gridLayout.addWidget(self.processInput_lbl, 0, 0, 1, 2)
        self.processInput = QtWidgets.QPlainTextEdit(Form)
        self.processInput.setObjectName("processInput")
        self.gridLayout.addWidget(self.processInput, 0, 2, 1, 2)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 4, 5, 1)
        self.output1 = QtWidgets.QTextBrowser(Form)
        self.output1.setObjectName("output1")
        self.gridLayout.addWidget(self.output1, 0, 5, 5, 1)
        spacerItem = QtWidgets.QSpacerItem(68, 132, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 6, 3, 1)
        self.coreCount_lbl = QtWidgets.QLabel(Form)
        self.coreCount_lbl.setObjectName("coreCount_lbl")
        self.gridLayout.addWidget(self.coreCount_lbl, 1, 0, 1, 1)
        self.coreCount = QtWidgets.QSpinBox(Form)
        self.coreCount.setMinimum(1)
        self.coreCount.setMaximum(100)
        self.coreCount.setProperty("value", 4)
        self.coreCount.setObjectName("coreCount")
        self.gridLayout.addWidget(self.coreCount, 1, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(48, 101, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 3, 4, 1)
        self.queues_lbl = QtWidgets.QLabel(Form)
        self.queues_lbl.setObjectName("queues_lbl")
        self.gridLayout.addWidget(self.queues_lbl, 2, 0, 1, 1)
        self.queues = QtWidgets.QSpinBox(Form)
        self.queues.setProperty("value", 1)
        self.queues.setObjectName("queues")
        self.gridLayout.addWidget(self.queues, 2, 1, 1, 2)
        self.waitQueue_lbl = QtWidgets.QLabel(Form)
        self.waitQueue_lbl.setObjectName("waitQueue_lbl")
        self.gridLayout.addWidget(self.waitQueue_lbl, 3, 0, 1, 1)
        self.waitQueues = QtWidgets.QSpinBox(Form)
        self.waitQueues.setProperty("value", 1)
        self.waitQueues.setObjectName("waitQueues")
        self.gridLayout.addWidget(self.waitQueues, 3, 1, 1, 2)
        self.stop_btn = QtWidgets.QPushButton(Form)
        self.stop_btn.setObjectName("stop_btn")
        self.stop_btn.setStyleSheet("background-color: red")
        self.gridLayout.addWidget(self.stop_btn, 3, 6, 1, 1)
        self.ioQueue_lbl = QtWidgets.QLabel(Form)
        self.ioQueue_lbl.setObjectName("ioQueue_lbl")
        self.gridLayout.addWidget(self.ioQueue_lbl, 4, 0, 1, 1)
        self.ioQueues = QtWidgets.QSpinBox(Form)
        self.ioQueues.setProperty("value", 1)
        self.ioQueues.setObjectName("ioQueues")
        self.gridLayout.addWidget(self.ioQueues, 4, 1, 1, 2)
        self.start_btn = QtWidgets.QPushButton(Form)
        self.start_btn.setObjectName("start_btn")
        self.start_btn.setStyleSheet("background-color: green")
        self.gridLayout.addWidget(self.start_btn, 4, 6, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.processInput_lbl.setText(_translate("Form", "Process Input"))
        self.processInput.setPlaceholderText(_translate("Form", "Drag .CSV here"))
        self.coreCount_lbl.setText(_translate("Form", "Core Count"))
        self.coreCount.setWhatsThis(_translate("Form", "<html><head/><body><p>coreCount</p></body></html>"))
        self.queues_lbl.setText(_translate("Form", "Queues"))
        self.waitQueue_lbl.setText(_translate("Form", "Wait Queues"))
        self.stop_btn.setText(_translate("Form", "Stop"))
        self.ioQueue_lbl.setText(_translate("Form", "I/O Queues"))
        self.start_btn.setText(_translate("Form", "Run"))

        

        self.start_btn.clicked.connect(self.start_btn_clicked)
        self.stop_btn.clicked.connect(self.stop_btn_clicked)

    def start_btn_clicked(self):
        with open(self.processInput.toPlainText().strip("file:///")) as f:
            reader = csv.reader(f)
            #for row in reader:
                #self.output1.append(str(row))
            return reader
    def stop_btn_clicked(self):
        self.output1.append("stop clicked")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
