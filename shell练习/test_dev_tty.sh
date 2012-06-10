#!/bin/bash

printf "Enter new password:"
stty -echo #关闭打印输入的字符
read password </dev/tty
printf "\nEnter again:"
read password2 </dev/tty 
printf "\n"
stty echo  #不要忘记了开启
echo "password=" $password
echo "password2="$password2
echo "all done"
