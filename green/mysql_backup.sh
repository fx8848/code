#!/bin/sh

DBUser=root

DBPass=yxdb123

DBHost=`hostname -s`

# make sure you already created the backup directory

BackupPath=/var/bak/mysql

# the path of mysqld
DBbinPath=/usr/opt/local/mysql-5.1.47/bin/mysqldump

# error record log file
ErrorLog=${BackupPath}/error.txt

if ${DBbinPath} -u${DBUser} -p${DBPass} --opt --default-character-set=utf8 --extended-insert=false --triggers -R --hex-blob --all-databases --flush-logs --delete-master-logs --delete-master-logs > ${BackupPath}"/"${DBHost}"-"`date "+%Y-%m-%d"`".sql" ;
then
     find ${BackupPath}"/" -mtime +6 -exec rm {} \;
else
     echo "-------------------" >> ${ErrorLog}
     echo `date "+%Y-%m-%d"` >> ${ErrorLog}
     echo "-------------------\n" >> ${ErrorLog}

     exit
fi
