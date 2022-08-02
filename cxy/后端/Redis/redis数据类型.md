[toc]

# 问题解决

> 在使用flushdb删除redis数据的时候发生错误

```bash
(error) MISCONF Redis is configured to save RDB snapshots, but it is currently not able to persist on disk. Commands that may modify the data set are disabled, because this instance is configured to report errors during writes if RDB snapshotting fails (stop-writes-on-bgsave-error option). Please check the Redis logs for details about the RDB error.
```

==解决方案==

```bash
#连接redis后运行　
#config set stop-writes-on-bgsave-error no　命令
#关闭配置项stop-writes-on-bgsave-error解决该问题。
127.0.0.1:6379> config set stop-writes-on-bgsave-error no
OK
127.0.0.1:6379> keys *
1) "key:__rand_int__"
2) "name"
127.0.0.1:6379> flushdb
OK
127.0.0.1:6379> 
```



# Redis-Key

```bash
#获取全部的key
keys * 
#设置key value
set age 1
#查看是否有这个名字
exists name
#移动对应的name到 [database]数据库
move name 1
#设置过期时间
set name blank
expire name [秒]
#获取剩余多少秒
ttl name
#查看当前key的类型
type name
```

# 五大数据类型

## String

### 字符串一般命令

查看当前db中的key `keys *`

设置键值对 `set key value`

获取对应键的值 `get key`

判断是否有对应键 `exists key`

向当前键的值中添加一段字符串 `append key 'hello'` ==如果当前值不存在,则相当于==`set key`

> 结果展示

```bash
127.0.0.1:6379> keys *
(empty array)
127.0.0.1:6379> flushall
OK
127.0.0.1:6379> set key1 v1
OK
127.0.0.1:6379> get key1
"v1"
127.0.0.1:6379> exists key1
(integer) 1
127.0.0.1:6379> append key1 'hello'
(integer) 7
127.0.0.1:6379> get key1
"v1hello"
127.0.0.1:6379> 
```

### 字符串进阶

> 数字自动加减

自增1 `incr key`

自减1 `decr key`

增加某个值 `incrby key 10`

减小某个值 `decrby key 4`

```bash
127.0.0.1:6379> set views 0
OK
127.0.0.1:6379> get views
"0"
127.0.0.1:6379> incr views
(integer) 1
127.0.0.1:6379> get views
"1"
127.0.0.1:6379> decr views
(integer) 0
127.0.0.1:6379> get views
"0"
127.0.0.1:6379> incrby views 10
(integer) 10
127.0.0.1:6379> get views
"10"
127.0.0.1:6379> decrby views 4
(integer) 6
127.0.0.1:6379> get views
"6"
```

> 字符串截取

`getrange key [start] [end]` ==闭区间==

```bash
127.0.0.1:6379> get key1
"v1hello,blank,zhangsan"
127.0.0.1:6379> getrange key1 0 5
"v1hell"
127.0.0.1:6379> getrange key1 0 -1
"v1hello,blank,zhangsan"
```

`setrange key [offect] ['替换成的']`==从offect开始替换成==

```bash
127.0.0.1:6379> set ss abcde
OK
127.0.0.1:6379> get ss
"abcde"
127.0.0.1:6379> setrange ss 1 xx
(integer) 5
127.0.0.1:6379> get ss
"axxde"
```

> 设置过期时间

`setex key time`

```bash
127.0.0.1:6379> setex ssc 30 '???'
OK
127.0.0.1:6379> get ssc
"???"
127.0.0.1:6379> ttl ssc
(integer) 23
```

`setnx if not exist`

```bash
127.0.0.1:6379> set ssc hello
OK
127.0.0.1:6379> get ssc
"hello"
127.0.0.1:6379> setnx ssc redis
(integer) 0
127.0.0.1:6379> get ssc
"hello"
127.0.0.1:
```

> 批量设置和获取

`mset [可变长度参数]`

`mget [可变长度参数]`

```bash
127.0.0.1:6379> mset k1 v1 k2 v2 k3 v3
OK
127.0.0.1:6379> keys *
1) "k3"
2) "k2"
3) "k1"
127.0.0.1:6379> mget k1 k2 k3
1) "v1"
2) "v2"
3) "v3"
```

`msetnx [可变长度参数]` ==如果某个key已经存在,则这整个语句都不会被执行==

```bash
127.0.0.1:6379> msetnx k1 v2 k4 v4
(integer) 0
127.0.0.1:6379> keys *
1) "k3"
2) "k2"
3) "k1"
```

> 设置对象

- 使用json格式保存对象

```bash
127.0.0.1:6379> set user:1 {name:blank,age:3}
OK
127.0.0.1:6379> get user:1
"{name:blank,age:3}"
```

- 变换设计方式

```bash
127.0.0.1:6379> mset user:2:name zhangsan user:2:age 2
OK
127.0.0.1:6379> mget user:2:name user:2:age
1) "zhangsan"
2) "2"
```

> 组合命令

`getset key value`

```bash
127.0.0.1:6379> getset db mysql
(nil)
127.0.0.1:6379> get db
"mysql"
127.0.0.1:6379> getset db redis
"mysql"
127.0.0.1:6379> get db
"redis"
```

## List

> list命令都是以l开头,基本指令

`lpush 列表名 值` 模类似左插入,左读取==

```bash
127.0.0.1:6379> lpush list1 one
(integer) 1
127.0.0.1:6379> lpush list1 two
(integer) 2
127.0.0.1:6379> lpush list1 three
(integer) 3
127.0.0.1:6379> lrange list1 0 -1
1) "three"
2) "two"
3) "one"
```

`rpush 列表名 值` 模拟队列==类似右插入,左读取==

```bash
127.0.0.1:6379> rpush list2 one
(integer) 1
127.0.0.1:6379> rpush list2 two
(integer) 2
127.0.0.1:6379> rpush list2 three
(integer) 3
127.0.0.1:6379> lrange list2 0 -1
1) "one"
2) "two"
3) "three"
```

`lpop` ==左弹出值==`rpop`==右弹出==

```bash
127.0.0.1:6379> lpop list1
"three"
127.0.0.1:6379> lrange list1 0 -1
1) "two"
2) "one"
127.0.0.1:6379> rpop list1 
"one"
127.0.0.1:6379> lrange list1 0 -1
1) "two"
```

`lrem key count value`==移除指定的值==

```bash
127.0.0.1:6379> lrange list2 0 -1
1) "one"
2) "two"
3) "three"
4) "one"
127.0.0.1:6379> lrem list2 2 one 
(integer) 2
127.0.0.1:6379> lrange list2 0 -1
1) "two"
2) "three"
127.0.0.1:6379> lpush list2 one
(integer) 3
127.0.0.1:6379> lpush list2 one
(integer) 4
127.0.0.1:6379> lrem list2 1 one
(integer) 1
127.0.0.1:6379> lrange list2 0 -1
1) "one"
2) "two"
3) "three"
```

`lindex list [index]` ==获取对应下标的值==

```bash
127.0.0.1:6379> lrange list2 0 -1
1) "one"
2) "two"
3) "three"
127.0.0.1:6379>  lindex list2 0
"one"
127.0.0.1:6379>  lindex list2 1
"two"
127.0.0.1:6379>  lindex list2 2
"three"
```

`llen key` ==获取列表长度==

```bash
127.0.0.1:6379> llen list2
(integer) 3
```

`ltrim list start stop`==截取指定的位置==

```bash
127.0.0.1:6379> rpush list n n n y y y n n n 
(integer) 9
127.0.0.1:6379> lrange list 0 -1
1) "n"
2) "n"
3) "n"
4) "y"
5) "y"
6) "y"
7) "n"
8) "n"
9) "n"
127.0.0.1:6379> ltrim list 3 3
OK
127.0.0.1:6379> lrange list 0 -1
1) "y"
127.0.0.1:6379> rpush list n n n y y y n n n 
(integer) 10
127.0.0.1:6379> lrange list 0 -1
 1) "y"
 2) "n"
 3) "n"
 4) "n"
 5) "y"
 6) "y"
 7) "y"
 8) "n"
 9) "n"
10) "n"
127.0.0.1:6379> ltrim list 4 6 
OK
127.0.0.1:6379> lrange list 0 -1
1) "y"
2) "y"
3) "y"
127.0.0.1:6379> 
```

`rpoplpush` ==移除最后一个元素,添加到别的中==

```bash
127.0.0.1:6379> lrange list 0 -1
1) "y"
2) "y"
3) "y"
127.0.0.1:6379> rpoplpush list other 
"y"
127.0.0.1:6379> lrange list 0 -1
1) "y"
2) "y"
127.0.0.1:6379> lrange other 0 -1
1) "y"
```

`lset list 0 item`==下标替换元素==

**不存在会报错**

```bash
127.0.0.1:6379> lset list 0 item
(error) ERR no such key
127.0.0.1:6379> rpush list 0 1 2 3 4 5 6
(integer) 7
127.0.0.1:6379> lrange list 0 -1
1) "0"
2) "1"
3) "2"
4) "3"
5) "4"
6) "5"
7) "6"
127.0.0.1:6379> lset list 0 99
OK
127.0.0.1:6379> lrange list 0 -1
1) "99"
2) "1"
3) "2"
4) "3"
5) "4"
6) "5"
7) "6"
```

`linsert list [befor|after] [指定的字符串][插入的值]`

```bash
127.0.0.1:6379> lrange list 0 -1
1) "99"
2) "1"
3) "2"
4) "3"
5) "4"
6) "5"
7) "6"
127.0.0.1:6379> linsert list before 99 --
(integer) 8
127.0.0.1:6379> lrange list 0 -1
1) "--"
2) "99"
3) "1"
4) "2"
5) "3"
6) "4"
7) "5"
8) "6"
127.0.0.1:6379> linsert list after 99 ==
(integer) 9
127.0.0.1:6379> lrange list 0 -1
1) "--"
2) "99"
3) "=="
4) "1"
5) "2"
6) "3"
7) "4"
8) "5"
9) "6"
```

> list特点

- 是一个链表,brfore node after ,左右都可以添加删除
- 如果key不存在则会创建一个
- 存在则添加
- 当所有值都被移除以后,则key也不存在
- 可以实现双端队列,列表,栈,队列,消息队列

## Set

**无序,不可重复**

> 基本指令 (一般以s开头)

`sadd set value`==添加==

`smembers key` ==查看值==

`sismember key value` ==查看key中是否有value值==

`scard key`==获取key中的元素个数==

```bash
127.0.0.1:6379> sadd myset blank
(integer) 1
127.0.0.1:6379> sadd myset blank1 blank2
(integer) 2
127.0.0.1:6379> smembers myset
1) "blank"
2) "blank1"
3) "blank2"
127.0.0.1:6379> sismember myset blank
(integer) 1
127.0.0.1:6379> sismember myset blank3
(integer) 0
127.0.0.1:6379> scard myset
(integer) 3
```

`srem key value`==移除指定元素==

```bash
127.0.0.1:6379> srem myset blank
(integer) 1
127.0.0.1:6379> smembers myset
1) "blank1"
2) "blank2"
```

`srandmember key`==随机抽选一个元素==

```bash
127.0.0.1:6379> smembers myset
1) "blank1"
2) "blank2"
127.0.0.1:6379> srandmember myset
"blank2"
127.0.0.1:6379> srandmember myset
"blank1"
127.0.0.1:6379> srandmember myset
"blank1"
```

`spop key` ==随机弹出一个幸运儿==

```bash
127.0.0.1:6379> spop myset
"5"
127.0.0.1:6379> smembers myset
 1) "3"
 2) "1"
 3) "2"
 4) "blank1"
 5) "9"
 6) "8"
 7) "6"
 8) "blank2"
 9) "7"
10) "4"
```

`smove key 目标key 值`==把指定值移动到另一个set中==

```bash
127.0.0.1:6379> smove myset myset2 blank1
(integer) 1
127.0.0.1:6379> smove myset myset2 blank2
(integer) 1
127.0.0.1:6379> smembers myset
1) "3"
2) "1"
3) "2"
4) "9"
5) "8"
6) "6"
7) "7"
8) "4"
127.0.0.1:6379> smembers myset2
1) "blank1"
2) "blank2"
```

`sdiff key1 key2`==差集==

`sunion key1 key2`==并集==

`sinter key1 key2`==交集==

```bash
127.0.0.1:6379> sadd k1 a b c d
(integer) 4
127.0.0.1:6379> sadd k2 c d e f
(integer) 4
127.0.0.1:6379> sdiff k1 k2
1) "b"
2) "a"
127.0.0.1:6379> sunion k1 k2
1) "b"
2) "a"
3) "e"
4) "d"
5) "c"
6) "f"
127.0.0.1:6379> sinter k1 k2
1) "d"
2) "c"
```

## Hash

**类似一个map集合**

> key :<key,value> 以H开头

`hset key field2 v1 field2 v2...`==设置hash表==

`hget key field`==获取指定的key的值==

`hmget key field1 field2....` ==获取多个指定的值==

`hgetall key`==获取全部的值==

```bash
127.0.0.1:6379> hset myhash k1 v1 k2 v2
(integer) 2
127.0.0.1:6379> hget myhash k1
"v1"
127.0.0.1:6379> hget myhash k2
"v2"
127.0.0.1:6379> hmget myhash k1 k2
1) "v1"
2) "v2"
127.0.0.1:6379> hgetall myhash
1) "k1"
2) "v1"
3) "k2"
4) "v2"
```

`hdel key field`==删除key ,对应的value也没了==

`hlen key`==获取有几个hash值==

```bash
127.0.0.1:6379> hdel myhash k1
(integer) 1
127.0.0.1:6379> hgetall myhash
1) "k2"
2) "v2"
127.0.0.1:6379> hset myhash k3 v3 k4 v4
(integer) 2
127.0.0.1:6379> hgetall myhash
1) "k2"
2) "v2"
3) "k3"
4) "v3"
5) "k4"
6) "v4"
127.0.0.1:6379> hlen myhash
(integer) 3

```

`hexists key field`==获取指定的field是否存在==

```bash
127.0.0.1:6379> hexists myhash k2
(integer) 1
127.0.0.1:6379> hexists myhash k1
(integer) 0
127.0.0.1:6379> hexists myhash k3
(integer) 1
```

`hkeys key`==获取全部field==

`hvals key`==获取全部val==

`hincrby key field 1`==自增指定增量==

`hsetnx key filed value`==不存在插入==

```bash
127.0.0.1:6379> hset myhash k1 1 k2 2 k3 3 k4 4
(integer) 4
127.0.0.1:6379> hkeys myhash
1) "k1"
2) "k2"
3) "k3"
4) "k4"
127.0.0.1:6379> hvals myhash
1) "1"
2) "2"
3) "3"
4) "4"
127.0.0.1:6379> hincrby myhash k1 5
(integer) 6
127.0.0.1:6379> hvals myhash
1) "6"
2) "2"
3) "3"
4) "4"
127.0.0.1:6379> hsetnx myhash k1 1
(integer) 0
```

> 存个对象

```bash
127.0.0.1:6379> hset user:1 name blank age 18 sex man
(integer) 3
127.0.0.1:6379> keys *
1) "user:1"
2) "myhash"
127.0.0.1:6379> hget user:1 name
"blank"
127.0.0.1:6379> hget user:1 ahe
(nil)
127.0.0.1:6379> hget user:1 age
"18"
```

## Zset

**有序集合**

> 命令

`zadd`==增加==

`zrange`==查看==

`zrangebyscore key -inf +inf`==从负无穷到正无穷==

`zrevrange key 0 -1` ==逆序排序== 

**可以选择 `(`来表示开区间**

```bash
127.0.0.1:6379> zadd myset 1 one 2 two 3 three
(integer) 3
127.0.0.1:6379> zrange myset 0 -1
1) "one"
2) "two"
3) "three"
127.0.0.1:6379> zadd salary 5000 blank 1500 xiaohong 3000 zhangsan
(integer) 3
127.0.0.1:6379> zrangebyscore salary -inf +inf
1) "xiaohong"
2) "zhangsan"
3) "blank"
127.0.0.1:6379> zrangebyscore salary -inf +inf withscores 
1) "xiaohong"
2) "1500"
3) "zhangsan"
4) "3000"
5) "blank"
6) "5000"
127.0.0.1:6379> zrevrange salary 0 -1
1) "blank"
2) "zhangsan"
3) "xiaohong"
127.0.0.1:6379> zrangebyscore salary -inf +inf
1) "xiaohong"
2) "zhangsan"
3) "blank"
```

`zrem key value`==移除==

```bash
127.0.0.1:6379> zrem salary xiaohong
(integer) 1
127.0.0.1:6379> zrange salary 0 -1
1) "zhangsan"
2) "blank"
```

`zcount key start end`==后去指定区间的成员数量==

```bash
127.0.0.1:6379> zrange salary 0 -1
1) "zhangsan"
2) "blank"
127.0.0.1:6379> zcount salary 0 -1
(integer) 0
127.0.0.1:6379> zcount salary 0 1
(integer) 0
127.0.0.1:6379> zcount salary 500 10000
(integer) 2
```



# 三大特殊类型

## geospatial

**地理位置**

`geoadd`==添加==   ==南北极无法添加,一般直接导入==  ==写入的数据必须符合 **经度** **纬度**==

`geodist`==获取距离==

`geopos` ==获取指定城市的经纬度==

`georadius`==以给定的经纬度为中心找出元素==

`georadiusbymember`==以给定的城市为中心找出元素==

`gephash`==返回11个hash长度==

`zrange key 0 -1` ==基本类型都能用,查看元素==



```bash
127.0.0.1:6379> geoadd china:city 116.40 39.90 beijing 121.47 31.23 shanghai 106.50 29.53 chongqing
(integer) 3
127.0.0.1:6379> geoadd china:city 114.05 22.52 shenzhen 120.16 30.24 hangzhou 108.96 34.26 xian
(integer) 3
############################################################################################################
127.0.0.1:6379> geopos china:city chongqing
1) 1) "106.49999767541885376"
   2) "29.52999957900659211"
127.0.0.1:6379> geopos china:city beijing
1) 1) "116.39999896287918091"
   2) "39.90000009167092543"
############################################################################################################  
127.0.0.1:6379> geodist china:city beijing xian
"910056.5237"   
############################################################################################################  
127.0.0.1:6379> georadius china:city 110 30 100 km
(empty array)
127.0.0.1:6379> georadius china:city 110 30 1000 km
1) "chongqing"
2) "xian"
3) "shenzhen"
4) "hangzhou"
127.0.0.1:6379> georadius china:city 110 30 1000 km withcoord
1) 1) "chongqing"
   2) 1) "106.49999767541885376"
      2) "29.52999957900659211"
2) 1) "xian"
   2) 1) "108.96000176668167114"
      2) "34.25999964418929977"
3) 1) "shenzhen"
   2) 1) "114.04999762773513794"
      2) "22.5200000879503861"
4) 1) "hangzhou"
   2) 1) "120.1600000262260437"
      2) "30.2400003229490224"
```

## Hyperloglog

> 基数--->不重复的元素

Redis 的基数统计算法

网页UV(一个人访问一个网站多次 , 但是还是算作一个人)

传统方式 : set保存用户id,然后统计set中的元素作为判断

Hyperloglog : 统计基数 , 0.81%的错误率;但是只占用12k内存

> 操作

`pfadd`==添加数量==

`pfcount`==统计基数==

`pfmerge key [key1] [key2]`==将两个个key合并为新的==

```bash
127.0.0.1:6379> pfadd pf1 a b c h m j k k
(integer) 1
127.0.0.1:6379> pfadd pf2 j i u y h ju g b n m g h
(integer) 1
127.0.0.1:6379> pfcount pf1
(integer) 7
127.0.0.1:6379> pfcount pf2
(integer) 10
127.0.0.1:6379> pfmerge onepf pf1 pf2
OK
127.0.0.1:6379> pfcount onepf
(integer) 13
```

## Bitmaps

> 位存储

统计用户信息,登录,打卡...... (某个状态)

bitmaps位图,只有0 1 两个状态

> 测试

`setbit key value [状态]`==设置状态==

`getbit` ==获得状态==

`bitcount`==统计状态为1==

```bash
127.0.0.1:6379> setbit daka 0 1
(integer) 0
127.0.0.1:6379> setbit daka 1 1
(integer) 0
127.0.0.1:6379> setbit daka 2 1
(integer) 0
127.0.0.1:6379> setbit daka 3 0
(integer) 0
127.0.0.1:6379> setbit daka 4 1
(integer) 0
127.0.0.1:6379> setbit daka 5 1
(integer) 0
127.0.0.1:6379> setbit daka 6 0
(integer) 0
127.0.0.1:6379> getbit daka 6
(integer) 0
127.0.0.1:6379> getbit daka 2
(integer) 1
127.0.0.1:6379> bitcount daka
(integer) 5
```

















