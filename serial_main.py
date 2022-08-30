# author:jerry wong
# date:2022 08 14 13:39

import sys
import time

from PyQt6.QtCore import QThread, QTimer
from PyQt6.QtGui import QIcon, QColor, QTextCursor
from PyQt6.QtSerialPort import QSerialPortInfo

import serial_ui
import PyQt6.QtWidgets as qw
import threading
import serial_thread
from serial_thread import Serial_Qthread


class SerialForm(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.port_name = []
        # 哟用于累加接收到的数据
        self.receivelength = 0
        self.sendlength = 0

        # 初始化界面：可以写在main中
        self.ui = serial_ui.Ui_Serial()
        self.ui.setupUi(self)

        # print("主线程id", threading.current_thread())
        self.interface_init()
        self.Ui_Init()

        # 创建线程
        ## (1)创建新线程
        self.serial_QThread = QThread()
        ## (2)创建对象
        self.serial_QThread_function = Serial_Qthread()
        ## (3)对象移动到线程中
        self.serial_QThread_function.moveToThread(self.serial_QThread)
        self.serial_QThread.start()

        # 触发线程的信号
        self.serial_QThread_function.signal_serialstart_function.connect(
            self.serial_QThread_function.serialinit_function)
        self.serial_QThread_function.signal_serialstart_function.emit()

        # 按下开始按钮
        self.serial_QThread_function.signal_pushButton_open.connect(self.serial_QThread_function.slot_PushButton_open)
        self.serial_QThread_function.signal_pushButton_open_flage.connect(self.slot_PushButton_open_flage)


        # 新建定时器扫描端口
        self.time_scan = QTimer()
        self.time_scan.timeout.connect(self.TimeOut_Scan)
        self.time_scan.start(1000)


        self.serial_QThread_function.signal_readdata.connect(self.slot_readdata)

        # 链接附加功能
        self.serial_QThread_function.signal_RTS.connect(self.serial_QThread_function.slot_RTS)
        self.serial_QThread_function.signal_DTR.connect(self.serial_QThread_function.slot_DTR)
        # self.serial_QThread_function.signal_time_stamper.connect(self.serial_QThread_function.slot_TimeStamper)
        self.serial_QThread_function.signal_send_data.connect(self.serial_QThread_function.slot_send_data)
        # # 定时发送的定时器
        # self.time_send = QTimer()
        # self.time_send.timeout.connect(self.TimeOut_Send)


    def interface_init(self):
        self.baud = ('4800', '9600', '57600', '115200')
        self.stop = ('1', '1.5', '2')
        self.data = ('8', '7', '6', '5')
        self.check = ('None', 'Odd', 'Even')
        self.ui.comboBox_Baud.addItems(self.baud)
        self.ui.comboBox_Stop.addItems(self.stop)
        self.ui.comboBox_Data.addItems(self.data)
        self.ui.comboBox_Check.addItems(self.check)

        # 接收
        self.ui.checkBox_RTS.stateChanged.connect(self.slot_CheckBox_RTS)
        self.ui.checkBox_DTR.stateChanged.connect(self.slot_CheckBox_DTR)
        # self.ui.checkBox_TimeStamp.stateChanged.connect(self.slot_CheckBox_TimeStamper)

        # 发送
        self.ui.checkBox_HexSend.stateChanged.connect(self.slot_CheckBox_hexsend)

        self.ui.pushButton_Send.clicked.connect(self.slot_PushButton_send)
        # self.ui.pushButton_CleanSend.clicked.connect(self.slot_PushButton_cleansend)
        # self.ui.pushButton_ReceiveClean.clicked.connect(self.slot_PushButton_receiveclean)

        # self.ui.checkBox_TimeStamp.stateChanged.connect(self.checkBox_TimeSend)
        # self.ui.lineEdit_IntervalTime.setText("10")
    def Ui_Init(self):
        self.ui.pushButton_Open.clicked.connect(self.pushButton_open)

    def pushButton_open(self):
        self.set_parameter = {}
        self.set_parameter["comboBox_Com"] = self.ui.comboBox_Com.currentText()
        self.set_parameter["comboBox_Check"] = self.ui.comboBox_Check.currentText()
        self.set_parameter["comboBox_Data"] = self.ui.comboBox_Data.currentText()
        self.set_parameter["comboBox_Stop"] = self.ui.comboBox_Stop.currentText()
        self.set_parameter["comboBox_Baud"] = self.ui.comboBox_Baud.currentText()
        self.serial_QThread_function.signal_pushButton_open.emit(self.set_parameter)

    def slot_PushButton_open_flage(self, state):
        print("串口的状态", state)
        if state == 0:
            qw.QMessageBox.warning(self, '错误信息', '串口已被占用，打开失败')
        elif state == 1:
            self.ui.pushButton_Open.setStyleSheet("color:red")
            self.ui.pushButton_Open.setText("关闭串口")
            self.time_scan.stop()
        else:
            self.ui.pushButton_Open.setStyleSheet("color:black")
            self.ui.pushButton_Open.setText("打开串口")
            self.time_scan.start(1000)

    def TimeOut_Scan(self):
        availablePort = QSerialPortInfo.availablePorts()
        new_port = []
        # print(availablePort)  # 输出的是COM口对象
        for port in availablePort:
            new_port.append(port.portName())  # 把COM口显示出来

        # 如果不相等，就把新的加进UI
        if len(self.port_name) != len(new_port):
            self.port_name = new_port
            self.ui.comboBox_Com.clear()
            self.ui.comboBox_Com.addItems(self.port_name)

    def slot_readdata(self, data):
        # self.receivelength = self.receivelength + len(data)
        # self.ui.label_receive.setText("接收:" + str(self.receivelength))

        # print("byte之前",data)
        # print("byte之前类型",type(data))
        if self.ui.checkBox_TimeStamp.checkState() == self.ui.checkBox_TimeStamp.checkState().Checked:
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "\r\n"
            self.ui.textEdit_receive.setTextColor(QColor(255, 100, 100))
            self.ui.textEdit_receive.insertPlainText(time_str)
            self.ui.textEdit_receive.setTextColor(QColor(0, 0, 0))
        byte_data = bytes(data)
        # print("byte之后",byte_data)
        # print("byte之后type",type(byte_data))
        if self.ui.checkBox_Hexview.checkState() == self.ui.checkBox_Hexview.checkState().Checked:
            # print("Hex show")
            view_data = ''
            for i in range(0, len(byte_data)):
                view_data = view_data + '{:02x}'.format(byte_data[i]) + ' '
            self.ui.textEdit_receive.insertPlainText(view_data)
            self.ui.textEdit_receive.insertPlainText("\r\n")
        else:
            self.ui.textEdit_receive.insertPlainText(byte_data.decode('utf-8', 'ignore'))

            self.ui.textEdit_receive.insertPlainText("\r\n")

    # 接收
    def slot_CheckBox_RTS(self, state):
        print("RTS", state)   # 勾选变为2，不勾选为0
        self.serial_QThread_function.signal_RTS.emit(state)

    def slot_CheckBox_DTR(self, state):
        print("DTR", state)
        self.serial_QThread_function.signal_DTR.emit(state)

    # 发送
    # def TimeOut_Send(self):
    #     print("定时时间到")
    #

    #
    #
    def slot_CheckBox_hexsend(self, state):
        print("16进制发送", state)
        if state == 2:
            # 当前字符转为16进制
            send_text = self.ui.textEdit_Send.toPlainText()
            # print(type(send_text))   # str类型

            byte_text = str.encode(send_text)
            view_data = ''
            for i in range(0, len(byte_text)):
                view_data = view_data + '{:02x}'.format(byte_text[i]) + ' '
            self.ui.textEdit_Send.setText(view_data)

        else:
            send_list = []
            send_text = self.ui.textEdit_Send.toPlainText()
            while send_text != "":
                try:
                    # 转16进制
                    num = int(send_text[0:2],16)
                except:
                    qw.QMessageBox.warning(self,"错误信息","请正确输入16进制")
                # 同时完成递减
                send_text = send_text[2:].strip()
                send_list.append(num)
            # list直接转为字符串
            input_s = bytes(send_list)
            self.ui.textEdit_Send.setText(input_s.decode())


    def slot_PushButton_send(self):
        print("点击发送按钮")
        send_data = {}
        if self.ui.checkBox_End.checkState()== self.ui.checkBox_End.checkState().Checked:
            send_data['data'] = self.ui.textEdit_Send.toPlainText() + '\r\n'

        else:
            send_data['data'] = self.ui.textEdit_Send.toPlainText()
        send_data['Hex'] = self.ui.checkBox_HexSend.checkState()
        self.serial_QThread_function.signal_send_data.emit(send_data)

    # self.ui.textEdit_Send.setText(send_list)
    # def slot_CheckBox_TimeStamper(self,state):
    #     print("Time Stamper",state)
    #     self.serial_QThread_function.signal_time_stamper.emit(state)
    #


    def checkBox_TimeSend(self, state):
        print("点击定时器")
        if state == 2:
            time_data = self.ui.lineEdit_IntervalTime.text()
            self.time_send.start(int(time_data))
        else:
            self.time_send.stop()
    #
    # def slot_PushButton_cleansend(self):
    #     self.sendlength = 0
    #     self.ui.label_send.setText("Send:0")
    #     self.ui.textEdit_Send.clear()
    #
    # def slot_PushButton_receiveclean(self):
    #     self.receivelength = 0
    #     self.ui.label_receive.setText("Rece:0")
    #     self.ui.label_send.setText("Send:0")
    #     self.ui.textEdit_receive.clear()
    #
    # def slot_send_data_length(self,length):
    #     self.sendlength += length
    #     self.ui.label_send.setText("Send"+str(length))
if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    app.setWindowIcon(QIcon('adell.ico'))
    w = SerialForm()
    w.show()
    sys.exit(app.exec())
