[toc]

## 帮助命令

```shell
docker version #查看版本信息
docker info #显示docker的系统信息,更加的详细
docker --help #显示docker的命令操作
```

## 镜像命令

`docker images`==查看镜像==

| `--all` , `-a`    | 列出所有镜像         | Show all images (default hides intermediate images) |
| ----------------- | -------------------- | --------------------------------------------------- |
| `--digests`       |                      | Show digests                                        |
| `--filter` , `-f` |                      | Filter output based on conditions provided          |
| `--format`        |                      | Pretty-print images using a Go template             |
| `--no-trunc`      |                      | Don't truncate output                               |
| `--quiet` , `-q`  | **只显示镜像的ID号** | Only show image IDs                                 |

`docker search`==搜索==

![image-20211010161859775](.\image-20211010161859775.png)

```shell
docker search mysql --filter=STARS=3000 #查询STARS大于等于3000的
```

`docker pull`==下载命令==

![image-20211010161543925](.\image-20211010161543925.png)

`docker rmi -f`

```shell
docker rmi -f 容器id
docker rmi -f 容器id 容器id 容器id 容器id
docker rmi -f $(docker images -aq) #查询全部的id,并删除
```

## 容器命令

`docker run`==启动一个容器==

```shell
# 参数说明
--name="Name" 容器名字
-d 			  后台运行:
-i			  使用交互方式运行
-P		  	  容器的端口 -p 8080:8080
-p			  随机指定
```

```shell
docker run -it centos /bin/bash
```

![image-20211010163145338](.\image-20211010163145338.png)

`docker ps`==列出所有运行的容器==

`exit`==退出容器==

`Ctrl + P + Q`==退出容器不停止容器==

`docker rm -f`==强制删除容器==

`docker start 容器id`==启动容器==

`docker restart`==重启==

`docker stop`==停止==

`docker kill`==杀死==

## 常用手册

#### 通过name或者短id查询完整id

```shell
➜  ~ docker inspect -f '{{.Id}}' some-clickhouse-server
2519e74844e099dfd95e7b28d955898fbd18ce202a2ace159a7b1734d982e683
```

#### 通过完整id传输文件

```shell
# 传输对象放在前面
➜  ~ docker cp 2519e74844e099dfd95e7b28d955898fbd18ce202a2ace159a7b1734d982e683:/etc/clickhouse-server/config.xml ~   
```

