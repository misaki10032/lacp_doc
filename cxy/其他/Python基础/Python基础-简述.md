# Python基础



## 简述

python是什么类型的语言

​		python是弱类型语言

​		脚本语言是计算机编程语言，因此也能让开发者编写出让电脑听命行事的程序。以简单的方式完成某些复杂的事情通常是创造脚本语言的重要原则，基于这项原则，使得脚本语言通常比C语言、C++语言或者java之类的系统编程语言要简单容易。

​		什么是强类型，比如c或者java这些语言在声明变量之前是需要定义变量是int还是str类型的。php是弱类型的语言，它不会区分变量的类型，你给它什么它就是什么。python在声明变量的时候也没有给定类型，python的变量是引用内存地址的，如果给一个其它类型的变量，它会把指针指向另一个地方。

### 		pyc文件

​		python的文件都是以.py结尾的.

​		pyc是一种**二进制文件**，是由py文件经过编译后，生成的文件，是一种byte code，py文件变成pyc文件后，加载的速度有所提高，而且pyc是一种跨平台的字节码，是由python的虚拟机来执行的，这个是类似于JAVA或者.NET的虚拟机的概念。pyc的内容，是跟python的版本相关的，不同版本编译后的pyc文件是不同的，2.5编译的pyc文件，2.4版本的 python是无法执行的。

​		因为py文件是可以直接看到源码的，为了不泄露源码,所以就需要编译为pyc后，再发布出去。当然，pyc文件也是可以反编译的，不同版本编译后的pyc文件是不同的，根据python源码中提供的opcode，可以根据pyc文件反编译出py文件源码，网上可以找到一个反编译python2.3版本的pyc文件的工具，如果需要反编译出新版本的pyc文件的话，就需要自己动手了,不过你可以自己修改python的源代码中的opcode文件，重新编译 python，从而防止不法分子的破解。

```python
#我们把编写好的python文件的记录下来
#在cmd中运行：
#python -m 你的文件名.py
#或者在IDLE中运行：
import py_compile
py_compile.compile(r'H:\game\test.py')  正则
#如果是批量生产pyc文件可以直接指定一个目录
```

​		查看pyc文件

```
#找到pyc文件的目录
#当你生成pyc文件成功以后默认有一个名为‘__pycache__’的文件夹
#进入文件夹输入
hexdump -C test.cpython-36.pyc 

```

## 了解python

​		从CMD启动python

```python
#首先我们打开cmd 输入python
import sys
print(sys.path) #打印出python的安装路径
```

​		我们在python的安装包里面可以看见`idle.exe`把它发送到桌面的快捷方式上去，它可以直接打开python自带的编译工具，而不需要从cmd进入

​		IDLE是什么：

​		IDLE是python shell，就是通过输入文本与程序交互的途径。就像是我们windows的cmd窗口，linux的命令窗口那样的东西，使用它们给计算机下达命令.

​		同样的利用IDLE就可以给python下达命令	

​		**python不同版本的语言语法不兼容**

​		对于Python3:

​		print(‘I love python’)

```python
>>> print("I love python")
# I love python
```

​		如果我们输入python2的语法
​		print "I love python"

```python
>>> print "I love python"
# SyntaxError: Missing parentheses in call to 'print'
```

​		会出现语法错误

​		如果我们输入其他语言(比如java)的语法
​		System.out.print("I love Python.");

```python
>>> System.out.print("I love Python.");
SyntaxError: invalid character in identifier
```

​		这样的话就会报名字错误 ，没有定义过
​		如果在代码前面加上了井号（#），那么后面的文字就不会被输出，井号是python中的注释，后面的内容不会被当做是a代码运行。

## python的独特

​		输入`print(5+3)`那么python会直接计算出结果,如果是c语言的话需要大费周章地利用数组做大运算，而python轻而易举地就可以完成了！

```python
#输入
print(1234567890987654321 * 9876543210123456789)
print(1234567890987654321 * 9876543210123456789)
#12193263121170553265523548251112635269
#我们在输入一下`
print('abc' + 'efg')`
#abcefg
可以看到他们两个人在一起了，非常幸福！
#语法
#输入
print('I love iphone\n' * 3)#在这里`\n`代表的是换行的意思
#I love iphone
#I love iphone
#I love iphone

```

​	乘法可以使结果重复，那么加法?

```python
print("I love python\n" + 3)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print("I love python\n" + 3)
TypeError: must be str, not int
```

​	失败了！因为在python里 加号 的作用是用来作数学运算和字符串链