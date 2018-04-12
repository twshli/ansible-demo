#!/bin/bash

SpringBoot=spring-boot-demo.jar

boot_id=`ps -ef |grep java|grep $SpringBoot|grep -v grep|awk '{print $2}'`
count=`ps -ef |grep java|grep $SpringBoot|grep -v grep|wc -l`

if [ $count != 0 ];then
    kill -9 $boot_id
fi

setsid java -jar ~/apps/$SpringBoot

exit 0
