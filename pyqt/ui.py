import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
import requests as rq


class RequestThread(QThread):
    # 自己定义信号槽
    sinOut = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        # 延时
        QThread.sleep(5)
        body = rq.get("https://www.baidu.com")
        result = body.text
        self.sinOut.emit(result)


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi()

        self.time_timer = QtCore.QTimer(self)
        # 设置定时器周期时间
        self.time_timer.setInterval(1000)
        self.count_int: int = 0

        self.start_btn.clicked.connect(self.timer_start_click)
        self.end_btn.clicked.connect(self.timer_stop_click)

        self.time_timer.timeout.connect(self.time_count)

        self.rq_thread = RequestThread()
        # 绑定自定义的槽事件
        self.rq_thread.sinOut.connect(self.thread_result_rec)

        self.thread_btn.clicked.connect(self.thread_start_clicked)

        self.show()

    def thread_start_clicked(self):
        self.rq_thread.start()


    def thread_result_rec(self, result: str):
        self.result_edit.setText(result)

    def timer_start_click(self):
        self.time_timer.start()

    def timer_stop_click(self):
        self.time_timer.stop()

    def time_count(self):
        self.count_int += 1
        self.timer_label.setText(str(self.count_int))

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(519, 572)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.timer_label = QtWidgets.QLabel(self.centralwidget)
        self.timer_label.setGeometry(QtCore.QRect(20, 90, 71, 51))
        self.timer_label.setObjectName("timer_label")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(170, 60, 113, 32))
        self.start_btn.setObjectName("start_btn")
        self.end_btn = QtWidgets.QPushButton(self.centralwidget)
        self.end_btn.setGeometry(QtCore.QRect(170, 130, 113, 32))
        self.end_btn.setObjectName("end_btn")
        self.result_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.result_edit.setGeometry(QtCore.QRect(20, 270, 331, 221))
        self.result_edit.setObjectName("result_edit")
        self.thread_btn = QtWidgets.QPushButton(self.centralwidget)
        self.thread_btn.setGeometry(QtCore.QRect(380, 270, 113, 32))
        self.thread_btn.setObjectName("thread_btn")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 519, 24))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.timer_label.setText(_translate("MainWindow", "计时器"))
        self.start_btn.setText(_translate("MainWindow", "开始"))
        self.end_btn.setText(_translate("MainWindow", "停止"))
        self.thread_btn.setText(_translate("MainWindow", "线程获取数据"))


if __name__ == "__main__":
    Qapp = QApplication(sys.argv)
    UI = Ui_MainWindow()
    sys.exit(Qapp.exec_())
