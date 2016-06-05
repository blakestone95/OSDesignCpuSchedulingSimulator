# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cpuSchedulerGUI2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import csv

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(831, 313)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widgetOutput = QtWidgets.QWidget(Form)
        self.widgetOutput.setMinimumSize(QtCore.QSize(401, 291))
        self.widgetOutput.setObjectName("widgetOutput")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widgetOutput)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.processInput = QtWidgets.QTextEdit(self.widgetOutput)
        self.processInput.setMinimumSize(QtCore.QSize(131, 31))
        self.processInput.setMaximumSize(QtCore.QSize(131, 16777215))
        self.processInput.setObjectName("processInput")
        self.gridLayout_2.addWidget(self.processInput, 0, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.widgetOutput)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 3, 9, 1)
        self.output1 = QtWidgets.QTextBrowser(self.widgetOutput)
        self.output1.setMinimumSize(QtCore.QSize(111, 131))
        self.output1.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.output1.setObjectName("output1")
        self.gridLayout_2.addWidget(self.output1, 0, 4, 4, 1)
        self.output2 = QtWidgets.QTextBrowser(self.widgetOutput)
        self.output2.setMinimumSize(QtCore.QSize(111, 131))
        self.output2.setObjectName("output2")
        self.gridLayout_2.addWidget(self.output2, 0, 5, 4, 1)
        self.algorithm_lbl = QtWidgets.QLabel(self.widgetOutput)
        self.algorithm_lbl.setObjectName("algorithm_lbl")
        self.gridLayout_2.addWidget(self.algorithm_lbl, 1, 0, 1, 1)
        self.algorithm = QtWidgets.QComboBox(self.widgetOutput)
        self.algorithm.setObjectName("algorithm")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.gridLayout_2.addWidget(self.algorithm, 1, 1, 1, 2)
        self.coreCount_lbl = QtWidgets.QLabel(self.widgetOutput)
        self.coreCount_lbl.setObjectName("coreCount_lbl")
        self.gridLayout_2.addWidget(self.coreCount_lbl, 2, 0, 1, 2)
        self.coreCount = QtWidgets.QSpinBox(self.widgetOutput)
        self.coreCount.setProperty("value", 4)
        self.coreCount.setObjectName("coreCount")
        self.gridLayout_2.addWidget(self.coreCount, 2, 2, 1, 1)
        self.queue_lbl = QtWidgets.QLabel(self.widgetOutput)
        self.queue_lbl.setObjectName("queue_lbl")
        self.gridLayout_2.addWidget(self.queue_lbl, 3, 0, 1, 2)
        self.queues = QtWidgets.QSpinBox(self.widgetOutput)
        self.queues.setMinimum(0)
        self.queues.setMaximum(99)
        self.queues.setProperty("value", 1)
        self.queues.setObjectName("queues")
        self.gridLayout_2.addWidget(self.queues, 3, 2, 1, 1)
        self.waitQueues_lbl = QtWidgets.QLabel(self.widgetOutput)
        self.waitQueues_lbl.setObjectName("waitQueues_lbl")
        self.gridLayout_2.addWidget(self.waitQueues_lbl, 4, 0, 1, 2)
        self.waitQueues = QtWidgets.QSpinBox(self.widgetOutput)
        self.waitQueues.setProperty("value", 1)
        self.waitQueues.setObjectName("waitQueues")
        self.gridLayout_2.addWidget(self.waitQueues, 4, 2, 1, 1)
        self.output3 = QtWidgets.QTextBrowser(self.widgetOutput)
        self.output3.setMinimumSize(QtCore.QSize(111, 131))
        self.output3.setObjectName("output3")
        self.gridLayout_2.addWidget(self.output3, 4, 4, 5, 1)
        self.output4 = QtWidgets.QTextBrowser(self.widgetOutput)
        self.output4.setMinimumSize(QtCore.QSize(111, 131))
        self.output4.setObjectName("output4")
        self.gridLayout_2.addWidget(self.output4, 4, 5, 5, 1)
        self.ioQueue_lbl = QtWidgets.QLabel(self.widgetOutput)
        self.ioQueue_lbl.setObjectName("ioQueue_lbl")
        self.gridLayout_2.addWidget(self.ioQueue_lbl, 5, 0, 1, 2)
        self.ioQueues = QtWidgets.QSpinBox(self.widgetOutput)
        self.ioQueues.setProperty("value", 1)
        self.ioQueues.setObjectName("ioQueues")
        self.gridLayout_2.addWidget(self.ioQueues, 5, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.widgetOutput)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 6, 0, 1, 3)
        self.run_btn = QtWidgets.QPushButton(self.widgetOutput)
        self.run_btn.setMinimumSize(QtCore.QSize(131, 31))
        self.run_btn.setObjectName("run_btn")
        self.gridLayout_2.addWidget(self.run_btn, 7, 0, 1, 3)
        self.stop_btn = QtWidgets.QPushButton(self.widgetOutput)
        self.stop_btn.setMinimumSize(QtCore.QSize(131, 31))
        self.stop_btn.setObjectName("stop_btn")
        self.gridLayout_2.addWidget(self.stop_btn, 8, 0, 1, 3)
        self.horizontalLayout.addWidget(self.widgetOutput)
        self.widgetGraph = QtWidgets.QWidget(Form)
        self.widgetGraph.setMinimumSize(QtCore.QSize(401, 291))
        self.widgetGraph.setObjectName("widgetGraph")
        self.gridLayout = QtWidgets.QGridLayout(self.widgetGraph)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.widgetGraph)
        self.graphicsView.setMinimumSize(QtCore.QSize(379, 269))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widgetGraph)
        self.widgetGraph.raise_()
        self.widgetOutput.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.processInput.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.processInput.setPlaceholderText(_translate("Form", "process input .csv"))
        self.output1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.output1.setPlaceholderText(_translate("Form", "Sample Output Box 1"))
        self.output2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.output2.setPlaceholderText(_translate("Form", "Sample Output Box 2"))
        self.algorithm_lbl.setText(_translate("Form", "Algorithm"))
        self.algorithm.setItemText(0, _translate("Form", "FCFS"))
        self.algorithm.setItemText(1, _translate("Form", "RR"))
        self.algorithm.setItemText(2, _translate("Form", "SPN"))
        self.algorithm.setItemText(3, _translate("Form", "SRT"))
        self.algorithm.setItemText(4, _translate("Form", "HRRN"))
        self.algorithm.setItemText(5, _translate("Form", "FB"))
        self.coreCount_lbl.setText(_translate("Form", "Core Count"))
        self.queue_lbl.setText(_translate("Form", "Queues"))
        self.queues.setWhatsThis(_translate("Form", "<html><head/><body><p>coreCount</p></body></html>"))
        self.waitQueues_lbl.setText(_translate("Form", "Wait Queues"))
        self.output3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.output3.setPlaceholderText(_translate("Form", "Sample Output Box 3"))
        self.output4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.output4.setPlaceholderText(_translate("Form", "Sample Output Box 4"))
        self.ioQueue_lbl.setText(_translate("Form", "I/O Queues"))
        self.run_btn.setText(_translate("Form", "Run"))
        self.stop_btn.setText(_translate("Form", "Stop"))

        self.run_btn.clicked.connect(self.run_btn_clicked)
        self.stop_btn.clicked.connect(self.stop_btn_clicked)

    def run_btn_clicked(self):
        processInputLocation = self.processInput.toPlainText()
        processInputLocation = processInputLocation.replace('file:///', '')
        with open(processInputLocation) as f:
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