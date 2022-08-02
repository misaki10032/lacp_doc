[toc]

# 安装出现的问题

> sudo apt-get update 更新报错
>
> ![image-20211010151925092](.\image-20211010151925092.png)

1.提示没有某个公钥,加上即可

```shell
sudo gpg --keyserver keyserver.ubuntu.com --recv 7EA0A9C3F273FCD8

##公钥和报错信息种提示的公钥一样
```

```shell
sudo gpg --export --armor 7EA0A9C3F273FCD8 | sudo apt-key add -

##公钥和报错信息种提示的公钥一样
```

2.之后按照官网的例子安装

# 安装Docker

**卸载旧版本**

```shell
sudo apt-get remove docker docker-engine docker.io containerd runc
```

**更新`apt`包索引并安装包以允许`apt`通过 HTTPS 使用存储库**

```shell
 sudo apt-get update
 
 sudo apt-get install \ 
 	apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

**添加Docker官方的GPG密钥**

```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

**设置稳定的储存库**

```shell
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

**安装Docker引擎**

```shell
sudo apt-get update
 
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

**运行`hello-world`映像验证Docker Engine是否正确安装**

```shell
 sudo docker run hello-world
```

> 使用docker version确认安装成功

```bash
root@fcm-stu:~# docker version
Client: Docker Engine - Community
 Version:           20.10.9
 API version:       1.41
 Go version:        go1.16.8
 Git commit:        c2ea9bc
 Built:             Mon Oct  4 16:08:29 2021
 OS/Arch:           linux/amd64
 Context:           default
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          20.10.9
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.16.8
  Git commit:       79ea9d3
  Built:            Mon Oct  4 16:06:37 2021
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.4.11
  GitCommit:        5b46e404f6b9f661a205e28d59c982d3634148f8
 runc:
  Version:          1.0.2
  GitCommit:        v1.0.2-0-g52b36a2
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0

```

# 查看Docker镜像

```shell
sudo docker images
```

![image-20211010155205889](.\image-20211010155205889.png)