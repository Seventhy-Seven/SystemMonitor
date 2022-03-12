import psutil
import time
import socket
import getmac
import cpuinfo

print()
print ('RAM:\n ')
print("RAM percent :",psutil.virtual_memory().percent,"%")
print("Total Memory :",psutil.virtual_memory().total/1024,'Gb')
print("Available Memory :",psutil.virtual_memory().available/1024,'Gb')
print("Used Memory :",psutil.virtual_memory().used/1024,'Gb\n')

print('CPU:\n ')
print('CPU model: ', cpuinfo.get_cpu_info()['brand_raw'])
print('Total number of CPUs :',psutil.cpu_count())
print("CPU usage ", abs(psutil.cpu_percent()),'%\n')

print ('DISK:\n')
obj_Disk = psutil.disk_usage('/')
print ("total Disk  :",obj_Disk.total / (1024.0 ** 3))
print ("used Disk  :",obj_Disk.used / (1024.0 ** 3))
print ("free Disk  :",obj_Disk.free / (1024.0 ** 3))
print (obj_Disk.percent,"%\n")

print('NET:\n')
print("hostname: ", socket.gethostname())
print("ip-adress :", socket.gethostbyname(socket.gethostname()))
print("mac-adress :", getmac.get_mac_address())
print("duplication of ip to ipv6 version :", socket.has_dualstack_ipv6())



