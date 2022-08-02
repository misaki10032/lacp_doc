[toc]

# Go

## 环境安装

安装包下载地址：[https://golang.org/dl/](https://golang.org/dl/)

1 、将下载的二进制包解压至 /usr/local目录。

```shell
tar -C /usr/local -xzf go1.4.linux-amd64.tar.gz
```

2、将 /usr/local/go/bin 目录添加至 PATH 环境变量：

```shell
export PATH=$PATH:/usr/local/go/bin
```

以上只能暂时添加 PATH，关闭终端下次再登录就没有了。

我们可以编辑 ~/.bash_profile 或者 /etc/profile，并将以下命令添加该文件的末尾，这样就永久生效了：

```shell
export PATH=$PATH:/usr/local/go/bin
```

添加后需要执行：

```shell
source ~/.bash_profile
# 或
source /etc/profile
```

### mac m1 

推荐直接下载pkg安装包，自动配置环境变量

**终端输入检测**

```shell
➜  ~ go version
go version go1.18.4 darwin/arm64
➜  ~ 
```

## 基础

### hello world

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello World")
}
```

### 数据类型

- 布尔型 
  - true或者false，例：`var b bool = true`或`var b = true`

- 数字类型
  - 整形int`var i = 1`
  - 浮点型float32和float64
- 字符串
  - 字符串就是一串固定长度的字符连接起来的字符序列。Go 的字符串是由单个字节连接起来的。Go 语言的字符串的字节使用 UTF-8 编码标识 Unicode 文本。
- 派生类型
  - 指针类型（Pointer）
  - 数组类型
  - 结构化类型(struct)
  - Channel 类型
  - 函数类型
  - 切片类型
  - 接口类型（interface）
  - Map 类型

### 变量和常量定义

```go
package main

import "fmt"

func main() {
	const MyLength int = 10
	const MyWidth int = 5
	var area int
	const a, b, c = 1, false, "str" //多重赋值

	area = MyLength * MyWidth
	fmt.Printf("面积为 : %d", area)
	println()
	println(a, b, c)
}
```

### 运算符

| 运算符 | 描述 | 实例               |
| :----- | :--- | :----------------- |
| +      | 相加 | A + B 输出结果 30  |
| -      | 相减 | A - B 输出结果 -10 |
| *      | 相乘 | A * B 输出结果 200 |
| /      | 相除 | B / A 输出结果 2   |
| %      | 求余 | B % A 输出结果 0   |
| ++     | 自增 | A++ 输出结果 11    |
| --     | 自减 | A-- 输出结果 9     |

### 条件语句

`if - else 语句`

```go
package main

import "fmt"

func main() {
	var chose int
	fmt.Scan(&chose)
	if chose < 10 {
		fmt.Print("太小啦")
	} else if chose == 10 {
		fmt.Print("nice")
	} else {
		fmt.Print("太大了")
	}
}
```

`swatch 语句`

```go
	switch chose {
    case 1:
      fmt.Print("太小啦")
    case 10:
      fmt.Print("nice")
    case 20:
      fmt.Print("太大了")
    default:
      fmt.Print("error")
	}
```

`select 语句`

```go
	var c1, c2 ,c3 chan int
	var i1, i2 int
	select {
	case i1 = <-c1:
		fmt.Println("i1=",i1," from c1=",c1)
	case c2 <- i2:
		fmt.Println("i2=",i2,"to c2=",c2)
	case i3,ok := (<-c3):
		if ok {
			fmt.Println("i3=",i3," from c3",c3)
		} else {
			fmt.Println("c3 is closed")
		}
	default:
		fmt.Println("no communication")
	}
```































