[toc]

# springBoot整合shiro

## shiro-spring - maven依赖

```xml
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-spring</artifactId>
    <version>1.7.1</version>
</dependency>
```

## shiro快速上手

shiro会通过他的自定义异常来帮助我们做安全管理 , 比如验证密码或者权限验证

> shiro的快速开始文档

```java
package com.cxy.shiro;

import lombok.extern.slf4j.Slf4j;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.*;
import org.apache.shiro.mgt.DefaultSecurityManager;
import org.apache.shiro.realm.text.IniRealm;
import org.apache.shiro.session.Session;
import org.apache.shiro.subject.Subject;
/**
 * Simple com.cxy.shiro.Quickstart application showing how to use Shiro's API.
 *
 * @since 0.9 RC2
 */
@Slf4j
public class Quickstart {
    public static void main(String[] args) {
        DefaultSecurityManager securityManager = new DefaultSecurityManager();
        IniRealm iniRealm = new IniRealm("classpath:shiro.ini");
        securityManager.setRealm(iniRealm);

        SecurityUtils.setSecurityManager(securityManager);
        //获取当前对象
        Subject currentUser = SecurityUtils.getSubject();
        //通过当前对象,拿到session
        Session session = currentUser.getSession();
        session.setAttribute("someKey", "aValue");
        String value = (String) session.getAttribute("someKey");
        if (value.equals("aValue")) {
            log.info("Subject--->session[" + value + "]");
        }
        //判断当前用户是否被认证
        if (!currentUser.isAuthenticated()) {
            //没被认证的话生成一个令牌
            UsernamePasswordToken token = new UsernamePasswordToken("lonestarr", "vespa");
            token.setRememberMe(true);//记住我
            try {
                currentUser.login(token);
            } catch (UnknownAccountException uae) {
                log.info("没有用户名为-->" + token.getPrincipal());
            } catch (IncorrectCredentialsException ice) {
                log.info("密码帐户-->" + token.getPrincipal() + ",是不正确的!");
            } catch (LockedAccountException lae) {
                log.info("用户名的帐户-->" + token.getPrincipal() + ",被锁定了.  " +
                        "请联系您的管理员解锁.");
            }
            catch (AuthenticationException ae) {
                //其他的catch块
            }
        }

        //say who they are:
        //打印它们的标识主体(在本例中是用户名):
        log.info("User [" + currentUser.getPrincipal() + "] 登陆成功.");

        //test a role:
        if (currentUser.hasRole("schwartz")) {
            log.info("愿schwartz与你同在!");
        } else {
            log.info("你好,凡人.");
        }

        //测试类型化权限(不是实例级权限)
        if (currentUser.isPermitted("lightsaber:wield")) {
            log.info("你可以使用lightsaber。明智地使用它.");
        } else {
            log.info("抱歉，lightsaber只对schwartz大师开放.");
        }

        //一个(非常强大的)实例级权限:
        if (currentUser.isPermitted("winnebago:drive:eagle5")) {
            log.info("你可以用车牌(id)“驾驶”温尼贝戈“eagle5”。  " +
                    "钥匙在这里——玩得开心!");
        } else {
            log.info("对不起，你不能开鹰5型温尼贝戈!");
        }

        //全部完成-注销!
        currentUser.logout();

        System.exit(0);
    }
}
```

> shiro.ini(配置)

```ini
# -----------------------------------------------------------------------------
[users]
#用户'root'密码'secret'和'admin'角色
root = secret, admin
#用户'guest'与密码'guest'和'guest'角色
guest = guest, guest
# user 'presidentskroob' with password '12345'("这是相同的组合
#我的行李! !”;))，以及“主席”的角色
presidentskroob = 12345, president
#用户“darkhelmet”，密码为“ludicrousspeed”，角色为“darklord”和“schwartz”
darkhelmet = ludicrousspeed, darklord, schwartz
#用户'lonestarr'密码'vespa'和角色'goodguy'和'schwartz'
lonestarr = vespa, goodguy, schwartz

# -----------------------------------------------------------------------------
#具有指定权限的角色
#
#每一行都符合在
# org.apache.shiro.realm.text。TextConfigurationRealm # setRoleDefinitions JavaDoc
# -----------------------------------------------------------------------------
[roles]
# 'admin'角色拥有所有权限，由通配符'*'表示
admin = *
# “施瓦茨”角色可以用任何光剑做任何事:
schwartz = lightsaber:*
#“好人”角色允许“驾驶”(操作)winnebago(类型)
#车牌'eagle5'(实例特定id)
goodguy = winnebago:drive:eagle5
```

> log4j.properties

```properties
log4j.rootLogger=INFO, stdout

log4j.appender.stdout=org.apache.log4j.ConsoleAppender
log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
log4j.appender.stdout.layout.ConversionPattern=%d %p [%c] - %m %n

# General Apache libraries
log4j.logger.org.apache=WARN

# Spring
log4j.logger.org.springframework=WARN

# Default Shiro logging
log4j.logger.org.apache.shiro=INFO

# Disable verbose logging
log4j.logger.org.apache.shiro.util.ThreadContext=WARN
log4j.logger.org.apache.shiro.cache.ehcache.EhCache=WARN
```

## shiro整合springboot

> 项目结构

![image-20210409193119251](.\image-20210409193119251.png)

### 编写shiro-config

> config

```java
package com.cxy.shiro.config;
import at.pollux.thymeleaf.shiro.dialect.ShiroDialect;
import org.apache.shiro.spring.web.ShiroFilterFactoryBean;
import org.apache.shiro.web.mgt.DefaultWebSecurityManager;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.LinkedHashMap;
import java.util.Map;
@Configuration
public class ShiroConfig {
    //shiroFilterFactoryBean
    @Bean
    public ShiroFilterFactoryBean getShiroFilterFactoryBean(@Qualifier("mysecurityManager")DefaultWebSecurityManager securityManager){
        ShiroFilterFactoryBean bean = new ShiroFilterFactoryBean();
        //设置安全管理器
        bean.setSecurityManager(securityManager);
        //添加shiro过滤器
        /*
        anon:无序认证即可
        authc:必须认证才可以访问
        user:必须拥有记住我功能
        perms:拥有某个资源的权限才可以访问
        role:拥有某个角色权限才可以访问
         */
        Map<String,String> filtermap = new LinkedHashMap<>();
        filtermap.put("/add","perms[123]");
        filtermap.put("/update","perms[111]");
        bean.setFilterChainDefinitionMap(filtermap);
        //设置登录页面
        bean.setLoginUrl("/login");
        //设置未授权跳转页面
        bean.setUnauthorizedUrl("/noauthor");
        return bean;
    }
    //DefaultWebSecurityManner
    @Bean(name="mysecurityManager")
    public DefaultWebSecurityManager getDefaultWebSecurityManager(@Qualifier("myRealm") MyRealm myRealm){
        DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager();
        securityManager.setRealm(myRealm);
        return securityManager;
    }
    //Realm
    @Bean(name = "myRealm")
    public MyRealm myRealm(){
        return new MyRealm();
    }

}

```

### shiro的realm编写

> realm

```java
package com.cxy.shiro.config;

import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.*;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.authz.SimpleAuthorizationInfo;
import org.apache.shiro.crypto.hash.Hash;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.session.Session;
import org.apache.shiro.subject.PrincipalCollection;
import org.apache.shiro.subject.Subject;
import org.apache.shiro.util.ByteSource;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class MyRealm extends AuthorizingRealm {
    @Override
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        System.out.println("授权--------start!");
        //授权
        SimpleAuthorizationInfo info = new SimpleAuthorizationInfo();
        Subject subject = SecurityUtils.getSubject();
        Session session = subject.getSession();
        String author = (String) session.getAttribute("author");
        info.addStringPermission(author);

        return info;
    }

    @Override
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken token) throws AuthenticationException {
        System.out.println("认证----start!-----");
        //模拟数据库取数据
        Map<String,String> map = new HashMap<>();
        map.put("admin","123");
        map.put("123","111");
        map.put("user","111");
        UsernamePasswordToken userToken = (UsernamePasswordToken)token;
        String username = userToken.getUsername();
        if(!map.containsKey(username)){
            System.out.println("-------err!!-----");
            return null;//用户不存在
        }else{
            System.out.println("认证----isok!-----");
        }
        ByteSource credentialsSalt = ByteSource.Util.bytes(username+"c1x2y3e4h");
        return new SimpleAuthenticationInfo(
                username, //存值可以通过subject取
                map.get(username), //密码
                credentialsSalt,//salt=username+salt
                getName()  //realm name
        );
    }
}
```

**因为不想连接数据库 , 所以使用了map作为替代数据 **

![image-20210409192634660](.\image-20210409192634660.png)

### 配置controller

```java
package com.cxy.shiro.controller;

import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.IncorrectCredentialsException;
import org.apache.shiro.authc.LockedAccountException;
import org.apache.shiro.authc.UnknownAccountException;
import org.apache.shiro.authc.UsernamePasswordToken;
import org.apache.shiro.session.Session;
import org.apache.shiro.subject.Subject;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletRequest;

@Controller
public class MyController {
    @RequestMapping({"/","/h1"})
    public String h1(Model model){
        model.addAttribute("msg","hello shiro");
        return "index";
    }
    @RequestMapping("/add")
    public String add(){
        return "user/add";
    }
    @RequestMapping("/update")
    public String update(){
        return "user/update";
    }
    @RequestMapping("/login")
    public String lo(){
        return "login";
    }
    @RequestMapping("/islogin")
    public String login(Model model,String nums,String pwd){
        //获取用户
        Subject subject = SecurityUtils.getSubject();
        //封装
        UsernamePasswordToken token = new UsernamePasswordToken(nums,pwd);
        //执行登录的方法
        try{
            subject.login(token);
            //通过subject取
            String num1 = (String) subject.getPrincipal();
            Session session = subject.getSession();
            session.setAttribute("author",pwd);
            model.addAttribute("user",num1);
            model.addAttribute("msg","hello shiro");
            return "index";
        }catch (UnknownAccountException uae) {
            model.addAttribute("msg","没有用户名为-->" + token.getPrincipal());
            return "login";
        } catch (IncorrectCredentialsException ice) {
            model.addAttribute("msg","密码帐户-->" + token.getPrincipal() + ",是不正确的!");
            return "login";
        } catch (LockedAccountException lae) {
            model.addAttribute("msg","用户名的帐户-->" + token.getPrincipal() + ",被锁定了.请联系您的管理员解锁.");
            return "login";
        }
    }
    @RequestMapping("/noauthor")
    @ResponseBody
    public String noauthor(){
        return "没有权限访问";
    }

}
```

### 效果

> 首页

![image-20210409193200723](.\image-20210409193200723.png)

> 点击add 

没登陆 , 所以跳转登录页面

![image-20210409193237799](.\image-20210409193237799.png)

`这里偷了个懒 , 把权限直接用密码临时用了一下`

> 所拥有的权限

![image-20210409193327754](.\image-20210409193327754.png)

> 成功访问add

![image-20210409193348841](.\image-20210409193348841.png)

> 没有权限访问update

![image-20210409193403693](.\image-20210409193403693.png)

> 123用户可以访问

![image-20210409193424476](.\image-20210409193424476.png)

![image-20210409193429881](.\image-20210409193429881.png)