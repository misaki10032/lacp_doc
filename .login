termHelp=`figlet -t -l Hello , LACP Term`
termHelp=${termHelp}"\n输入help查看命令帮助"
termHelp=${termHelp}"\n输入help+\`命令\`查看某些命令"
wl=`fortune | sed '/^$/d'`
termHelp=${termHelp}"\n${wl}"

echo "${termHelp}" | lolcat
