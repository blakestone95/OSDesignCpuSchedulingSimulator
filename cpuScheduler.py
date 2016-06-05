# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cpuSchedulerGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import csv

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(831, 363)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widgetOutput = QtWidgets.QWidget(Form)
        self.widgetOutput.setMinimumSize(QtCore.QSize(401, 341))
        self.widgetOutput.setObjectName("widgetOutput")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widgetOutput)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.output1 = QtWidgets.QTextBrowser(self.widgetOutput)
        self.output1.setMinimumSize(QtCore.QSize(111, 151))
        self.output1.setObjectName("output1")
        self.gridLayout_2.addWidget(self.output1, 0, 3, 4, 1)
        self.coreCount_lbl = QtWidgets.QLabel(self.widgetOutput)
        self.coreCount_lbl.setObjectName("coreCount_lbl")
        self.gridLayout_2.addWidget(self.coreCount_lbl, 2, 0, 1, 2)
        self.algorithm = QtWidgets.QComboBox(self.widgetOutput)
        self.algorithm.setObjectName("algorithm")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.gridLayout_2.addWidget(self.algorithm, 1, 1, 1, 2)
        self.queues = QtWidgets.QSpinBox(self.widgetOutput)
        self.queues.setProperty("value", 1)
        self.queues.setObjectName("queues")
        self.gridLayout_2.addWidget(self.queues, 2, 2, 1, 1)
        self.waitQueues = QtWidgets.QSpinBox(self.widgetOutput)
        self.waitQueues.setProperty("value", 1)
        self.waitQueues.setObjectName("waitQueues")
        self.gridLayout_2.addWidget(self.waitQueues, 4, 2, 1, 1)
        self.processInput = QtWidgets.QTextEdit(self.widgetOutput)
        self.processInput.setMinimumSize(QtCore.QSize(131, 29))
        self.processInput.setObjectName("processInput")
        self.gridLayout_2.addWidget(self.processInput, 0, 0, 1, 3)
        self.output1_3 = QtWidgets.QTextBrowser(self.widgetOutput)
        self.output1_3.setMinimumSize(QtCore.QSize(111, 151))
        self.output1_3.setObjectName("output1_3")
        self.gridLayout_2.addWidget(self.output1_3, 4, 4, 4, 1)
        self.waitQueue_lbl = QtWidgets.QLabel(self.widgetOutput)
        self.waitQueue_lbl.setObjectName("waitQueue_lbl")
        self.gridLayout_2.addWidget(self.waitQueue_lbl, 3, 0, 1, 2)
        self.queues_lbl = QtWidgets.QLabel(self.widgetOutput)
        self.queues_lbl.setObjectName("queues_lbl")
        self.gridLayout_2.addWidget(self.queues_lbl, 4, 0, 1, 2)
        self.ioQueue_lbl = QtWidgets.QLabel(self.widgetOutput)
        self.ioQueue_lbl.setObjectName("ioQueue_lbl")
        self.gridLayout_2.addWidget(self.ioQueue_lbl, 5, 0, 1, 2)
        self.output2 = QtWidgets.QTextBrowser(self.widgetOutput)
        self.output2.setMinimumSize(QtCore.QSize(111, 151))
        self.output2.setObjectName("output2")
        self.gridLayout_2.addWidget(self.output2, 0, 4, 4, 1)
        self.ioQueues = QtWidgets.QSpinBox(self.widgetOutput)
        self.ioQueues.setProperty("value", 1)
        self.ioQueues.setObjectName("ioQueues")
        self.gridLayout_2.addWidget(self.ioQueues, 5, 2, 1, 1)
        self.coreCount = QtWidgets.QSpinBox(self.widgetOutput)
        self.coreCount.setMinimum(0)
        self.coreCount.setMaximum(99)
        self.coreCount.setProperty("value", 4)
        self.coreCount.setObjectName("coreCount")
        self.gridLayout_2.addWidget(self.coreCount, 3, 2, 1, 1)
        self.run_btn = QtWidgets.QPushButton(self.widgetOutput)
        self.run_btn.setObjectName("run_btn")
        self.gridLayout_2.addWidget(self.run_btn, 6, 0, 1, 3)
        self.algorithm_lbl = QtWidgets.QLabel(self.widgetOutput)
        self.algorithm_lbl.setObjectName("algorithm_lbl")
        self.gridLayout_2.addWidget(self.algorithm_lbl, 1, 0, 1, 1)
        self.output3 = QtWidgets.QTextBrowser(self.widgetOutput)
        self.output3.setMinimumSize(QtCore.QSize(111, 151))
        self.output3.setObjectName("output3")
        self.gridLayout_2.addWidget(self.output3, 4, 3, 4, 1)
        self.stop_btn = QtWidgets.QPushButton(self.widgetOutput)
        self.stop_btn.setObjectName("stop_btn")
        self.gridLayout_2.addWidget(self.stop_btn, 7, 0, 1, 3)
        self.horizontalLayout.addWidget(self.widgetOutput)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(401, 341))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setMinimumSize(QtCore.QSize(379, 319))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget)
        self.widget.raise_()
        self.widgetOutput.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.output1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sample Output Box 1</p></body></html>"))
        self.coreCount_lbl.setText(_translate("Form", "Core Count"))
        self.algorithm.setItemText(0, _translate("Form", "FCFS"))
        self.algorithm.setItemText(1, _translate("Form", "RR"))
        self.algorithm.setItemText(2, _translate("Form", "SPN"))
        self.algorithm.setItemText(3, _translate("Form", "SRT"))
        self.algorithm.setItemText(4, _translate("Form", "HRRN"))
        self.algorithm.setItemText(5, _translate("Form", "FB"))
        self.processInput.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.processInput.setPlaceholderText(_translate("Form", "process input .csv"))
        self.output1_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sample Output Box 4</p></body></html>"))
        self.waitQueue_lbl.setText(_translate("Form", "Wait Queues"))
        self.queues_lbl.setText(_translate("Form", "Queues"))
        self.ioQueue_lbl.setText(_translate("Form", "I/O Queues"))
        self.output2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sample Output Box 2</p></body></html>"))
        self.coreCount.setWhatsThis(_translate("Form", "<html><head/><body><p>coreCount</p></body></html>"))
        self.run_btn.setText(_translate("Form", "Run"))
        self.algorithm_lbl.setText(_translate("Form", "Algorithm"))
        self.output3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sample Output Box 3</p></body></html>"))
        self.stop_btn.setText(_translate("Form", "Stop"))

        self.run_btn.clicked.connect(self.run_btn_clicked)
        self.stop_btn.clicked.connect(self.stop_btn_clicked)

    def run_btn_clicked(self):
        with open(self.processInput.toPlainText()) as f:
            reader = csv.reader(f)
            for row in reader:
                self.output1.append(str(row))
                print(type(row))
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