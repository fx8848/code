#encoding=utf-8
#!/usr/bin/python
import os
import thread

threads_number = 60
similar_ids = []
des_img_name = 'dest.gif2.jpg'

def checkSimilar(destPath, id_img):
	returnstr = os.popen("findimagedupes %s %s" % (des_img_name, destPath)).readlines()  
	if len(returnstr)>0:
		mylock.acquire()
		similar_ids.append(id_img)
		mylock.release()
	else:
		mylock.acquire()
		similar_ids.append(-1)
		mylock.release()
	#print returnstr

#多线程同步锁
mylock = thread.allocate_lock()
for i in range(0, threads_number):
	filename = "%i.jpg" % (i)
	thread.start_new_thread(checkSimilar, (filename,i))
while True:
	if len(similar_ids) == threads_number:
		break
print ','.join([str(s) for s in similar_ids if s!=-1])
