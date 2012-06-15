#! /bin/bash
baseurl='http://app.moxian.com/apps/quickhand/system/'
phpsessid='PHPSESSID=a687a6b3f4e600e2a8bba6917268ca87'

jsonreturn=`curl -b "${phpsessid}" -d "rank=2" ${baseurl}creategame.php`  #创建游戏
jsonreturn=`echo $jsonreturn`
echo "创建游戏返回："$jsonreturn
gid=`echo ${jsonreturn}|grep -o "[0-9]\{4\}"`
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
result=`echo ${result:0:-1}`
echo "匹配结果："$result

isok=` curl -b "${phpsessid}" -d "gid=${gid}&pos=${result}" ${baseurl}checkchoose.php`  #提交结果
echo -e "\033[1;31;40m提交结果返回：\033[0m"$isok
