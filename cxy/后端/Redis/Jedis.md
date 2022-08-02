[toc]

# jedis

**java操作redis**

> jedis是官方推荐的java连接开发工具 

## maven依赖

```xml
<!-- https://mvnrepository.com/artifact/redis.clients/jedis -->
<dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
    <version>3.5.2</version>
</dependency>

<!-- https://mvnrepository.com/artifact/com.alibaba/fastjson -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>1.2.75</version>
</dependency>
```

## 编写java代码

```java
public class redisText {
    public static void main(String[] args) {
        Jedis jedis = new Jedis("192.168.31.193",6379);
        System.out.println(jedis.ping());
        System.out.println(jedis.set("name","blank"));
        System.out.println(jedis.set("age","age"));
        System.out.println(jedis.get("name"));
    }
}
```

### 失败原因1

```bash
Exception in thread “main“ redis.clients.jedis.exceptions.JedisDataException
```

关闭受保护模式

> 进入redis

**config set protected-mode "no"**

> 是说Redis服务处于保护模式，我们需要修改配置文件redis.conf。将NETWORK下的protected-mode yes修改
>
> 为protected-mode no，然后重启服务（./bin/redis-server ./redis.conf）

```bash
blank@ubuntu:~/桌面$ cd /usr/local/bin/bconfig
blank@ubuntu:/usr/local/bin/bconfig$ ls
redis.conf
blank@ubuntu:/usr/local/bin/bconfig$ sudo gedit redis.conf
blank@ubuntu:~$redis-server /usr/local/bin/bconfig/redis.conf
```

### 失败原因2

```bash
java.net.SocketTimeoutException: connect timed out
```

> 解决:关闭bind:127.0.0.1 ::1
>
> 进入配置文件注释这一句

![image-20210405144117451](.\image-20210405144117451.png)

```bash
blank@ubuntu:~/桌面$ cd /usr/local/bin/bconfig
blank@ubuntu:/usr/local/bin/bconfig$ ls
redis.conf
blank@ubuntu:/usr/local/bin/bconfig$ sudo gedit redis.conf
blank@ubuntu:~$redis-server /usr/local/bin/bconfig/redis.conf
```

## 测试运行

```java
PONG
OK
OK
blank
```

**全部的命令都可以使用 `jedis.方法运行`**

## jedis事务

```java
Transaction multi = jedis.multi();
try{
    multi.set("hello","world");
    multi.ecec();
}catch(Exception e){
    multi.discard();
}finally{
    sout(jedis.get("hello"));
    jedis.close();
}
```



# Spring Boot整合

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

**在SpringBoot 2.x以后 , jedis被替换成了 lettuce**

> jedis: 采用直连 , 多线程不安全 , 如果要避免,需要使用jedis pool
>
> lettuce:采用netty , 实力可以在多个线程中共享 , 减少线程数据 , 性能更高

```properties
spring.redis.host=192.168.31.193
spring.redis.port=6379
```

### 测试

![image-20210405152809041](.\image-20210405152809041.png)

### 使用springboot存对象相关序列化问题

1 . 构建自己的实体类

> 对象必须序列化,不序列化报错

```java
package com.cxy.redis.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.io.Serializable;
@Data
@AllArgsConstructor
@NoArgsConstructor
public class User implements Serializable {
    private String name;
    private Integer age;
}
```

2 . 编写测试类

```java
package com.cxy.redis;
import com.cxy.redis.pojo.User;
import com.fasterxml.jackson.core.JsonProcessingException;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.redis.core.RedisTemplate;
@SpringBootTest
class RedisApplicationTests {
    @Autowired
    private RedisTemplate redisTemplate;
    @Test
    public void test() throws JsonProcessingException {
        User user = new User("user", 3);
        redisTemplate.opsForValue().set("user",user);
        System.out.println(redisTemplate.opsForValue().get("user"));
    }

}
```

> 序列化问题

**直接向value中存对象 , 会发生问题**

![image-20210405164932080](.\image-20210405164932080.png)

**对象的key被保存成了乱码的样子**

*原因是redisTemplate , 默认使用的JDK序列化方式*

> 解决

key的序列化使用String序列化`stringRedisSerializer` , value使用`jackson2JsonRedisSerializer`序列化

> 编写自己的配置类

```java
package com.cxy.redis.config;
import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.PropertyAccessor;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.jsontype.impl.LaissezFaireSubTypeValidator;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.Jackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.JdkSerializationRedisSerializer;
import org.springframework.data.redis.serializer.StringRedisSerializer;
import java.net.UnknownHostException;
@Configuration
public class RedisConfig {
    //自己的redisTemplate
    @Bean
    @SuppressWarnings("all")
    public RedisTemplate<String, Object> redisTemplates(RedisConnectionFactory factory) {
        RedisTemplate<String,Object> template = new RedisTemplate<>();
        template.setConnectionFactory(factory);
        //序列化配置
        Jackson2JsonRedisSerializer<Object> jackson2JsonRedisSerializer = new Jackson2JsonRedisSerializer<Object>(Object.class);
        ObjectMapper om = new ObjectMapper();
        om.setVisibility(PropertyAccessor.ALL, JsonAutoDetect.Visibility.ANY);
        om.activateDefaultTyping(LaissezFaireSubTypeValidator.instance,ObjectMapper.DefaultTyping.NON_FINAL, JsonTypeInfo.As.WRAPPER_ARRAY);
        jackson2JsonRedisSerializer.setObjectMapper(om);
        //string的序列化
        StringRedisSerializer stringRedisSerializer = new StringRedisSerializer();
        //key采用string的序列化方式
        template.setKeySerializer(stringRedisSerializer);
        //hash的key采用string的序列化方式
        template.setHashKeySerializer(stringRedisSerializer);
        //value采用string的序列化方式
        template.setValueSerializer(jackson2JsonRedisSerializer);
        //hash的value采用string的序列化方式
        template.setHashValueSerializer(jackson2JsonRedisSerializer);
        template.afterPropertiesSet();
        return template;
    }
}
```

**使用注解导入自己的配置**

```java
@Qualifier("redisTemplates")
private RedisTemplate redisTemplate;
```

> 启动测试

![image-20210405165434105](.\image-20210405165434105.png)

**乱码解决**

![image-20210405165519868](.\image-20210405165519868.png)

> 一般会编写RedisUtil去调用redis











