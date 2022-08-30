# author:jerry wong
# date:2022 08 14 14:14
import threading
from time import sleep

from PyQt6.QtCore import pyqtSignal, QObject, QIODeviceBase
from PyQt6.QtSerialPort import QSerialPort


class Serial_Qthread(QObject):
    signal_serialstart_function = pyqtSignal()
    # 按下按钮触发的信号
    signal_pushButton_open = pyqtSignal(object)
    signal_pushButton_open_flage = pyqtSignal(object)

    # 收到数据的信号
    signal_readdata = pyqtSignal(object)

    # 附加的信号显示
    signal_DTR = pyqtSignal(object)
    signal_RTS = pyqtSignal(object)
    # signal_time_stamper = pyqtSignal(object)
    # 发送数据的信号
    signal_send_data = pyqtSignal(object)
    signal_send_data_length = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        print("初始化时候线程", threading.current_thread())

        # 定义状态:0未打开/ 1打开/ 2占用或错误
        self.state = 0

    def serialinit_function(self):
        sleep(1)
        print("串口线程id:", threading.current_thread())
        self.Serial = QSerialPort()
        # 串口收到数据跳到槽函数
        self.Serial.readyRead.connect(self.serial_receive_data)

    def slot_PushButton_open(self, parameter):
        print("按下按钮", parameter)
        if self.state == 0:
            # 设置参数
            self.Serial.setPortName(parameter["comboBox_Com"])
            self.Serial.setBaudRate(int(parameter["comboBox_Baud"]))

            if parameter["comboBox_Stop"] == "1.5":
                self.Serial.setStopBits(3)
            else:
                # self.Serial.setStopBits())
                self.Serial.setStopBits(QSerialPort.StopBits(int(parameter["comboBox_Stop"])))

            self.Serial.setDataBits(QSerialPort.DataBits(int(parameter["comboBox_Data"])))

            setParity = 0
            if parameter["comboBox_Check"] == 'None':
                setParity = 0
            elif parameter["comboBox_Check"] == 'Odd':
                setParity = 3
            else:
                setParity = 2

            self.Serial.setParity(QSerialPort.Parity(setParity))

            if self.Serial.open(QIODeviceBase.OpenModeFlag.ReadWrite) == True:
                print("打开串口成功")
                self.state = 1
                self.signal_pushButton_open_flage.emit(self.state)
            else:
                print("打开串口失败")
                self.signal_pushButton_open_flage.emit(0)
        else:
            print("串口关闭")
            self.state = 0
            self.Serial.close()
            self.signal_pushButton_open_flage.emit(2)

    def serial_receive_data(self):
        # print("接收数据的线程id:", threading.current_thread())
        self.signal_readdata.emit(self.Serial.readAll())

    def slot_send_data(self, send_data):
        # 串口要先打开
        if self.state != 1:
            return
            # print('发送数据',send_data)
        if send_data['Hex'] == 2:
            # 转为字符串才能发送
            send_list = []
            send_text = send_data['data']
            while send_text != '':
                try:
                    num = int(send_text[0:2], 16)
                except:
                    return
                send_text = send_text[2:].strip()
                send_list.append(num)
            input_s = bytes(send_list)
            self.Serial.write(input_s)
        else:
            # 转为二进制才能发送
            byte_data = str.encode(send_data['data'])
            self.Serial.write(byte_data)

    def slot_DTR(self, state):
        print("DTR", state)
        if state == 2:
            self.Serial.setDataTerminalReady(True)
        else:
            self.Serial.setDataTerminalReady(False)

    def slot_RTS(self, state):
        print("RTS", state)
        if state == 2:
            self.Serial.setRequestToSend(True)
        else:
            self.Serial.setRequestToSend(False)
    #
    # def slot_TimeStamper(self,state):
    #     print("TimeStamper",state)
