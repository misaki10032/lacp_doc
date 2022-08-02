[toc]

# Redis.conf

> 网络

```bash
bind 127.0.0.1 ::1 #绑定ip
Protected-mode yes #保护模式
port 6379       #端口号
```

> 通用GENERAL

```bash
daemonized yes #以守护进程模式运行,默认no,开启yes为后台运行
pidfile /var/run/redis_6379.pid #后台模式运行需要配置一个pid
loglevel notice 
logfile "" #日志文件位置
databases 16 #数据库数量,默认16个
always-show-logo yes #是否总是显示logo
```

> 快照

在规定的时间执行了多少操作,会生成文件.rdb 或.aof

redis是内存数据库,没有持久化数据就会断电消失

```bash
save 900 1   #900秒内,至少有一个key进行了修改,会进行持久化
save 300 10  #300s内,至少10key修改,持久
save 60 10000 #60s内,至少10000key修改,持久

stop-writes-on-bgsave-error yes #持久化出错,是否继续工作

rdbcompression yes #是否压缩rdb文件,会消耗cpu
rdbchecksum  #保存rdb时候进行错误校验
dir ./ #rdb文件的保存目录
```

> REPLICATION 复制





> SECURITY安全

```bash
#设置密码
config set requirepass "123456"
#获取密码
config get requirepass
#登录
auth 123456
```

> CLIENTS客户端限制

```bash
maxclients 10000 #最大客户端数量
maxmemory <byte> #redis配置最大的内存容量
maxmemory-policy noeviction #内存上限的处理策略
    1、volatile-lru：只对设置了过期时间的key进行LRU（默认值） 
    2、allkeys-lru ： 删除lru算法的key   
    3、volatile-random：随机删除即将过期key   
    4、allkeys-random：随机删除   
    5、volatile-ttl ： 删除即将过期的   
    6、noeviction ： 永不过期，返回错误
```

> APPEND ONLY模式 aof配置

```bash
appendonly no #默认不开启,默认为rdb持久化
appendfilename "appendonly.aof" #名字
appendfsync everysec #每秒执行一次sync,可能丢失
appendfsync always  #每次修改执行一次sync ,消耗性能
appendfsync no     #不执行sync,速度快
```

# Redis持久化

`面试重点`

## RDB(Redis DataBases)

![image-20210405201846102](.\image-20210405201846102.png)

> 自定义

`save 60 5` 60秒内修改5个

>触发机制

- save的规则满足定义的规则时候,会产生rdb
- 执行flushall会产生rdb文件
- 退出redis,也会产出rdb文件

> 恢复rdb文件

放在运行目录下即可

```bash
127.0.0.1:6379> config get dir #获取运行目录
1) "dir"
2) "/home/blank/\xe6\xa1\x8c\xe9\x9d\xa2"
```

> 优缺点

- 优点

```text
1.大规模数据恢复,dump.rdb效率很高
2.对数据完整性要求不高
```

- 缺点

```text
1.需要一定时间进行间隔操作,意外宕机后,删除就没了
2.fork进程的时候,会占用内存空间
```

## AOF(Append Only File)

![image-20210405201900341](.\image-20210405201900341.png)

**将所有命令都记录下来 , 恢复的时候,全部执行一遍**

> 操作

默认不开启,手动开启>`appendonly yes` 开启aof ,重启即可生效

*如果aof文件损坏,则无法启动redis*

**aof使用`redis-check-aof --fix`修复aof文件**

![image-20210405201637151](.\image-20210405201637151.png)

如果aof文件大于60m,会开启新的线程来重写文件。

> 优缺点

- 优点

```text
1.每次修改都同步,文件完整性更加好
2.每秒同步一次,可能丢失1秒数据
```

- 缺点

```text
1.aof文件大,修复速度慢
2.aof运行效率低,所以默认redis为rdb模式
```

# Redis发布订阅

> 命令

`pusbscribe` ==订阅一个或多个指定模式的频道==

`publish` ==将message发送到指定的频道==

`pubsub`

`punsubscribe`

`subscribe` ==订阅给定的一个或多个频道信息==

`unsubscribe`



redis通过`subscribe`命令可以让客户端订阅任意数量的频道,每当新消息被发送到订阅的频道时,就会显示出来

![image-20210406091751780](.\image-20210406091751780.png)

频道channel1, client2,5,1是订阅了频道的人

当有新消息通过publish命令,发送给频道channel1的时候,这个消息就会被发送给所有订阅了的发送者

![image-20210406091919207](.\image-20210406091919207.png)



接收端:

![image-20210406092643569](.\image-20210406092643569.png)

发送端:

![image-20210406092654629](.\image-20210406092654629.png)

# Redis主从复制

### 概念

主从复制就是把一台Redis服务器的数据,复制到其他阿德Redis服务器上句号,前者叫主节点,后者叫做从节点 ; ==数据复制时单向的只能由主节点到从节点==

### 作用

- 数据冗余 : 实现数据的热备份
- 故障恢复 : 当主节点发生问题的时候, 可以由从节点提供服务 , 实现快速的故障恢复
- 负载均衡 : 主从复制配合读写分离 , 由主节点提供写服务 , 从节点提供读取服务 , 分担服务器亚里 , 提高并发量
- 高可用(集群) : 是哨兵模式和集群能够实现的基础

*redis最大使用内存不应该超过20G*

### 环境配置

`info replication`

![image-20210406130758232](.\image-20210406130758232.png)

master为主机

#### *只用配置从机*

1 . `slaveof [127.0.0.1/ip] [6379/端口]`==从命令行配置==

2 . `replication配置`

- replicaof < masterip >< masterport >
- masterauth< master-password >

> 特点

- 主机可以写 , 从机不能写只能读

- 注解宕机以后 , 从机仍然可以读取 , 如果需要重新指定主机需要更改配置
- 主机重新上线以后 , 从机仍然可以读取
- 命令行配置的从机 , 在宕机后 , 重新启动 , 会变回主机

- 只要变回从机以后 , 数据会恢复
  - ==slave==启动成功连接到==master==后 , 会发送一个==sync==同步命令,==mashter==接到命令后 , 会传输整个文件到==slave== , 完成一次完全同步 . 
  - ==全量复制== : 接到数据库文件数据后 , 将其加载到内存中
  - ==增量复制== : 之后接到的新的数据 , 即为增量复制

**重新连接master后 , 一次完全同步将被自动执行**

### 主从复制的模式

#### *1 . 一主二从*

![image-20210406133030976](.\image-20210406133030976.png)

#### *2 . 层层链路*

![image-20210406133110731](.\image-20210406133110731.png)

如果主机断开了连接 , 可以使用 `slaveof no one` 让自己变成主机 , 主机修复以后 , 也只能重新配置

#### *3 . 哨兵模式*

> 自动选取master的模式

哨兵是一个进程 , 哨兵模式是一个特殊的模式 , redis提供了哨兵的命令 , 作为进程 , 独立运行 , 哨兵通过发送命令 , 灯到redis服务器响应 , 从而监控多个redis实例

##### -单哨兵模式

![image-20210406134628101](.\image-20210406134628101.png)

##### - 多哨兵模式

![image-20210406135206145](.\image-20210406135206145.png)

​		假设主机宕机 , 哨兵1检测到服务器不可用 , 但不会马上进行failover过程 , 被称为*主观下线*, 当后面的哨兵也检测到服务器不可用以后 , 哨兵之间会进行一次投票 , 投票的结果由一个哨兵发起 , 进行failover[故障转移]操作==(存在一个投票算法)==. 切换成功后 , 会通过发布订阅模式 , 让每个哨兵把自己监控的从服务器实现切换主机 , 叫做*客观下线* 

> 开启哨兵配置

使用`redis-sentinel`

```bash
#新建一个文件
vim sentinel.conf
#写入
sentinel monitor [名字.随便起] [监控ip] [监控端口6379] [1 判断客观下线的数量的临界点]
#启动哨兵
redis-sentinel bconfig/sentinel.conf
```

**当主机回来以后 , 只能重新当作从机**

> 优缺点

- 优点 :
  -  哨兵集群 , 所有的主从复制优点都有
  - 主从切换 , 故障可以转移
  - 自动转移,很方便

- 缺点 :
  - 不好在线扩容 , 扩容上线以后比较麻烦
  - 配置复杂

> 哨兵模式配置资料

```test
sentinel monitor mymaster 192.16831.193 6379 1：哨兵监视器(名为 mymaster,ip,port,1表示主机挂了 slave 会投票选举成为主机)

sentinel down-after-milliseconds mymaster 5000：主机 down 掉后经过 5s 后哨兵开始投票选举谁成为主机

sentinel failover-timeout mymaster 900000：当一个slave从一个错误的master那里同步数据的计算时间为 900s

sentinel parallel-syncs mymaster 2：指定在发生failover主备切换时最多可以有多少个slave同时对新的master进行数据同步
```

# Redis缓存穿透 , 缓存击穿和缓存雪崩

*缓存处理流程*

![image-20210406145027878](.\image-20210406145027878.png)

## 缓存穿透

> 概念

缓存穿透是指 , 用户访问不存在的数据 , 这时的用户就类似攻击者 , 不断地访问数据库会使数据库压力过大 , 缓存失去了保护的意义

> 解决

- 接口增加校验 , 过滤掉一些恶意攻击 , 和一些不合法的数据
- 存储空数据 , key-value 设置为 key-null ,但是会消耗掉一部分缓存 , 浪费了空间 , 所以可以设置空数据过期时间防止用户反复的攻击同一个数据 

## 缓存击穿

> 概念

在高并发的过程中 , 由于用户高频的访问某一个key(比如微博热搜) , 但是可能缓存过期 (也可能是其他) , 由于并发的数据非常的多 , 所以就发生了击穿现象 , 数据库压力瞬间增大

> 解决

- 设置热点数据永不过期 . 弊端:占用空间
- 加互斥锁 : 当并发数据同时请求数据库的时候 , 只允许一个线程进入 ,其他的排队等待 , 减小数据库压力 , 但是效率就会略低

## 缓存雪崩

> 概念

缓存雪崩是指 , 在缓存中的数据 , 大面积过期 , 这时候用户的所有访问就会经过数据库 , 引起数据库压力过大 , 甚至宕机

> 解决

- 缓存的数据的过期时间设置为随机的 , 防止同一时间的大面积数据过期
- 分布式系统下 , 将热点数据分布在不同的缓存中
- 设置热点数据永不过期(占空间)







