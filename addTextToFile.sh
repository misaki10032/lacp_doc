#!/bin/bash

# 保存记录到md文件
now_push_time=$(date "+%Y-%m-%d %H:%M:%S")
newMD_log="【${now_push_time}】-【调用接口：/api/news/list/top10】- 微博热搜爬取成功，推送10条致QQ群【DONE】"
echo -e $newMD_log
sed -i "${newMD_log}\n -- cxy \n" ./tbpc.md
