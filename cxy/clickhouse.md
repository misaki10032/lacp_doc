

[toc]

## docker 部署clickhouse

### 下载docker镜像

```dockerfile
# 下载clickhouse服务端
docker pull yandex/clickhouse-server
# 下载连接服务端
docker pull yandex/clickhouse-client
```

### 启动服务端

#### 直接启动

```shell
➜  ~ docker run -it --rm --link some-clickhouse-server:clickhouse-server yandex/clickhouse-client --host clickhouse-server
```

#### 使用主机系统存储卷

```shell
# 创建目录
➜  ~ mkdir $HOME/some_clickhouse_database
# 启动服务器容器
➜  ~ docker run -d \
> --name clickserver \
> --ulimit nofile=262144:262144 \
> --volume=$HOME/clickhouse_database:/var/lib/clickhouse \
> -p 9000:9000 \
> -p 9004:9004 \
> yandex/clickhouse-server
```

### 启动客户端

```shell
➜  ~ docker run -it --rm --link some-clickhouse-server:clickhouse-server yandex/clickhouse-client --host clickhouse-server
```

**或者**

```shell
➜  ~ docker exec -it clickserver clickhouse-client
```

### 检测是否启动成功

- 查询1

```shell
➜  ~ docker exec -it clickserver clickhouse-client
<jemalloc>: MADV_DONTNEED does not work (memset will be used instead)
<jemalloc>: (This is the expected behaviour if you are running under QEMU)
ClickHouse client version 22.1.3.7 (official build).
Connecting to localhost:9000 as user default.
Connected to ClickHouse server version 22.1.3 revision 54455.

bb6c7a987c08 :) select 1

SELECT 1

Query id: 045897d4-e4da-40a8-a1a0-5d9136069e83

┌─ 1─┐
│  1  │
└───┘

1 rows in set. Elapsed: 0.028 sec. 

```

- 访问9000端口

```http
http://localhost:9000/

Port 9000 is for clickhouse-client program
You must use port 8123 for HTTP.

http://localhost:8123/
```

![image-20220520101951237](flink.assets/image-20220520101951237.png)

- 使用mysql客户端链接

```mysql
➜  ~ mysql --protocol tcp -u default -P 9004
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 0
Server version: 22.1.3.7-ClickHouse 

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| name               |
+--------------------+
| INFORMATION_SCHEMA |
| default            |
| information_schema |
| system             |
+--------------------+
4 rows in set (0.05 sec)
Read 4 rows, 543.00 B in 0.034942083 sec., 114 rows/sec., 15.18 KiB/sec.

mysql> 
```

