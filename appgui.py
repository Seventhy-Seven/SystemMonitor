from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 335)
        MainWindow.setMinimumSize(0, 335)
        MainWindow.setMaximumSize(500, 335)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("#RamProgressBar {\n"
"    text-align: center;\n"
"}\n"
                                 
"#RamProgressBar::chunk {\n"
"    background-color: #3498db;\n"
"}\n"
                                 
"#CpuProgressBar {\n"
"    text-align: center;\n"
"}\n"
                                 
"#CpuProgressBar::chunk {\n"
"    background-color: #2ecc71;\n"
"}\n"
                                 
"#DiskProgressBar {\n"
"    text-align: center;\n"
"}\n"
                                 
"#DiskProgressBar::chunk {\n"
"   background-color: #c2ff5f;\n"
"}\n"
                                 
"QProgressBar\n"
"{\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"color: black;\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"border-radius :0px;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 497, 251))
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.SysInfo = QtWidgets.QWidget()
        self.SysInfo.setObjectName("SysInfo")
        self.layoutWidget = QtWidgets.QWidget(self.SysInfo)
        self.layoutWidget.setGeometry(QtCore.QRect(2, 0, 491, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.host = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.host.sizePolicy().hasHeightForWidth())
        self.host.setSizePolicy(sizePolicy)
        self.host.setMinimumSize(QtCore.QSize(301, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.host.setFont(font)
        self.host.setObjectName("host")
        self.verticalLayout_3.addWidget(self.host)
        self.pltf = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pltf.sizePolicy().hasHeightForWidth())
        self.pltf.setSizePolicy(sizePolicy)
        self.pltf.setMinimumSize(QtCore.QSize(301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pltf.setFont(font)
        self.pltf.setObjectName("pltf")
        self.verticalLayout_3.addWidget(self.pltf)
        self.pltf_ver = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pltf_ver.sizePolicy().hasHeightForWidth())
        self.pltf_ver.setSizePolicy(sizePolicy)
        self.pltf_ver.setMinimumSize(QtCore.QSize(301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pltf_ver.setFont(font)
        self.pltf_ver.setObjectName("pltf_ver")
        self.verticalLayout_3.addWidget(self.pltf_ver)
        self.typeSys = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeSys.sizePolicy().hasHeightForWidth())
        self.typeSys.setSizePolicy(sizePolicy)
        self.typeSys.setMinimumSize(QtCore.QSize(301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.typeSys.setFont(font)
        self.typeSys.setObjectName("typeSys")
        self.verticalLayout_3.addWidget(self.typeSys)
        self.tabWidget.addTab(self.SysInfo, "")
        self.CPU = QtWidgets.QWidget()
        self.CPU.setObjectName("CPU")
        self.CpuProgressBar = QtWidgets.QProgressBar(self.CPU)
        self.CpuProgressBar.setEnabled(True)
        self.CpuProgressBar.setGeometry(QtCore.QRect(100, 110, 200, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CpuProgressBar.sizePolicy().hasHeightForWidth())
        self.CpuProgressBar.setSizePolicy(sizePolicy)
        self.CpuProgressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.CpuProgressBar.setMaximumSize(QtCore.QSize(600, 31))
        self.CpuProgressBar.setProperty("value", 50)
        self.CpuProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.CpuProgressBar.setTextVisible(True)
        self.CpuProgressBar.setObjectName("CpuProgressBar")
        self.label_2 = QtWidgets.QLabel(self.CPU)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 51, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(90, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cpu_model = QtWidgets.QLabel(self.CPU)
        self.cpu_model.setGeometry(QtCore.QRect(60, 10, 420, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpu_model.sizePolicy().hasHeightForWidth())
        self.cpu_model.setSizePolicy(sizePolicy)
        self.cpu_model.setMinimumSize(QtCore.QSize(0, 0))
        self.cpu_model.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.cpu_model.setFont(font)
        self.cpu_model.setObjectName("cpu_model")
        self.cores = QtWidgets.QLabel(self.CPU)
        self.cores.setGeometry(QtCore.QRect(100, 60, 20, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cores.sizePolicy().hasHeightForWidth())
        self.cores.setSizePolicy(sizePolicy)
        self.cores.setMinimumSize(QtCore.QSize(0, 0))
        self.cores.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cores.setFont(font)
        self.cores.setObjectName("cores")
        self.label_3 = QtWidgets.QLabel(self.CPU)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 90, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(90, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.CPU)
        self.label_5.setGeometry(QtCore.QRect(140, 60, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.threads = QtWidgets.QLabel(self.CPU)
        self.threads.setGeometry(QtCore.QRect(250, 60, 20, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threads.sizePolicy().hasHeightForWidth())
        self.threads.setSizePolicy(sizePolicy)
        self.threads.setMinimumSize(QtCore.QSize(0, 0))
        self.threads.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.threads.setFont(font)
        self.label_6 = QtWidgets.QLabel(self.CPU)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 90, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(90, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.CPU)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.cpu_temperature = QtWidgets.QLabel(self.CPU)
        self.cpu_temperature.setGeometry(QtCore.QRect(155, 160, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpu_temperature.sizePolicy().hasHeightForWidth())
        self.cpu_temperature.setSizePolicy(sizePolicy)
        self.cpu_temperature.setMinimumSize(QtCore.QSize(0, 0))
        self.cpu_temperature.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cpu_temperature.setFont(font)
        self.cpu_temperature.setObjectName("cpu_temperature")
        self.tabWidget.addTab(self.CPU, "")
        self.RAM = QtWidgets.QWidget()
        self.RAM.setObjectName("RAM")
        self.RamProgressBar = QtWidgets.QProgressBar(self.RAM)
        self.RamProgressBar.setGeometry(QtCore.QRect(100, 80, 200, 31))
        self.RamProgressBar.setStyleSheet("selection-background-color: yellow")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RamProgressBar.sizePolicy().hasHeightForWidth())
        self.RamProgressBar.setSizePolicy(sizePolicy)
        self.RamProgressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.RamProgressBar.setMaximumSize(QtCore.QSize(500, 31))
        self.RamProgressBar.setProperty("value", 50)
        self.RamProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.RamProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.RamProgressBar.setObjectName("RamProgressBar")
        self.label_8 = QtWidgets.QLabel(self.RAM)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 90, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_8.setMaximumSize(QtCore.QSize(90, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.ram_info = QtWidgets.QLabel(self.RAM)
        self.ram_info.setGeometry(QtCore.QRect(10, 110, 490, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ram_info.sizePolicy().hasHeightForWidth())
        self.ram_info.setSizePolicy(sizePolicy)
        self.ram_info.setMinimumSize(QtCore.QSize(0, 0))
        self.ram_info.setMaximumSize(QtCore.QSize(490, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ram_info.setFont(font)
        self.ram_info.setObjectName("ram_info")
        self.ram_info_2 = QtWidgets.QLabel(self.RAM)
        self.ram_info_2.setGeometry(QtCore.QRect(10, 20, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ram_info_2.sizePolicy().hasHeightForWidth())
        self.ram_info_2.setSizePolicy(sizePolicy)
        self.ram_info_2.setMinimumSize(QtCore.QSize(0, 0))
        self.ram_info_2.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ram_info_2.setFont(font)
        self.ram_info_2.setObjectName("ram_info_2")
        self.label_9 = QtWidgets.QLabel(self.RAM)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setMaximumSize(QtCore.QSize(502, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.ram_volume = QtWidgets.QLabel(self.RAM)
        self.ram_volume.setGeometry(QtCore.QRect(115, 20, 51, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ram_volume.sizePolicy().hasHeightForWidth())
        self.ram_volume.setSizePolicy(sizePolicy)
        self.ram_volume.setMinimumSize(QtCore.QSize(0, 0))
        self.ram_volume.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ram_volume.setFont(font)
        self.ram_volume.setObjectName("ram_volume")
        self.type_memo = QtWidgets.QLabel(self.RAM)
        self.type_memo.setGeometry(QtCore.QRect(120, 10, 51, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_memo.sizePolicy().hasHeightForWidth())
        self.type_memo.setSizePolicy(sizePolicy)
        self.type_memo.setMinimumSize(QtCore.QSize(0, 0))
        self.type_memo.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.type_memo.setFont(font)
        self.type_memo.setObjectName("type_memo")
        self.tabWidget.addTab(self.RAM, "")
        self.Disk = QtWidgets.QWidget()
        self.Disk.setObjectName("Disk")
        self.diskinfo = QtWidgets.QLabel(self.Disk)
        self.diskinfo.setGeometry(QtCore.QRect(10, 80, 461, 115))
        self.diskinfo.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.diskinfo.setFont(font)
        self.diskinfo.setObjectName("diskinfo")
        self.DiskProgressBar = QtWidgets.QProgressBar(self.Disk)
        self.DiskProgressBar.setGeometry(QtCore.QRect(10, 50, 200, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DiskProgressBar.sizePolicy().hasHeightForWidth())
        self.DiskProgressBar.setSizePolicy(sizePolicy)
        self.DiskProgressBar.setMinimumSize(QtCore.QSize(0, 31))
        self.DiskProgressBar.setMaximumSize(QtCore.QSize(461, 31))
        self.DiskProgressBar.setProperty("value", 43)
        self.DiskProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.DiskProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.DiskProgressBar.setObjectName("DiskProgressBar")
        self.label_4 = QtWidgets.QLabel(self.Disk)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(self.Disk)
        self.label_10.setGeometry(QtCore.QRect(270, 10, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.disk_temp = QtWidgets.QLabel(self.Disk)
        self.disk_temp.setGeometry(QtCore.QRect(380, 10, 51, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disk_temp.sizePolicy().hasHeightForWidth())
        self.disk_temp.setSizePolicy(sizePolicy)
        self.disk_temp.setMinimumSize(QtCore.QSize(0, 0))
        self.disk_temp.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.disk_temp.setFont(font)
        self.disk_temp.setObjectName("disk_temp")
        self.tabWidget.addTab(self.Disk, "")
        self.Net = QtWidgets.QWidget()
        self.Net.setObjectName("Net")
        self.ip = QtWidgets.QLabel(self.Net)
        self.ip.setGeometry(QtCore.QRect(10, 10, 400, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ip.sizePolicy().hasHeightForWidth())
        self.ip.setSizePolicy(sizePolicy)
        self.ip.setMinimumSize(QtCore.QSize(0, 0))
        self.ip.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ip.setFont(font)
        self.ip.setObjectName("ip")
        self.mac = QtWidgets.QLabel(self.Net)
        self.mac.setGeometry(QtCore.QRect(10, 60, 400, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mac.sizePolicy().hasHeightForWidth())
        self.mac.setSizePolicy(sizePolicy)
        self.mac.setMinimumSize(QtCore.QSize(301, 31))
        self.mac.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mac.setFont(font)
        self.mac.setObjectName("mac")
        self.sub_mask = QtWidgets.QLabel(self.Net)
        self.sub_mask.setGeometry(QtCore.QRect(10, 110, 400, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sub_mask.sizePolicy().hasHeightForWidth())
        self.sub_mask.setSizePolicy(sizePolicy)
        self.sub_mask.setMinimumSize(QtCore.QSize(301, 31))
        self.sub_mask.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sub_mask.setFont(font)
        self.sub_mask.setObjectName("sub_mask")
        self.gateway = QtWidgets.QLabel(self.Net)
        self.gateway.setGeometry(QtCore.QRect(10, 160, 400, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gateway.sizePolicy().hasHeightForWidth())
        self.gateway.setSizePolicy(sizePolicy)
        self.gateway.setMinimumSize(QtCore.QSize(301, 31))
        self.gateway.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.gateway.setFont(font)
        self.gateway.setObjectName("gateway")
        self.tabWidget.addTab(self.Net, "")
        self.DateTime = QtWidgets.QLabel(self.centralwidget)
        self.DateTime.setGeometry(QtCore.QRect(120, 270, 189, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.DateTime.setFont(font)
        self.DateTime.setObjectName("DateTime")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 496, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionAbout)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SystemMonitor"))
        self.host.setText(_translate("MainWindow", "Hostname:"))
        self.pltf.setText(_translate("MainWindow", "Platform:"))
        self.pltf_ver.setText(_translate("MainWindow", "Platform-version:"))
        self.typeSys.setText(_translate("MainWindow", "Type of system:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SysInfo), _translate("MainWindow", "System information"))
        self.label_2.setText(_translate("MainWindow", "Model:"))
        self.label_3.setText(_translate("MainWindow", "CPU Cores:"))
        self.label_6.setText(_translate("MainWindow", "CPU Usage:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CPU), _translate("MainWindow", "CPU"))
        self.label_8.setText(_translate("MainWindow", "RAM Usage:"))
        self.ram_info.setText(_translate("MainWindow", "Available Memory:\n"
"Used Memory:"))
        self.ram_info_2.setText(_translate("MainWindow", "RAM Volume: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RAM), _translate("MainWindow", "RAM"))
        self.label_4.setText(_translate("MainWindow", "System Disk (C): "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Disk), _translate("MainWindow", "Disk"))
        self.ip.setText(_translate("MainWindow", "IP-Address:"))
        self.mac.setText(_translate("MainWindow", "Mac-address:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Net), _translate("MainWindow", "Net_Info"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())