# python基础语法学习

​		**国际惯例**

```python
print('Hello World !')
```

​		输入这些代码，并运行:

```python
Hello World !
```

## 	**Tab按键的作用**

​	（1）缩进。
​	（2）IDLE会提供联想，比如你输入 pr 按Tab键 会提供可能使用的命令供你选择参考。

​		我们看到程序成功的运行起来了，坦白的说，这玩意配叫游戏吗？以后我们在去慢慢的改进，我们说下语法

​		一切语法类似于c语言的编程语言都叫c-like语言,有c-like编程基础的人都会受不了python的IDLE的执行过程，没有声明变量类型，直接给变量定义,还会发现python根本就没有大括号来界定作用域，好多语言都是用大括号来表示作用域的，在python中只需要用适当的缩进来表示。

## 		缩进

​		缩进是python的灵魂，缩进的严格要求，使得python的代码显得非常的精简并且要层次感。

​		但是，在python中对待代码的缩进要万分的小心，因为你如果没有正确的使用缩进，就会报错,但如果没有报错,就可能导致程序编程类别的样子

```python
n = True
if  n == True:
    print('结果是true打印是这里')
else:
    print('这里我特意少打了一个Tab，结果就发生了变化 ')
print('结果是false打印是这里')

```

## 		BIF		

​		BIF就是	`built-in Functions`，内置函数的意思。什么是内置函数？为了程序员快速的编写程序而把代码打包起来的形成的方法.

​		例如`print()`就是一个内置函数，它就是一个BIF

```python
在CMD中输入dir(__builttins__)可以看到python中的内置函数列表。
```

```python
#help()这个BIF用于现实BIF的功能描述：
>>> help(print)
Help on built-in function print in module builtins:
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
>>> 
>>> 
```

​		比如下面两个:

```python
input() #让用户输入的函数括号里面可以填写提示符
print() #打印和输出括号里的值

```

## 		编码规范

​		pep8 官网规范地址
​		`https://www.python.org/dev/peps/pep-0008/`
​		变量和函数命名：下划线分割，小驼峰
​		切片里面的冒号：冒号两边都不加空格
​		字典里面的冒号：冒号前面不加空格，后面加空格
​		lambda中的冒号：冒号前面不加空格，后面加空格
​		定义变量=号两边加空格
​		函数中形参=号两边不加空格
​		关键字参数调用函数不加空格

​		优先级高的运算符不建议有空格:

```python
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
#模块名：使用下划线分割
```

​		包名：直接全部小写，不推荐使用下划线

