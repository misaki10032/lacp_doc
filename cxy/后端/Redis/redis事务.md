[toc]

# redis事务

mysql: ACID原则 原子性,隔离性,一致性,持久性

redis: **一个事务的所有命令会被序列化,事务执行过程中,会按照顺序执行**

> 一次性、顺序性、排他性

==Redis事务没有隔离级别的概念==

所有命令在事务中，没有直接执行，只有发起执行才会执行

==单条命令有原子性 , 事务没有原子性==

> 操作

`multi` ==开启事务==

`exec`==执行事务==

`discard`==取消事务==

```bash
127.0.0.1:6379> multi
OK
127.0.0.1:6379(TX)> set k1 v1
QUEUED
127.0.0.1:6379(TX)> set k2 v2 
QUEUED
127.0.0.1:6379(TX)> get k2
QUEUED
127.0.0.1:6379(TX)> exec
1) OK
2) OK
3) "v2"
127.0.0.1:6379> 
```

> 错误的命令 , 代码有问题,所有的命令都不会被执行

```bash
127.0.0.1:6379> multi
OK
127.0.0.1:6379(TX)> set k1 v1
QUEUED
127.0.0.1:6379(TX)> set k2 v2
QUEUED
127.0.0.1:6379(TX)> getset k3
(error) ERR wrong number of arguments for 'getset' command
127.0.0.1:6379(TX)> set k4 v4
QUEUED
127.0.0.1:6379(TX)> exec
(error) EXECABORT Transaction discarded because of previous errors.
```

> 运行时异常, 语法没有问题,但是报错了,其他的会被执行

```bash
127.0.0.1:6379> multi
OK
127.0.0.1:6379(TX)> incr k1
QUEUED
127.0.0.1:6379(TX)> set k2 v2 
QUEUED
127.0.0.1:6379(TX)> set k3 v3
QUEUED
127.0.0.1:6379(TX)> get k3
QUEUED
127.0.0.1:6379(TX)> exec
1) (error) ERR value is not an integer or out of range
2) OK
3) OK
4) "v3"
```

# 悲观锁和乐观锁

悲观锁:

- 认为什么时候都会出现问题,不论做什么都加锁

乐观锁:

- 认为不会有问题, 不上锁,更新数据的时候判断一下,在此期间是否有人修改这个数据
- 获取version
- 判断version

`watch`==监控==

`unwatch`==解锁==

> 如果被watch的值被另一个线程修改,则事务不会提交成功

> 线程1

```bash
127.0.0.1:6379> watch money
OK
127.0.0.1:6379> multi
OK
127.0.0.1:6379(TX)> decrby money 20
QUEUED
127.0.0.1:6379(TX)> exec
(nil)
```

> 线程2

```bash
127.0.0.1:6379> set money 1000
OK
127.0.0.1:6379> 
```

**如果获取失败,获取最新值就好**

