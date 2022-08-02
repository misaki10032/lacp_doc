# 注释

​			每个语言中都有注释, 注释就是把代码描述出来，让其他人更快的去理解。

​			被注释的内容就是不被程序解析的文本域。

```python
#井号代表单行注释

'''
三个单引号表示多行注释
三个单引号表示多行注释
三个单引号表示多行注释
'''

"""
三个双引号表示多行注释
三个双引号表示多行注释
三个双引号表示多行注释
"""
```

##  print和input

​		print和input一个是输出一个是输入

```python
#print()的作用就是向屏幕上打印输出内容
print('hello')
print('hello1','hello2')
print(12)
print(13,14)
```

​		print的参数’end‘，我们上面的print输出完以后每次都会换行，这就是end导致的，end的默认参数是’\n‘就是回车的意思。

```python
print('hello word',end=' ')#表示以空格拼接
print('hello shanghai'，end=' =>') #表示以=>（箭头）拼接

>>>hello word hello shanghai =>
```

​		input就是接受我们输入的信息的,input种的文字,会被打印到终端里:作为提示语句

类似java中的		scanner (system.in)

```python
name = input('随便输入一段话：')
print(name)

>>>随便输入一段话：你好python
>>>你好python

```

## 标识符

​		标识符就是一段字符,类名,函数名,变量名,文件名

​		标识符的规则

```python
1、只能由字母、数字、下划线组成，且不能以数字开头。
2、不能是python的关键字 
	input
	import keyword
	print(keyword.kwlist)
	可以在python脚本中引入keyword查看
3、区分大小写，见名知意，比如声明一个（用户账号）的变量 ：username
```

​		标识符的作用就是给变量、函数、类等等命名的。

​		**在python3中非 ASCII 标识符也是允许的**

## 数据类型

​		对于计算机而言, 不同的数据就需要不同的类型。

​		python的中的变量是没有数据类型的，python中的变量更加像是标签想贴哪儿就贴哪儿，通过这个标签，就可以找到变量在内存中对应的存放位置。

```python
python的数据类型有       
	number(数字)：
    	int（整形或者说正整数和负整数）、
    	float（浮点型或者说小数）、
    	complex(复数)
	str(字符串)
	bool(布尔值)
	none(空值)
	list(列表)    
	tuple(元祖)
	dict(字典)
	set(集合)
```

## 变量和常量

​		当一个赋值给一个名字时，它会储存在内存中，把这块内存空间成为变量，在大多数语言中，都把这种行为称为’给变量赋值‘或’或把值存在变量中‘。

​		python不同于其它语言，python并不是把值存在变量中，而是把名字’贴‘在’值‘上面。所以python'的变量不需要声明变量类型,你给他什么,他就是什么.

​		常量就是恒久不变的变量，它在.py文件执行过程中就会自动加载到内存的静态区中，遗憾的是，python中没有常量的定义。

```python
name = '李连杰'
print(name)

>>>李连杰

name = '吴京'
print(name)

>>>吴京
#name是变量 等于号 后面的是值
```

​		变量是可变的

```python
x = 3
x = 5
y = 8
z = x + y
print(z)

>>>13
```

​		同样运用到字符串中：

```python
name1 = 'JACK'
name2 = 'ROSE'
name3 = name1 + name2
print(name3)

>>> JACKROSE
#这种字符串相加叫拼接
```

<font color= 'red'>需要注意的地方：</font>

```python
1、在使用之前，需要对它赋值。
2、变量名可以包括字母、数字下划线，但变量名不能以数字开头。
3、等号（=）地赋值的意思，左边是名字，右边是值，不可写反了。
4、变量的名字理论上可以取任何合法的名字，但作为一个优秀的程序员，请尽量给变量一个专业一点的名字。
```

​		使用 BIF  `id()` 它的作用是查找 值在内存中的地址，看下面的例子：

```python
num1 = 3
num2 = 3

print(id(num1),id(num2))

>>>4297636960 4297636960

#num1，和num2 的结果是一样，num1和num2指向内存中的同一个地址。
```

## 类型

​		虽然我们的变量是没有类型的，但是我们的 值 是有类型区分的，怎么查看值的类型呢？

​		使用BIF  `type()` 作用是获取值的类型：

```python
str = 'abcd' 
sn  = None
int = 123
flt = 1.22
com = 234j
boo = True
print(str,sn,int,flt,com,boo)
print(type(str),type(sn),type(int),type(flt),type(com),type(boo))

>>>abcd None 123 1.22 234j True
>>><class 'str'> <class 'None'> <class 'int'> <class 'float'> <class 'complex'> <class 'bool'>
```

​		通过上面的例子可以看出python的数据类型有

​					`数字(number)、字符型(string)、布尔型(boolean)、None(空值)`

​		Python中还有:

​					`列表(list)、tuple(元祖)、dict(字典)、set(集合)`

​		python的8种数据类型


​		还可以使用 isinstance(）

```python
stri = '123'
print(isinstance(stri,int))
print(isinstance(stri,str))

>>>False
>>>True
#第一个参数是我们要分辨的变量，第二个参数是我们需要判断的类型，
#它只会返回True和False
```

## Number

​		number类型分为 `整形、浮点型、复数`

​		整形说白了就是整数，python3的整形已经与长整型进行了无缝结合，现在的python3的整形类似于Java的BigInteger类型，它的长度不受限制，如果非要有个限制，那就只限于计算机的虚拟内存总数了。所以python3很容易进行大数计算。

```python
num1 = 10
num2 = num1
print(id(num2))
# 连续定义多个变量
num3 = num4 = num5 = 1
print(num3, num4, num5)
#交互式赋值定义变量
num6, num7 = 6, 7
print(num6, num7)

```

## float(浮点数)

​		浮点数就是小数

​		**E记法**。也就是我们平时说的科学计数法，用于表示特别大和特别小的数：

```python
num = 0.000025
print(num)

>>>2.5e-05

num = 25000
print(format(num,'.1e'))

>>>2.5e+04

#python3在正整数输出的时候默认会原样输出，所以使用format()函数转换成科学计数法。
format(num,'.1e')第二个参数是'.1e'表示保留小数点后面的1个小数部分。
format(num,'e')如果是”e“会默认保留多个小数部分。
```

## 复数

​		复数由虚部和实部构成。一个复数是一对有序浮点数(x, y)。

​		表示为x + yj，其中x是实数部分，y是虚数部分。 

```python
虚数不能单独存在，它们总是和一个值为 0.0 的实数部分一起来构成一个复数。
复数由实数部分和虚数部分构成
表示虚数的语法： real+imagj
实数部分和虚数部分都是浮点数
虚数部分必须有后缀j或J。
```

​		复数的内建属性 
​		复数对象拥有数据属性，分别为该复数的实部和虚部。复数还拥有conjugate 方法，调用它可以返回该复数的共轭复数对象。

​		复数属性：

```python
属性                   描述 
num.real             该复数的实部 
num num.imag         该复数的虚部 
num.conjugate()      返回该复数的共轭复数
```

```python
c=2.3+2.5j
print(c.real)
print(c.imag)
print(c.conjugate())

>>>2.3
>>>2.5
>(2.3-2.5j)
```

## 类型的转换

接下来介绍几个跟数据类型紧密相关的函数：int()、float()、str()

**int()：**

  			`int()`的作用是将一个字符串或者一个浮点数转换成一个整数

```python
a = '123'
b = 3.1415926
c = 5.9
print(int(a),end=',')
print(int(b),end=',')
print(int(c))

>>>123,3,5

#int在转换浮点型的时候，python会采取’截断‘处理，就是把小数点后面的数据直接砍掉，而不是四舍五入；
```


<font color='red'>注意：</font>

```python
a = '4a'
print(int(a))  #如果这个字符串里面不是纯数字字符那么就会报错。
>>>Traceback (most recent call last):
  File "/Users/ruidong/PycharmProjects/project/demo.py", line 7, in <module>
    print(int(a),end=',')
ValueError: invalid literal for int() with base 10: 'q'
```

**float():**

​				`float()` 的作用是把一个字符串或整数转换成浮点数。

```python
a = 520
b = '520'
c = '980'
print(float(a))
print(float(b + c))

>>>520.0
>>>520980.0

#python进行浮点型转换的时候默认在后面加了一个’.0‘
```

**str():**
				`str()`的作用是将一个数或任何类型转换成一个字符串

```python
a = str(3.4)
b = str(89)
c = 5e15
print(a,b,str(c))

>>>3.4 89 5000000000000000.0
#在被转类型的两边加上了引号
```

## 数学功能

```python
import math    #引入数学库
```

​		abs()绝对值

```python
a1 = -10
a2 = abs(a1)
print(a2)

>>>10
```

​		比较两个数的大小

```python
a3 = 100
a4 = 9
print((a3>a4)-(a3<a4))

>>>1
```

​		max()返回一个最大的值

```python
print(max(1,2,3,4,5,6,7,8))

>>>8
```

​		min()返回一个最小的值

```python
print(min(1,2,3,4,5,6,7,8))

>>>1
```

​		pow(x,y)求x的y次方

```python
print(pow(2, 5))

>>>32
```

​		round(x,y)四舍五入 x表示数字  y表示保留几位小数

```python
print(round(3.456))
print(round(3.556))
print(round(3.456, 2))
print(round(3.546, 1))

>>>3
>>>4
>>>3.46
>>>3.5
```

​		math.ceil()向上取整

```python
print(math.ceil(18.1))
print(math.ceil(18.9))

>>>19
>>>19
```

​		math.floor()向下取整

```python
print(math.floor(18.1))
print(math.floor(18.9))

>>>18
>>>18
```

​		math.modf()返回整数部分与小数部分

```python
print(math.modf(22.3))

>>>(0.3000000000000007, 22.0)
```

​		math.sqrt()开方 返回浮点类型

```python
print(math.sqrt(16))

>>>4.0
```

​		随机数  random.choise() 从序列的元素中随机挑选一个元素

```python
print(random.choice([1,3,5,7,9]))
print(random.choice(range(5)))#range(5) == [0,1,2,3,4]
print(random.choice("sunck"))#"sunck"  == ["s","u","n","c","k"]
print(random.choice(range(10)) + 1)
```

​		random.randrange() 从指定范围内，按指定的基数递增的集合中选取一个随机数

```python
#random.randrange([start,] stop[, step])
#start--指定范围的开始值，包含在范围内，默认是0
#stop--指定范围的结束之，不包含在范围内
#step--指定的递增数，默认是1
print(random.randrange(1, 100, 2))
#从0-99选取一个随机数
print(random.randrange(100))
```

​		random.random() 随机生产[0,1)之间的数(浮点数)

```python
print(random.random())
```

​		random.shuffle()将序列的所有元素随机排序

```python
list = [1,2,3,4,5]
random.shuffle(list)
print(list)
```

​		random.uniform(x,y)随机生产一个实数，他在[x,y]范围

```python
print(random.uniform(3,9))
```

​		**三角函数**

```python
sin(A) #返回A的正玄值
```

```python
cos(A) #返回A的余玄值
```

```python
tanA=a/b "∠A的对边/∠A的邻边"
tanA=sinA/cosA
```

```python
tan(A)  #返回A的正切值
```

___

