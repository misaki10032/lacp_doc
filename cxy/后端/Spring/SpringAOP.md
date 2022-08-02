[toc]

# 动态代理

- 动态代理和静态代理的角色实一样的
- 动态代理是动态生成的,静态代理是自己写好的
- 动态代理分类:基于接口的动态代理,基于类的动态代理
  - 基于接口 ---JDK动态代理
  - 基于类 ---CGlib
  - java字节码实现 ---javaSIST

## Proxy

动态生成代理类

```java
package com.cxy.util;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

public class ProxyInvocationHandler implements InvocationHandler {
    private Object target;
    //设置代理对象
    public void setTarget(Object target){
        this.target = target;
    }
    //获得代理类
    public Object getProxy(){
        return Proxy.newProxyInstance(this.getClass().getClassLoader(), target.getClass().getInterfaces(),this);
    }
    //处理代理实例
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        log(method.getName());
        return  method.invoke(target, args);
    }
    //提示日志
    public void log(String msg){
        System.out.println("代理处理了"+msg+"方法");
    }
}

```

- 测试

- ```java
  package com.cxy.service;
  
  import com.cxy.util.ProxyInvocationHandler;
  
  public class Client {
  
      public static void main(String[] args) {
          //真实角色
          User user = new User();
          //代理角色
          ProxyInvocationHandler pih = new ProxyInvocationHandler();
          pih.setTarget(user);
          //动态生成代理类
          UserService proxy = (UserService) pih.getProxy();
          proxy.getUserService("送货");
      }
  }
  
  ```

## Spring AOP

允许用户自定义切面

- 导入依赖包

```xml
<!--代理依赖-->
<dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjweaver</artifactId>
            <version>1.9.4</version>
        </dependency>
```

### 实现方式1接口api实现:

> 日志类
>
> ```java
> 1.
>     package com.cxy.log;
> 
> import org.springframework.aop.MethodBeforeAdvice;
> 
> 
> import java.lang.reflect.Method;
> 
> public class Log implements MethodBeforeAdvice {
>     public void before(Method method, Object[] objects, Object o) throws Throwable {
>         System.out.println(o.getClass().getName()+"的"+method.getName()+"被执行了!");
>     }
> }
> 2.
>     package com.cxy.log;
> 
> import org.springframework.aop.AfterReturningAdvice;
> 
> import java.lang.reflect.Method;
> 
> public class AfterLog implements AfterReturningAdvice {
>     public void afterReturning(Object returnValue, Method method, Object[] args, Object target) throws Throwable {
>         System.out.println("执行了"+method.getName()+"方法,返回值:"+returnValue);
>     }
> }
> ```
>
> 2.实现类,真实对象
>
> ```java
> package com.cxy.service;
> 
> public interface UserService {
> 
>     String getUserService(String msg);
> 
>     void add();
> 
>     void delete();
> }
> 
> 
> 2.
>     package com.cxy.service;
> 
> import org.springframework.stereotype.Component;
> 
> public class User implements UserService{
> 
>     public String getUserService(String msg) {
>         return msg;
>     }
> 
>     public void add() {
>         System.out.println("添加了一个用户");
>     }
> 
>     public void delete() {
>         System.out.println("删除了一个用户");
>     }
> }
> 
> ```
>
> 
>
> spring配置
>
> ```xml
> <?xml version="1.0" encoding="UTF-8"?>
> <beans xmlns="http://www.springframework.org/schema/beans"
>        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>        xmlns:aop="http://www.springframework.org/schema/aop"
>        xsi:schemaLocation="http://www.springframework.org/schema/beans
>         https://www.springframework.org/schema/beans/spring-beans.xsd
>         http://www.springframework.org/schema/aop
>         https://www.springframework.org/schema/aop/spring-aop.xsd
>        ">
> 
>     <bean id="user" class="com.cxy.service.User"/>
>     <bean id="log" class="com.cxy.log.Log"/>
>     <bean id="afterLog" class="com.cxy.log.AfterLog"/>
> 
>     <aop:config>
>         <aop:pointcut id="pointcut" expression="execution(* com.cxy.service.User.*(..))"/>
>         <aop:advisor advice-ref="log" pointcut-ref="pointcut" />
>         <aop:advisor advice-ref="afterLog" pointcut-ref="pointcut"/>
>     </aop:config>
> 
> </beans>
> ```
>
> 测试类
>
> ```java
> @Test
>     public void text1(){
>         ApplicationContext context = new ClassPathXmlApplicationContext("bean.xml");
>         UserService user = (UserService)context.getBean("user");
>         user.add();
>     }
> ```
>
> 结果
>
> ```text
> com.cxy.service.User的add被执行了!
> 添加了一个用户
> 执行了add方法,返回值:null
> ```

### 实现方式2自定义切面

> 1.自定义方法切面
>
> ```java
> package com.cxy.log;
> 
> public class MyDiyLog {
> 
>     public void befor(){
>         System.out.println("=====执行前========");
>     }
> 
>     public void after(){
>         System.out.println("=====执行后========");
>     }
> }
> ```
>
> 2.配置
>
> ```xml
> <?xml version="1.0" encoding="UTF-8"?>
> <beans xmlns="http://www.springframework.org/schema/beans"
>        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>        xmlns:aop="http://www.springframework.org/schema/aop"
>        xsi:schemaLocation="http://www.springframework.org/schema/beans
>         https://www.springframework.org/schema/beans/spring-beans.xsd
>         http://www.springframework.org/schema/aop
>         https://www.springframework.org/schema/aop/spring-aop.xsd
>        ">
> 
>     <bean id="user" class="com.cxy.service.User"/>
>     <bean id="log" class="com.cxy.log.Log"/>
>     <bean id="afterLog" class="com.cxy.log.AfterLog"/>
>     <bean id="diy" class="com.cxy.log.MyDiyLog"/>
>     <aop:config>
>         <aop:aspect ref="diy">
>             <aop:pointcut id="point" expression="execution(* com.cxy.service.*.*(..))"/>
>             <aop:before method="befor" pointcut-ref="point"/>
>             <aop:after method="after" pointcut-ref="point"/>
>         </aop:aspect>
> 
>     </aop:config>
> 
> </beans>
> ```
>
> 3.测试
>
> ```java
> public class Text {
>     @Test
>     public void text1(){
>         ApplicationContext context = new ClassPathXmlApplicationContext("bean.xml");
>         UserService user = (UserService)context.getBean("user");
>         user.add();
>     }
> }
> ```
>
> 4.结果
>
> ```text
> =====执行前========
> 添加了一个用户
> =====执行后========
> 
> 进程已结束,退出代码0
> 
> ```

### 方式三使用注解

@Aspect 标注这个类是一个切面

@Before 标注之前执行

@After 之后

@Around 给定一个参数,代理获取的切入点

- 实现类

  ```java
  package com.cxy.log;
  import org.aspectj.lang.annotation.After;
  import org.aspectj.lang.annotation.Aspect;
  import org.aspectj.lang.annotation.Before;
  public class AutoDiyli {
      @Before("execution(* com.cxy.service.*.*(..))")
      public void befor(){
          System.out.println("------------执行前----------");
      }
      @After("execution(* com.cxy.service.*.*(..))")
      public void after(){
          System.out.println("------------执行后----------");
      }
          @Around("execution(* com.cxy.service.*.*(..))")
      public void huan(ProceedingJoinPoint pjp) throws Throwable {
          System.out.println("=====环绕前====");
          Object proceed = pjp.proceed();
          pjp.getSignature();//获得签名
          System.out.println("=====环绕后====");
      }
  }
  ```

  - 配置

    ```xml
     <bean id="autolog" class="com.cxy.log.AutoDiyli"/>
        <aop:aspectj-autoproxy/
                           >
    ```

  - 结果

    ```java
    =====环绕前====
    ------------执行前----------
    添加了一个用户
    ------------执行后----------
    =====环绕后====
    ```

  - @Around

    ```java
    
    ```

    