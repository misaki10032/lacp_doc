#!/bin/bash

# 保存记录到md文件
now_push_time=$(date "+%Y-%m-%d %H:%M:%S")
newMD_log="【${now_push_time}】-【调用接口：/api/news/list/top10】- 微博热搜爬取成功，推送10条致QQ群【DONE】"
echo -e $newMD_log
sed -i "N;2a ${newMD_log} \n" ./tbpc.md

# 下载后续脚本必须的python包
pip install lxml
pip install json
pip install datetime
