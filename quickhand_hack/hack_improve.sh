#! /bin/bash
baseurl='http://app.moxian.com/apps/quickhand/system/'
username=810492306@qq.com
userpwd=`echo -n 810492306|md5sum|cut -d ' ' -f1`
phpsessid=`grep  -o "PHPSESSID=.\{32\}" cookies.txt`

jsonreturn=`curl -b "${phpsessid}" -d "rank=2" ${baseurl}creategame.php`  #创建游戏
if echo $jsonreturn|grep "system" ;then  #没有登陆
	curl -d "__userlable__=${username}&__pwd__=${userpwd}&type=login&keeplogin=off&u=&code=" -D cookies.txt http://moxian.com/login/gatway.php
	phpsessid=`grep  -o "PHPSESSID=.\{32\}" cookies.txt`
	jsonreturn=`curl -b "${phpsessid}" -d "rank=2" ${baseurl}creategame.php`  #创建游戏
fi

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

result=`python getresult.py`
echo "匹配结果："$result

isok=` curl -b "${phpsessid}" -d "gid=${gid}&pos=${result}" ${baseurl}checkchoose.php`  #提交结果
echo -e "\033[1;31;40m提交结果返回：\033[0m"$isok
