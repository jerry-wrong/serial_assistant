# Form implementation generated from reading ui file 'serial_ui.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Serial(object):
    def setupUi(self, Serial):
        Serial.setObjectName("Serial")
        Serial.resize(668, 583)
        self.gridLayout_2 = QtWidgets.QGridLayout(Serial)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.textEdit_receive = QtWidgets.QTextEdit(Serial)
        self.textEdit_receive.setObjectName("textEdit_receive")
        self.horizontalLayout_9.addWidget(self.textEdit_receive)
        self.groupBox = QtWidgets.QGroupBox(Serial)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_Baud = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_Baud.setObjectName("comboBox_Baud")
        self.horizontalLayout.addWidget(self.comboBox_Baud)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_Stop = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_Stop.setObjectName("comboBox_Stop")
        self.horizontalLayout_2.addWidget(self.comboBox_Stop)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_Data = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_Data.setObjectName("comboBox_Data")
        self.horizontalLayout_3.addWidget(self.comboBox_Data)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.comboBox_Check = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_Check.setObjectName("comboBox_Check")
        self.horizontalLayout_4.addWidget(self.comboBox_Check)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.pushButton_Open = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.horizontalLayout_5.addWidget(self.pushButton_Open)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.pushButton_ReceiveClean = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ReceiveClean.setObjectName("pushButton_ReceiveClean")
        self.horizontalLayout_6.addWidget(self.pushButton_ReceiveClean)
        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 0, 1, 2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox_Hexview = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Hexview.setObjectName("checkBox_Hexview")
        self.horizontalLayout_7.addWidget(self.checkBox_Hexview)
        self.checkBox_DTR = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_DTR.setObjectName("checkBox_DTR")
        self.horizontalLayout_7.addWidget(self.checkBox_DTR)
        self.gridLayout.addLayout(self.horizontalLayout_7, 7, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox_RTS = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_RTS.setObjectName("checkBox_RTS")
        self.horizontalLayout_8.addWidget(self.checkBox_RTS)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setEnabled(False)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_8.addWidget(self.checkBox_5)
        self.gridLayout.addLayout(self.horizontalLayout_8, 8, 0, 1, 2)
        self.checkBox_TimeStamp = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_TimeStamp.setObjectName("checkBox_TimeStamp")
        self.gridLayout.addWidget(self.checkBox_TimeStamp, 9, 0, 1, 2)
        self.comboBox_Com = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_Com.setObjectName("comboBox_Com")
        self.gridLayout.addWidget(self.comboBox_Com, 0, 0, 1, 2)
        self.horizontalLayout_9.addWidget(self.groupBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.textEdit_Send = QtWidgets.QTextEdit(Serial)
        self.textEdit_Send.setObjectName("textEdit_Send")
        self.horizontalLayout_10.addWidget(self.textEdit_Send)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_Send = QtWidgets.QPushButton(Serial)
        self.pushButton_Send.setObjectName("pushButton_Send")
        self.verticalLayout.addWidget(self.pushButton_Send)
        self.pushButton_CleanSend = QtWidgets.QPushButton(Serial)
        self.pushButton_CleanSend.setObjectName("pushButton_CleanSend")
        self.verticalLayout.addWidget(self.pushButton_CleanSend)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.checkBox_TimeSend = QtWidgets.QCheckBox(Serial)
        self.checkBox_TimeSend.setObjectName("checkBox_TimeSend")
        self.horizontalLayout_11.addWidget(self.checkBox_TimeSend)
        self.label_11 = QtWidgets.QLabel(Serial)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.lineEdit_IntervalTime = QtWidgets.QLineEdit(Serial)
        self.lineEdit_IntervalTime.setObjectName("lineEdit_IntervalTime")
        self.horizontalLayout_11.addWidget(self.lineEdit_IntervalTime)
        self.label_12 = QtWidgets.QLabel(Serial)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.checkBox_HexSend = QtWidgets.QCheckBox(Serial)
        self.checkBox_HexSend.setObjectName("checkBox_HexSend")
        self.horizontalLayout_12.addWidget(self.checkBox_HexSend)
        self.checkBox_End = QtWidgets.QCheckBox(Serial)
        self.checkBox_End.setObjectName("checkBox_End")
        self.horizontalLayout_12.addWidget(self.checkBox_End)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_send = QtWidgets.QLabel(Serial)
        self.label_send.setMinimumSize(QtCore.QSize(100, 0))
        self.label_send.setObjectName("label_send")
        self.verticalLayout_3.addWidget(self.label_send)
        self.label_receive = QtWidgets.QLabel(Serial)
        self.label_receive.setObjectName("label_receive")
        self.verticalLayout_3.addWidget(self.label_receive)
        self.horizontalLayout_13.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(369, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_13, 2, 0, 1, 1)

        self.retranslateUi(Serial)
        QtCore.QMetaObject.connectSlotsByName(Serial)

    def retranslateUi(self, Serial):
        _translate = QtCore.QCoreApplication.translate
        Serial.setWindowTitle(_translate("Serial", "Form"))
        self.groupBox.setTitle(_translate("Serial", "Serial Choice"))
        self.label.setText(_translate("Serial", "Baud Rates："))
        self.label_2.setText(_translate("Serial", "Stop Bits:"))
        self.label_3.setText(_translate("Serial", "Data Bits:"))
        self.label_4.setText(_translate("Serial", "Parity:"))
        self.label_5.setText(_translate("Serial", "Serial Op:"))
        self.pushButton_Open.setText(_translate("Serial", "Open Serial"))
        self.pushButton_2.setText(_translate("Serial", "Save Serial"))
        self.pushButton_ReceiveClean.setText(_translate("Serial", "Clear Data"))
        self.checkBox_Hexview.setText(_translate("Serial", "hex show"))
        self.checkBox_DTR.setText(_translate("Serial", "DTR"))
        self.checkBox_RTS.setText(_translate("Serial", "RTS"))
        self.checkBox_5.setText(_translate("Serial", "Auto Save"))
        self.checkBox_TimeStamp.setText(_translate("Serial", "Time Stamp"))
        self.pushButton_Send.setText(_translate("Serial", "Send"))
        self.pushButton_CleanSend.setText(_translate("Serial", "Clear Send"))
        self.checkBox_TimeSend.setText(_translate("Serial", "send on time"))
        self.label_11.setText(_translate("Serial", "Period:"))
        self.label_12.setText(_translate("Serial", "ms"))
        self.checkBox_HexSend.setText(_translate("Serial", "HEX send"))
        self.checkBox_End.setText(_translate("Serial", "Add Newline"))
        self.label_send.setText(_translate("Serial", "send："))
        self.label_receive.setText(_translate("Serial", "rece："))