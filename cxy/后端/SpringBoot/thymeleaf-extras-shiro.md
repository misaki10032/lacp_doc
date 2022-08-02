[toc]

# 整合thymeleaf和shiro

## maven依赖

```xml
<dependency>
    <groupId>com.github.theborakompanioni</groupId>
    <artifactId>thymeleaf-extras-shiro</artifactId>
    <version>2.0.0</version>
</dependency>
```

## 配置shiro方言

> 增加到config中即可

```java
//配置方言
@Bean
public ShiroDialect shiroDialect() {
    return new ShiroDialect();
}
```

## 更改前端页面

> 要更改的部分

```html
<h1>首页</h1>
<span th:text="${msg}"></span>--<span th:text="${user}"></span><a th:href="@{/login}">login</a>--<span th:text="${session.author}"></span>
<hr>
<div shiro:hasPermission="123">
    <a th:href="@{/add}">add</a>
</div>
<div shiro:hasPermission="111">
    <a th:href="@{/update}">update</a>
</div>
```

## 前端效果

> 没有权限的用户不再显示标签

![image-20210409192247310](.\image-20210409192247310.png)

> admin用户只有add

![image-20210409192337363](.\image-20210409192337363.png)

> 123只有update

![image-20210409192402078](.\image-20210409192402078.png)