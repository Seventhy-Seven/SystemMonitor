from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from appgui import Ui_MainWindow
from datetime import datetime
import psutil
import threading
import time
import sys
import platform,socket,re,uuid,cpuinfo

class MEM(QThread,Ui_MainWindow):

    x = pyqtSignal(int)

    def run(self):
        try:
            while True:
                value = psutil.virtual_memory().percent
                self.x.emit(int(value))
                time.sleep(1)

        except:
            self.statusBar.showMessage("Error in getting Ram informations")
class PROC(QThread,Ui_MainWindow):

    y = pyqtSignal(int)

    def run(self):
        try:
            while True:
                value = psutil.cpu_percent()
                self.y.emit(int(value))
                time.sleep(1)
        except:
            self.statusBar.showMessage("Error in getting Cpu informations")
class DISK(QThread,Ui_MainWindow):

    z = pyqtSignal(int)

    def run(self):
        try:
            while True:
                obj_Disk = psutil.disk_usage('/')
                self.z.emit(int(obj_Disk.percent))
                time.sleep(1)
        except:
            self.statusBar.showMessage("Error in getting disk informations")

#main class
class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.setSysinfo()
        self.StartThread()
        self.actionAbout.triggered.connect(self.about)
        self.actionExit.triggered.connect(self.exit)
        th = threading.Thread(target=self.setStatsInfo)
        th.setDaemon(True)
        th.start()


    def setSysinfo(self):
        try:
            self.pltf.setText(self.pltf.text()+" "+platform.system() +" "+ platform.release())
            self.pltf_ver.setText(self.pltf_ver.text()+" "+platform.version())
            
            self.ram_volume.setText(self.ram_volume.text()+" "+str(round(psutil.virtual_memory().total / (1024.0 **3)))+" Gb")
            self.host.setText(self.host.text()+" "+socket.gethostname())
            self.ip.setText(self.ip.text()+" "+socket.gethostbyname(socket.gethostname()))
            self.mac.setText(self.mac.text()+" "+':'.join(re.findall('..', '%012x' % uuid.getnode())))
            
            self.cpu_model.setText(self.cpu_model.text()+" " + cpuinfo.get_cpu_info()['brand_raw'])
            bit = platform.architecture()
            self.typeSys.setText(self.typeSys.text()+" " + bit[0] )
            self.cores.setText(self.cores.text()+" "+str(psutil.cpu_count()))
            current_date = datetime.now().date()
            self.DateTime.setText(str(current_date))
        except:
            self.statusBar.showMessage("Error in getting System informations")
    def StartThread(self):
        self.ram_obj = MEM()
        self.cpu_obj = PROC()
        self.disk_obj = DISK()

        self.ram_obj.x.connect(self.setRam)
        self.cpu_obj.y.connect(self.setCpu)
        self.disk_obj.z.connect(self.setDisk)
        self.ram_obj.start()
        self.cpu_obj.start()
        self.disk_obj.start()

    def setStatsInfo(self):
        try:
            while True:
                obj_Disk = psutil.disk_usage('/')
                self.ram_info.setText("\nAvailable Memory :"+str(round(psutil.virtual_memory().available/(1024.0**3),2)) + "Gb"+"\n\n"+"Used Memory :"+str(round(psutil.virtual_memory().used/(1024.0**3),2)) + "Gb")
                self.diskinfo.setText("\ntotal Disk  :"+ str(round(obj_Disk.total / (1024.0 ** 3),2))+"Gb\n\nused Disk  :"+str(round(obj_Disk.used / (1024.0 ** 3),2)) + "Gb\n\nfree Disk  :"+ str(round(obj_Disk.free / (1024.0 ** 3),2)) + "Gb" )
                
                time.sleep(1)
        except:
            self.statusBar.showMessage("Error in getting additional information about ram and cpu")

    
    def setRam(self, value):
        self.RamProgressBar.setValue(value)
    def setCpu(self, value):
        self.CpuProgressBar.setValue(value)
    def setDisk(self,value):
        self.DiskProgressBar.setValue(value)

    def about(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("SystemMonitor:\nVersion:1.0")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    def exit(self):
        QtWidgets.QApplication.quit()

app = QtWidgets.QApplication(sys.argv)
win = MyWindow()
sys.exit(app.exec_())