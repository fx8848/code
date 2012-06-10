#! /bin/bash
baseurl='http://test.m41s.com:7979/apps/quickhand/'
phpsessid='PHPSESSID=4a4054b8c980f05625807b6984e962f1'

jsonreturn=`curl -b "${phpsessid}" -d "rank=2" ${baseurl}creategame.php`  #创建游戏
gid=`echo "import json
print json.loads('${jsonreturn}')['gid']" | python`  #根据返回得到gid
echo $gid
curl -b "${phpsessid}" -o getimage.jpg ${baseurl}getimage.php?gid=${gid}  #下载大图

jsonreturn=`curl -b "${phpsessid}" -d "gid=${gid}" ${baseurl}start.php`  #创建游戏
cardimg=`echo "import json
print json.loads('${jsonreturn}')['card']" | python`  #目标选项的图片 
echo $cardimg
curl -b "${phpsessid}" -o dest.gif ${cardimg}  #下载目标图

#下面进行处理，识别目标所在的序号
bigImagePath="getimage.jpg"
destImagePath="dest.gif"

python ./cropBigImage.py $bigImagePath
python ./cropDestImage.py $destImagePath
result=''
return=`findimagedupes *.jpg | grep dest.gif2.jpg|grep -o -E "/[0-9]+".jpg|grep -o -E [0-9]+`   #相似匹配
#echo $return
for id in $return; do
	#return_str=`findimagedupes ${id}.jpg dest.gif2.jpg`
	#if [ "${return_str}" != "" ]; then
		result=${result}${id}","
	#fi
done
result=`echo ${result:0:-1}`
echo $result

isok=` curl -b "${phpsessid}" -d "gid=${gid}&pos=${result}" ${baseurl}checkchoose.php`  #提交结果
echo $isok
