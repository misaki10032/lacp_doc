## 什么是Quarkus

> 官方文档： https://cn.quarkus.io/about/

### 简介

传统的Java堆栈是为单体应用设计的，启动时间长，内存需求大，而当时还没有云、容器和Kubernetes的存在。Java框架需要发展以满足这个新世界的需求。

Quarkus的创建是为了使Java开发人员能够为现代的、云原生的世界创建应用程序。Quarkus是一个为GraalVM和HotSpot定制的Kubernetes原生Java框架，由最佳的Java库和标准精心打造。其目标是使Java成为Kubernetes和无服务器环境的领先平台，同时为开发者提供一个框架，以解决更广泛的分布式应用架构问题。

### 特性

1. 轻量级：Quarkus框架采用了轻量级的编程模型，减少了应用程序的内存占用和启动时间。它使用了Just-In-Time（JIT）编译和Ahead-Of-Time（AOT）编译相结合的方式，使得应用程序在运行时能够更加高效地利用系统资源。
2. 高性能：Quarkus框架通过优化JVM和原生编译技术，提高了应用程序的性能和响应速度。它支持反应式编程模型，能够处理高并发、低延迟的场景，使得应用程序能够更好地适应云原生环境的需求。
3. 易于使用：Quarkus框架提供了丰富的特性和工具，使得开发者能够更轻松地构建、部署和运行云原生应用。它支持多种开发模式，如Maven、Gradle等，同时提供了可视化的开发环境和调试工具，方便开发者进行开发和调试。
4. 强大的生态支持：Quarkus框架得到了许多开源社区和企业的支持，如Red Hat、IBM等。它提供了丰富的扩展和插件，支持多种：数据库、消息队列、缓存等技术，方便开发者快速构建功能强大的应用程序。

### 对比SpringBoot

https://juejin.cn/post/7023317351563001886

## 使用IDEA创建项目

- JDK - GraalVM 17.0.11
- Maven 3.8.3
- IDEA

### 创建项目

![Pasted-image-20240710172301.png](./Pasted%20image%2020240710172301.png)

### 集成Mybatis

```xml
<dependency>  
    <groupId>io.quarkus</groupId>  
    <artifactId>quarkus-rest</artifactId>  
</dependency>  
<dependency>  
    <groupId>org.projectlombok</groupId>  
    <artifactId>lombok</artifactId>  
    <version>1.18.28</version>  
</dependency>  
<dependency>  
    <groupId>io.quarkus</groupId>  
    <artifactId>quarkus-jdbc-mysql</artifactId>  
</dependency>  
<dependency>  
    <groupId>io.quarkiverse.mybatis</groupId>  
    <artifactId>quarkus-mybatis-plus</artifactId>  
    <version>2.2.3</version>  
</dependency>  
<dependency>  
    <groupId>io.quarkus</groupId>  
    <artifactId>quarkus-arc</artifactId>  
</dependency>  
<dependency>  
    <groupId>io.quarkus</groupId>  
    <artifactId>quarkus-junit5</artifactId>  
    <scope>test</scope>  
</dependency>  
<dependency>  
    <groupId>io.rest-assured</groupId>  
    <artifactId>rest-assured</artifactId>  
    <scope>test</scope>  
</dependency>
```

### 项目配置文件

```properties
quarkus.datasource.jdbc.url=jdbc:mysql://127.0.0.1:3306/db_lacp_dbma?useUnicode=true&characterEncoding=utf-8&serverTimezone=Asia/Shanghai&allowMultiQueries=true  
quarkus.datasource.jdbc.driver=com.mysql.cj.jdbc.Driver  
quarkus.datasource.username=root  
quarkus.datasource.password=xxxxxxx  
  
quarkus.mybatis.mapper-locations=classpath:mapper/*.xml
```

### 实体类和接口

**实体类**

```java
@Data  
@NoArgsConstructor  
@AllArgsConstructor  
@Builder  
@Accessors(chain = true)  
@TableName("t_lacp_dbma_spider_goods")  
@ToString  
public class SpiderGoodDTO {  
    private Integer id;  
    @TableField("good_name")  
    private String goodName;  
    @TableField("shop_name")  
    private String shopName;  
    @TableField("good_price")  
    private String goodPrice;  
    @TableField("good_region")  
    private String goodRegion;  
    @TableField("payment_num")  
    private String paymentNum;  
    @TableField("spider_keywords")  
    private String spiderKeywords;  
    @TableField("spider_source")  
    private String spiderSource;  
    @TableField("create_time")  
    private String createTime;  
    @TableField("update_time")  
    private String updateTime;  
}
```

**Mapper**

```java
@Mapper  
public interface SpiderGoodMapper extends BaseMapper<SpiderGoodDTO> {}
```

### 编写Resource

```java
@Path("/good")  
public class ExampleResource {  
  
    @Inject  
    SpiderGoodMapper goodMapper;  
  
    @GET  
    @Path("/byTime/{time}")  
    @Produces(MediaType.TEXT_PLAIN)  
    public String hello(@PathParam("time") @Encoded String time) {  
        QueryWrapper<SpiderGoodDTO> wrapper = new QueryWrapper<>();  
        wrapper.inSql("id", "select id from t_lacp_dbma_spider_goods where left(create_time, 10) = '" + time + "'");  
        System.out.println("select id from t_lacp_dbma_spider_goods where left(create_time, 10) = '" + time + "'");  
        List<SpiderGoodDTO> spiderGoodDTOS = goodMapper.selectList(wrapper);  
        System.out.println(spiderGoodDTOS.size());  
        return spiderGoodDTOS.toString();  
    }  
}
```

通过这个Resource看出来，和平时的controller相似度很高。

### 启动项目

#### 使用Quarkus-cli

```base
quarkus:dev
```

#### 使用Maven

```bash
 ./mvnw compile quarkus:dev
```

![Pasted-image-20240711113036.png](./Pasted%20image%2020240711113036.png)
![Pasted-image-20240711113145.png](./Pasted%20image%2020240711113145.png)
会自带一个开发者UI
![Pasted-image-20240711113215.png](./Pasted%20image%2020240711113215.png)

#### 编写测试用例

```java
@QuarkusTest  
class ExampleResourceTest {  
    @Test  
    void testHelloEndpoint() {  
        given()  
            .when().get("/good/byTime/2023-04-27")  
            .then()  
            .statusCode(200)  
            .body(notNullValue());  
    }  
}
```

测试成功
![Pasted-image-20240711113240.png](./Pasted%20image%2020240711113240.png)

### Tip

#### 不指定JDBCurl或链接配置错误

quarkus会自动在docker上开启一个mysql的容器
![Pasted-image-20240711114227.png](./Pasted%20image%2020240711114227.png)
在docker desktop上也可以正常看到：
![Pasted-image-20240711114307.png](./Pasted%20image%2020240711114307.png)
所以说quarkus的容器化支持很好

### 编译和部署

#### 构建不需要JVM的原生可执行文件

- JDK 17+ installed with `JAVA_HOME` configured appropriately
- Apache Maven 3.9.8
- 一个运行中的容器 (Docker or [Podman](https://cn.quarkus.io/guides/podman))
- 如果你愿意的话，还可以选择使用Quarkus CLI
- 可以安装Mandrel或者GraalVM
- 一个 C语言工作开发环境
- 在开发的应用程序代码。

> **背景**：
> 构建一个原生可执行文件需要使用GraalVM的发行版。有三个发行版：Oracle GraalVM社区版（CE）、Oracle GraalVM企业版（EE）和Mandrel。Oracle和Mandrel发行版之间的区别如下：
>
> - Mandrel是Oracle GraalVM CE的一个下游发行版。Mandrel的主要目标是提供一种方法来构建专门为支持Quarkus而设计的原生可执行文件。
> - Mandrel版本的代码库来自于上游的Oracle GraalVM CE代码库，只做了一些小的改动，但也有一些重要的对于Quarkus本地应用程序来说是没有必要的排除项。它们支持与Oracle GraalVM CE相同的构建原生可执行文件的能力，在功能上没有重大变化。值得注意的是，它们不包括对多语言编程的支持。之所以排除这些功能，是为了给大多数Quarkus用户提供更好的支持水平。与Oracle GraalVM CE/EE相比，这些不包括的内容也意味着Mandrel发布的软件包大小大大减小。
> - Mandrel的构建方式与Oracle GraalVM CE略有不同，它使用标准的OpenJDK项目。这意味着，Oracle往OpenJDK增加了一些小增强功能，并用于构建Oracle自己的GraalVM，但Mandrel不能从中获益。这些增强功能被省略了，因为它上游的标准OpenJDK并不管理这些特性，也无法提供保障。这一点在涉及到一致性和安全性时尤其重要。
> - Mandrel被推荐用于构建针对Linux容器化环境的原生可执行文件。这意味着，我们鼓励Mandrel用户使用容器来构建他们的原生可执行文件。如果你要为macOS构建本地可执行文件，你应该考虑使用Oracle GraalVM，因为Mandrel目前不针对这个平台。直接在裸机Linux或Windows上构建原生可执行文件是可能的，详情可参见 [Mandrel README](https://github.com/graalvm/mandrel/blob/default/README.md) 和 [Mandrel发行版](https://github.com/graalvm/mandrel/releases) 。

配置pom文件

```xml
```xml
<profiles>
    <profile>
        <id>native</id>
        <activation>
            <property>
                <name>native</name>
            </property>
        </activation>
        <properties>
            <skipITs>false</skipITs>
            <quarkus.native.enabled>true</quarkus.native.enabled>
        </properties>
    </profile>
</profiles>
```

#### 使用quarkus cli

```bash
quarkus build --native
```

#### 使用maven

```bash
./mvnw install -Dnative
```
