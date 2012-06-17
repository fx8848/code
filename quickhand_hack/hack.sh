#! /bin/bash
baseurl='http://app.moxian.com/apps/quickhand/system/'
curl -d "__userlable__=810492306@qq.com&__pwd__=6b7450d79ccf4d8ed189769a10d31204&type=login&keeplogin=off&u=&code=" -D cookies.txt http://moxian.com/login/gatway.php
phpsessid=`grep  -o "PHPSESSID=.\{32\}" cookies.txt`
#phpsessid='PHPSESSID=fb753d8e52cdf77104531c231f1bd8f7'

jsonreturn=`curl -b "${phpsessid}" -d "rank=2" ${baseurl}creategame.php`  #创建游戏
jsonreturn=`echo $jsonreturn`
echo "创建游戏返回："$jsonreturn
gid=`echo ${jsonreturn}|grep -o "[0-9]\{5\}"`
echo "游戏ID："$gid
curl -b "${phpsessid}" -o getimage.jpg ${baseurl}getimage.php?gid=${gid}  #下载大图

jsonreturn=`curl -b "${phpsessid}" -d "gid=${gid}" ${baseurl}start.php`  #创建游戏
echo "开始游戏返回："$jsonreturn
cardimg=`echo ${jsonreturn} | grep -o "[0-9]\{1,2\}\.gif" | grep -o "[0-9]\{1,2\}"`
cardimg=${cardimg}".jpg"
echo "目标图片："$cardimg
#curl -b "${phpsessid}" -o dest.gif ${cardimg}  #下载目标图
cp dest/${cardimg} dest.jpg

#下面进行处理，识别目标所在的序号
bigImagePath="getimage.jpg"
destImagePath="dest.gif"

python ./cropBigImage.py $bigImagePath
rm $bigImagePath
#python ./cropDestImage.py $destImagePath
result=''
return=`findimagedupes *.jpg | grep dest.jpg|grep -o -E "/[0-9]+".jpg|grep -o -E [0-9]+`   #相似匹配
for id in $return; do
	#return_str=`findimagedupes ${id}.jpg dest.gif2.jpg`
	#if [ "${return_str}" != "" ]; then
		result=${result}${id}","
	#fi
done
result=${result%,*}
echo "匹配结果："$result

isok=` curl -b "${phpsessid}" -d "gid=${gid}&pos=${result}" ${baseurl}checkchoose.php`  #提交结果
echo -e "\033[1;31;40m提交结果返回：\033[0m"$isok
