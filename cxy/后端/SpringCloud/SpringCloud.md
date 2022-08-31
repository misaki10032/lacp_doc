[toc]

# 微服务

## 什么是微服务

- 微服务是一种架构模式,一种架构风格

- 将原先的一组应用程序划分成一个一个的单一应用的小服务,每个服务之间相互配合,完成整个应用。

## 为什么要使用微服务架构

部分来自于知乎:@[老刘](https://www.zhihu.com/people/xue-chuan-da-chong)

> 演变1

==传统架构==

![image-20210505140206977](.\image-20210505140206977.png)

==传统项目==

![image-20210505131427851](.\image-20210505131427851.png)

==新的需求==

![image-20210505132128090](.\image-20210505132128090.png)

- 原先的单一架构模式不能满足业务的需求,从而增加了很多庞杂的业务,出现很多的重复代码
- 不同的业务逻辑糅杂在一起,调用同一个数据库,同一张表可能被多个业务依赖,数据库也出现了性能瓶颈
- 开发、测试、部署、维护变得困难,一个小改动就会影响整个应用

> 演变2

==多个服务分开存放,但是数据库仍然是公用的==

![image-20210505132549834](.\image-20210505132549834.png)

- 数据库成为性能瓶颈,有单点故障的风险
- 数据管理混乱,不同的服务还剩会有取其他服务数据的现象
- 表结构被多个服务依赖,很难调整

> 演变3

==拆分数据库,所有持久层相互隔离,并且加入了消息队列机制==

![image-20210505133141075](.\image-20210505133141075.png)

- 系统故障后,定位困难。微服务架构整个应用分散成多个服务,定位故障点非常困难
- 在微服务中,一个服务的故障,可能产生雪崩效应,导致整个系统瘫痪,并且在高并发的场景下,故障总会出现
- 服务数量多,管理工作量巨大
- 开发上, 难以保证各个服务在持续开发的情况下协同合作
- 测试上, 原先的单一测试变成了服务之间的调用测试 , 测试变得复杂

> 演变4

- 日志分析
- 链路跟踪
- 权限控制
- 动态扩容
- Service Mesh
- ......

> 总结

服务化将不同业务逻辑进行垂直解耦，每个模块只负责一个服务，对外界透明，因此，服务模块修改升级不影响其他模块。同时，服务模块解耦，有助于实现服务模块的水平扩展，从而实现服务高可用。

- 优点
  - 单一职责
  - 每个服务足够内聚,代码容易理解
  - 开发简单,效率高,每个服务单一
  - 能够被小团队单独开发
  - 松耦合,具有功能意义
  - 微服务可以使用不同语言开发
  - 容以和第三方集成
  - 微服务容易被开发人员理解,修改和维护
  - 只是简单的逻辑代码,不会和界面混合
  - 有自己单独的数据库
  - ......
- 缺点
  - 开发人员要处理分布式系统的复杂性
  - 多服务运维难度高,运维压力大
  - 系统部署依赖
  - 成本高
  - 数据一致性难以保证
  - 测试和性能监控
  - ......

# Spring Cloud

## 什么是Spring Cloud

​		Spring Cloud为开发人员提供了快速构建分布式系统中一些常见模式的工具（例如配置管理，服务发现，断路器，智能路由，微代理，控制总线）。分布式系统的协调导致了样板模式, 使用Spring Cloud开发人员可以快速地支持实现这些模式的服务和应用程序。他们将在任何分布式环境中运行良好，包括开发人员自己的笔记本电脑，裸机数据中心，以及Cloud Foundry等托管平台。

> 特性

Spring Cloud专注于提供良好的开箱即用经验的典型用例和可扩展性机制覆盖。

- 分布式/版本化配置
- 服务注册和发现
- 路由
- service - to - service调用
- 负载均衡
- 断路器
- 分布式消息传递

## Spring Cloud和Spring Boot 的关系

- Spring Boot专注快速开发单个个体服务
- Spring Cloud关注于全局的微服务协调整理治理框架 , 把Spring Boot 开发的每个单体微服务合并管理起来 , 为各个微服务之间提供配置管理 , 服务发现 , 路由 ....... 等集成服务
- Spring Boot 可以离开Spring Cloud独立使用,开发项目,但 Spring Cloud离不开Spring Boot 

## 微服务之间是如何通信的

**微服务的通信机制**

- 组件定义为独立替换和升级的软件单元。
- 使用以业务能力为出发点组织服务的策略。
- RESTful HTTP协议是微服务架构中最常用的通讯机制。
- 微服务可以使用不同的编程语言。
- 不同微服务可以采用不同的数据持久化技术。
- 微服务非常重视建立架构及业务相关指标的实时监控和日志机制，必须考虑每个服务的失败容错机制。
- 注重快速更新，因此系统会随时间不断变化及演进。可替代性模块化设计。

**微服务的通信方式**

- 同步：
  - RPC
  - REST

- 异步：
  - 消息队列。

## Spring Cloud和 Dubbo 的区别



## 什么是服务熔断



## 什么是服务降级



## 微服务的优缺点

- 优点
  - 单一职责
  - 每个服务足够内聚,代码容易理解
  - 开发简单,效率高,每个服务单一
  - 能够被小团队单独开发
  - 松耦合,具有功能意义
  - 微服务可以使用不同语言开发
  - 容以和第三方集成
  - 微服务容易被开发人员理解,修改和维护
  - 只是简单的逻辑代码,不会和界面混合
  - 有自己单独的数据库
  - ......
- 缺点
  - 开发人员要处理分布式系统的复杂性
  - 多服务运维难度高,运维压力大
  - 系统部署依赖
  - 成本高
  - 数据一致性难以保证
  - 测试和性能监控
  - ......



## 微服务的技术栈

| 微服务条目     |   技术   |
| :------------: | :--: |
| 服务开发       |  Springboot、Spring、SpringMVC	    |
| 服务配置与管理 | Netflix公司的Archaius、阿里的Diamond等  |
| 服务注册与发现 | 	Eureka、Consul、Zookeeper等	 |
| 服务调用	| REST、RPC、gRPC	 |
| 服务熔断器| 	Hystrix、Envoy等	 |
| 负载均衡	| Ribbon、Nginx等	 |
| 服务接口调用| （客户端调用服务发简单工具）	Feign等	 |
| 消息队列| 	kafka、RabbitMQ、ActiveMQ等	|
| 服务配置中心管理	 |SpringCloudConfig、Chef等|
| 服务路由| （API网关）	Zuul等	 |
| 服务监控| 	Zabbix、Nagios、Metrics、Spectator等	|
| 全链路追踪	| Zipkin、Brave、Dapper等	 |
| 服务部署	| Docker、OpenStack、Kubernetes等	 |
| 数据流操作开发包| 	SpringCloud Stream（封装与Redis，Rabbit、Kafka等发送接收消息）|
| 事件消息总线 | 	SpringCloud Bus|

# 新建一个Spring Cloud 项目

### 建立服务注册发现中心

**建一个空的Maven项目（删除src目录）**

> pom文件如下

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.lacp</groupId>
  <artifactId>lacpCloud</artifactId>
  <version>1.0-SNAPSHOT</version>

</project>
```

**建立SpringBoot项目，pom文件如下**

> 注意：**SpringCloud的版本要和Springboot版本有对应关系**，具体可查看官网

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.7.0</version>
    <relativePath/> <!-- lookup parent from repository -->
  </parent>

  <groupId>com.lacp</groupId>
  <artifactId>cloudApi</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  <name>cloudApi</name>
  <description>lacpCloud server</description>

  <properties>
    <java.version>1.8</java.version>
    <spring-cloud.version>2021.0.3</spring-cloud.version>
  </properties>

  <dependencies>
    <!-- web -->
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <!-- eureka -->
    <dependency>
      <groupId>org.springframework.cloud</groupId>
      <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
    </dependency>
  </dependencies>

  <dependencyManagement>
    <dependencies>
      <!-- spring-cloud-dependencies -->
      <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-dependencies</artifactId>
        <version>${spring-cloud.version}</version>
        <type>pom</type>
        <scope>import</scope>
      </dependency>
    </dependencies>
  </dependencyManagement>

  <build>
    <plugins>
      <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
      </plugin>
    </plugins>
  </build>

</project>
```

**yaml配置文件**

```yaml
# 服务中心的端口
server:
    port: 25600

eureka:
    client:
    		#是否需要将自己注册到注册中心，因为该工程自己就是服务注册中心，所以无需注册。如果是多个服务注册中心集群模式，则另当别论
        registerWithEureka: false
        #是否向注册中心定时更新自己状态
        fetchRegistry: false
```

**启动类添加注解`@EnableEurekaServer`**

```java
@SpringBootApplication
@EnableEurekaServer
public class CloudApiApplication {
    public static void main(String[] args) {
        SpringApplication.run(CloudApiApplication.class, args);
    }
}
```

**启动后则可以访问到管理中心**

![image-20220830163557917](SpringCloud.assets/image-20220830163557917.png)

### 服务方配置

> **首先pom文件版本要统一**，以下是pom依赖

```xml
<dependencies>
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
  </dependency>
  <dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
  </dependency>
</dependencies>

<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.springframework.cloud</groupId>
      <artifactId>spring-cloud-dependencies</artifactId>
      <version>${spring-cloud.version}</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

**配置文件`yaml`**

```yaml
server:
    port: 25601

spring:
    application:
    		# 配置自己的服务名，和pom文件中对应
        name: lacpTestService

eureka:
    client:
    		#是否需要将自己注册到注册中心
        registerWithEureka: true
        #是否向注册中心定时更新自己状态
        fetchRegistry: true
        #注册中心地址
        serviceUrl:
            defaultZone: http://eureka:eureka@124.222.34.234:25600/eureka
```

**添加启动类注解`@EnableEurekaClient`**

```java
@SpringBootApplication
@EnableEurekaClient
public class LacpTestServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(LacpTestServiceApplication.class, args);
    }
}
```

### 调用方配置

> pom文件版本统一，以下是依赖

```xml
<dependencies>
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
  </dependency>
  <dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
  </dependency>
  <dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
  </dependency>
</dependencies>

<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.springframework.cloud</groupId>
      <artifactId>spring-cloud-dependencies</artifactId>
      <version>${spring-cloud.version}</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

**配置文件`yaml`**

和服务方基本相同

```yaml
server:
    port: 25602

spring:
    application:
    		# 配置自己的服务名，和pom文件中对应
        name: lacpTestConsumer

eureka:
    client:
    		#是否需要将自己注册到注册中心
        registerWithEureka: true
        #是否向注册中心定时更新自己状态
        fetchRegistry: true
        #注册中心地址
        serviceUrl:
            defaultZone: http://eureka:eureka@124.222.34.234:25600/eureka
```

**配置启动类注解`@EnableEurekaClient`和`@EnableFeignClients`**

```java
@SpringBootApplication
@EnableEurekaClient
@EnableFeignClients
public class LacpTestConsumerApplication {
    public static void main(String[] args) {
        SpringApplication.run(LacpTestConsumerApplication.class, args);
    }
}
```

**调用服务方接口**

- 编写调用接口

> `value`中的值为要调用的服务名
>
> `fallback`为失败调用的方法类对象
>
> **注意点：@RequestParam 必写**

```java
@FeignClient(value = "lacpTestService", fallback = FallBackExample.class)
public interface UserService {
    @GetMapping("/server1/user")
    String getUser(@RequestParam("name") String name);
}
```

- 失败的方法调用

```java
@Component
public class FallBackExample implements UserService {

    @Override
    public String getUser(@RequestParam("name") String name) {
        return "服务不可用 error -> param:" + name;
    }
}
```

- 调用方法

```java
@RestController
@RequestMapping("test")
@RequiredArgsConstructor
public class TestController {

    private final UserService userService;

    @GetMapping("service1")
    public String test1(String name){
        return userService.getUser(name);
    }

}
```

> 如果调用方和服务方不在同一台服务器上，注册中心读取到的ip为局域网ip则无法找到实例，此时有两种解决方法
>
> 1. 配置instance-ip
> 2. 指定访问url

- 注册服务时,统一都使用服务器ip来注册

```properties
# 服务名，默认取 spring.application.name 配置值，如果没有则为 unknown
eureka.instance.appname = eureka-client

# 实例ID
eureka.instance.instance-id = eureka-client-instance1

# 应用实例主机名
eureka.instance.hostname = localhost

# 客户端在注册时使用自己的IP而不是主机名，缺省：false
eureka.instance.prefer-ip-address = false

# 应用实例IP
eureka.instance.ip-address = 127.0.0.1

# 服务失效时间，失效的服务将被剔除。单位：秒，默认：90
eureka.instance.lease-expiration-duration-in-seconds = 90

# 服务续约（心跳）频率，单位：秒，缺省30
eureka.instance.lease-renewal-interval-in-seconds = 30

# 状态页面的URL，相对路径，默认使用 HTTP 访问，如需使用 HTTPS则要使用绝对路径配置，缺省：/info
eureka.instance.status-page-url-path = /info

# 健康检查页面的URL，相对路径，默认使用 HTTP 访问，如需使用 HTTPS则要使用绝对路径配置，缺省：/health
eureka.instance.health-check-url-path = /health
```

- feign指定访问的url

```java
@FeignClient(value = "DATABASEMANAGEMENT", url = "http://124.222.34.234:27314")
public interface DbmaService {
  
    @GetMapping("/api/news/list/top/{num}")
    String getNewsTop(@PathVariable @RequestParam("num") String num);
  
}
```













