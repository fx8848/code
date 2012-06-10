a2x = [chr(i+ord('a')) for i in xrange(24)]
yz = ['y', 'z']
dest = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#dest = "map"
dest2 = ""
for d in dest:
	if d in a2x:
		d = chr(ord(d)+2)
	elif d in yz:
		d = chr(ord(d)+2-26)
	dest2 += d
print dest2
