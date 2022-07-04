[toc]

# mac m1  安装hive

-   方式1`Homebrew`

```shell
➜  ~ brew install hive
```

>   我的m1 pro发生了如下错误
>
>   Error: openjdk@8: no bottle available!
>   You can try to install from source with:
>    brew install --build-from-source openjdk@8
>   Please note building from source is unsupported. You will encounter build
>   failures with some formulae. If you experience any issues please create pull
>   requests instead of asking for help on Homebrew's GitHub, Twitter or any other
>   official channels.
>
>   经过查找得知是m1芯片架构的homebrew问题，所以改用手动安装

-   方式2`手动`

    -   下载tar包

    ```shell
    # 解压
    ➜  ~ tar -zxvf xxxx.tar
    # 改个名字方便使用
    ➜  ~ mv apache-hive-3.1.2-bin hive
    ➜  ~ cd hive
    ```

    -   配置环境变量

    ```shell
    ➜  ~ vim ~/.bash_profile
    ➜  ~ export HIVE_HOME=/hive目录路径
    ➜  ~ export PATH=${PATH}:${HIVE_HOME}/bin
    # 刷新使其生效
    ➜  ~ source ~/.bash_profile
    ```

    -   修改配置文件

    ```shell
    ➜  ~ cd conf
    # 根据模板创建
    ➜  ~ cp hive-env.sh.template hive-env.sh
    # 修改HADOOP_HOME
    ➜  ~ vim hive-env.sh
    ➜  ~ HADOOP_HOME=你的HADOOP目录
    # 根据模板创建
    ➜  ~ cp hive-default.xml.template hive-site.xml
    # 修改为mysql配置好的元数据库
    ```

    -   hive-site

    ```xml
    <configuration>
      
    　　<property>
            <name>hive.metastore.local</name>
            <value>true</value>
        </property>
        <property>
            <name>javax.jdo.option.ConnectionURL</name>
            <value>jdbc:mysql://localhost:3306/metastore</value>
        </property>
     　　<!--mysql5以前的版本没有cj，com.mysql.jdbc.Driver-->
        <property>
            <name>javax.jdo.option.ConnectionDriverName</name>
            <value>com.mysql.cj.jdbc.Driver</value>
        </property>
    　　<!--mysql用户名-->
        <property>
            <name>javax.jdo.option.ConnectionUserName</name>
            <value>root</value>
        </property>
    　　<!--mysql密码-->
    　　<property>
            <name>javax.jdo.option.ConnectionPassword</name>
            <value>密码</value>
        </property>
     
    	<!-- hive用来存储不同阶段的map/reduce的执行计划的目录，同时也存储中间输出结果
    	，默认是/tmp/<user.name>/hive,可以自己创建文件夹，我们实际一般会按组区分，然后组内自建一个tmp目录存>储 -->
     
        <property>
            <name>hive.exec.local.scratchdir</name>
            <value>/tmp/hive</value>
        </property>
        <property>
            <name>hive.downloaded.resources.dir</name>
                <value>/tmp/hive</value>
        </property>
        <property>
            <name>hive.metastore.warehouse.dir</name>
            <value>/data/hive/warehouse</value>
        </property>
        <property>
            <name>hive.server2.logging.operation.log.location</name>
            <value>/tmp/hive</value>
        </property>
     
    </configuration>
    ```

    -   初始化仓库

    ```shell
    # 初始化
    ➜  ~ schematool -initSchema -dbType mysql
    # 得到以下回复
    Initialization script completed
    schemaTool completed
    ```

    -   启动metastore服务

    ```shell
    ➜  bin ./hive --service metastore &
    [1] 61217
    
    ➜  bin 2022-05-18 16:54:06: Starting Hive Metastore Server
    SLF4J: Class path contains multiple SLF4J bindings.
    SLF4J: Found binding in [jar:file:/Users/chenxinyu/app/hive/lib/log4j-slf4j-impl-2.10.0.jar!/org/slf4j/impl/StaticLoggerBinder.class]
    SLF4J: Found binding in [jar:file:/opt/homebrew/Cellar/hadoop/3.3.2/libexec/share/hadoop/common/lib/slf4j-log4j12-1.7.30.jar!/org/slf4j/impl/StaticLoggerBinder.class]
    SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
    SLF4J: Actual binding is of type [org.apache.logging.slf4j.Log4jLoggerFactory]
    hive>
    ```

    

# hive 语法

## **DDL**

### 创建数据库

```hive
create database [if not exists] <表名>
[comment <表的说明>]
[localtion <路径>]
[with dbproperties (<属性名> = <属性值>, ... )];
```

### 查询数据库

-   通配符匹配数据库

```hive
show database like 'defau*';
```

-   查看数据库详情

```hive
desc database [extended] <数据库名>;
```

-   使用数据库

```hive
use <数据库名>;
```

### 修改、删除数据库

-   修改

```hive
alter database <数据库名> set dbproperties("<属性名>" = "<值>");
-- 举例
alter database test set dbproperties("create_time" = "2019");
```

-   删除

```hive
drop database <数据库名> [cascade];
```

>   cascade：默认只能删除空数据库，加上这个以后可以删除非空数据库

### 创建表

```hive
create [external] table [if not exists] <表名>
[(列名 <数据类型> [comment <该列的备注>, ...]]
[comment <表的备注>]
[partitioned by (列名 <数据类型> [comment <列的备注>], ...)]
[clustered by (列名1, 列名2, ...) [sorted by (列名 [asc|desc], ...)] into <分桶数量> buckets]
[row format <字段切分格式> ...]
[stored as <文件格式>]
[location <HDFS中文件路径>]
[tblproperties (<属性名> = <值>, ...)]
[as <select_statement>] 
```

>-   if not exists : 判断表是否存在
>-   partitioned by … : 分区
>-   clustered by … : 分桶
>-   row format : 行的格式, 指定每个字段用什么分割, 例如指定字段之间用’,‘隔开, 集合之间用’_‘隔开, map之间用’:‘隔开, 行之间用’\n’隔开
>-   stored as <文件格式> : 指定这张表的存储类型
>-   location <HDFS中文件路径> : 表的位置
>-   tblproperties (<属性名> = <值>, …) : 表的属性的描述
>-   as <select_statement> : 把结果选成一张新的表

**例子**

```hive
create table if not exists student2(id int, name string)
row format delimited fields terminated by '\t'
stored as textfile
location '/user/hive/warehost/student2';
```

## **DML**

**从文件插入数据**

```hive
-- 从本地文件插入
load data local inpath'/本地文件路径' into table table_name;
-- 从hdfs插入
load data inpath'/hdfs文件路径' into table_name;
```



**hive 通常有三种方式对包含分区字段的表进行数据插入**

```hive
-- 静态插入数据
insert overwrite tablename （year='2017', month='03'） select a, b from tablename2;
-- 动静混合
insert overwrite tablename （year='2017', month） select a, b from tablename2;
-- 动态分区
insert overwrite tablename （year, month） select a, b from tablename2;
```

**insert into**

```hive
insert into table tablename1 select a, b, c from tablename2;
```

**insert overwrite**

```hive
insert overwrite table tablename1 select a, b, c from tablename2;
```
