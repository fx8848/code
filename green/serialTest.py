# encoding=utf-8

import serial
import binascii
from struct import unpack

ser = serial.Serial(0)
ser.baudrate = 19200
ser.write('unlogall\r\n')
ser.write('log bestposb ontime 1\r\n')
ser.write('log trackstatb ontime 1\r\n')
ser.write('log gpgga ontime 2\r\n')
ser.write('log gpgsv ontime 1\r\n')
line = ''
while True:
	line += ser.readline()
	print line
	asscii_header = binascii.unhexlify('AA4412')  #AA4412的字符串形式
	msg_sum = line.count(asscii_header)
	if line.find(asscii_header) != -1:
		print '\033[0;31m 共有%s条二进制数据  \033[0m ' % msg_sum
	while True:
		i = line.find(asscii_header)
		if i==-1: break
		if len(line)<28:
			print '长度不够，退出'
			#raw_input('press any key to continue')
			break   #文件头长度都不够，则等待下次数据，连接在一起再一起解析
		header_len_hex = binascii.hexlify(line[i+3]).upper()
		header_len = int(header_len_hex, 16) #文件头长度
		msg_len_hex = binascii.hexlify(line[i+8].upper())
		msg_len = int(msg_len_hex, 16) #消息内容长度			
		print "文件头长度：%s，消息内容长度：%s" % (header_len, msg_len)
		if len(line)<i+msg_len+header_len+4: 
			print '长度不够，退出'
			#raw_input('press any key to continue')
			break
		msg_id_hex = binascii.hexlify(line[i+4]).upper()
		msg_id = int(msg_id_hex,16)
		print "消息ID：%s" % msg_id  #id=83为trackstat   id=42为bestpos
		line1 = line[0:i]
		line2 = line[i:i+header_len+msg_len]
		line3 = line2[i+header_len+msg_len:]
		line2_hex = binascii.hexlify(line2)
		#print 'line1:'+binascii.hexlify( line1)+'\033[0;31m'+ 'line2:'+'\033[0m'+line2_hex+'line3:'+binascii.hexlify( line3)
		if msg_id == 83:  #分析trackstat数据
			msg_start = i+header_len
			L2_str = line[msg_start+36: msg_start+40]
			L2_hex = binascii.hexlify(L2_str).upper()
			L2 = int(L2_hex,16)
			print '\033[0;31m '+ 'L2值:%s' % L2+ '\033[0m'
		elif msg_id == 42:  #分析bestpos数据
			msg_start = i+header_len
			lat_str = line[msg_start+8:msg_start+16]
			lat_hex = binascii.hexlify(lat_str)
			lat_double = unpack('d', lat_str)

			lon_str = line[msg_start+16:msg_start+24]
			lon_double = unpack('d',lon_str)
			print '\033[0;31m'+ '经度：%s 纬度：%s' %(lon_double, lat_double)+'\033[0m'
			#raw_input(lat_str)
		line = line[i+header_len+msg_len+4:]
		#print "left line:"+ binascii.hexlify(line)  #剩下的0d0a表示\r\n的意思
		#raw_input('press any key to continue...')
	#print line
