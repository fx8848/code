# encoding=utf-8
import bluetooth
import os

print "开始搜索..."
nearby_devices = bluetooth.discover_devices(lookup_names=True)
print "共发现 %d 个设备" % len(nearby_devices)
for addr,name in nearby_devices:
	#if name == "zhd_0832166":
		print "尝试连接设备： %s - %s" % (addr,name)
		sockfd = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
		try:
			sockfd.connect((addr,1))  
			sockfd.send('unlogall\r\n')
			sockfd.send('log gpgga ontime 1\r\n')
			sockfd.send('log gpgsv ontime 3\r\n')
			sockfd.send('log gpgsa ontime 1\r\n')
			sockfd.send('log bestposb ontime 1\r\n')
			sockfd.send('log trackstatb ontime 2\r\n')
			sockfd.send('log gpgst ontime 1\r\n')
			sockfd.send('log gprmc ontime 1\r\n')

			output = open('logdata.bin', 'w+')
			while True:
				data = sockfd.recv(1024)  #每次接收1KB的数据
				output.write(data)
				print data
		except:
			print "操作失败鸟..."
		#finally:
			#sockfd.close()
			#output.close()
