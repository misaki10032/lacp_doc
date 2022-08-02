# 迭代器

## 	可迭代对象

​		可迭代对象就是可以直接作用于(比如for循环)的对象. 可迭代对象(lterable).可以用isinstance()去判断是否是lterable对象

​		可以直接作用于for循环的数据类型一般分两种

​		1.集合数据类型: list  \  tuple  \ dict  \ set  \ string

​        2.ganerator: 包括生成器 和 带yield的generator  function

```python
from collection import Iterable
print(isinstance([], Iterable)) #list
print(isinstance((), Iterable)) #tuple
print(isinstance({}, Iterable)) #dict
print(isinstance("", Iterable)) #string
print(isinstance((x for x in range(10)), Iterable))  #生成器
print(isinstance(1, Iterable)) # int

   >>>  True
   >>>  True
   >>>  True
   >>>  True
   >>>  True
   >>>  False
```

上述中除了 int  1  ,其他的都是可迭代对象.

## 迭代器

​		迭代器就是,不仅可以作用于for循环,还可以被next()函数不断调用**返回下一个值**,只到最后抛出Stoplteration错误无法返回下一个值为止.

​		可以被next()函数不断调用返回下一个值的对象被称为迭代器

​		可以使用isinstance()函数判断一个对象是否是lterator对象

```python
from  collections import Iterator

print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance("", Iterator))
print(isinstance((x for x in range(10)), Iterator))

>>>  False
>>>  False
>>>  False
>>>  False
>>>  True
```

由此可见上面数据类型中,只有生成器生成了一个迭代器对象.

```python
可迭代的对象有  __iter__ 方法，每次都实例化一个新的迭代器；

而迭代器要实现 __next__ 方法，返回单个元素，此外还要实现 __iter__ 方法，返回迭代器本身

可迭代的对象一定不能是自身的迭代器。也就是说，可迭代的对象必须实现__iter__ 方法，但不能实现 __next__ 方法
```

## next()

```python
list1 = (x for x in [5,25,66,18,95])
print(next(l)) 
print(next(l))
print(next(l))
print(next(l)) 
print(next(l))
print(list1.__next__())  #同上,只不过用了对象的调用方法  对象.方法

>>>  5
>>>  25
>>>  66
>>>  18
>>>  95
>>>  Traceback (most recent call last):
  File "E:/python基础/1.py", line 7, in <module>
    print(list1.__next__())  #同上,只不过用了对象的调用方法  对象.方法
StopIteration
```

list没有第六个值,所以最后一行发生了报错,

## 迭代器转化为可迭代对象

iter(可迭代对象)

```python
from  collections import Iterator

a = iter([1,2,3,4,5])  #lsit不是一个迭代器,是一个可迭代对象 
print(next(a))
print(next(a))

print(isinstance(iter([]), Iterator))
print(isinstance(iter(()), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter(''), Iterator))

>>>  1
>>>  2
>>>  True
>>>  True
>>>  True
>>>  True
```

上述代码说明了a列表已经被转化成为了迭代器.

## 总结

### 三者的关系

![1603095334004](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\迭代器.png)

# 生成器

生成器是一种特殊的迭代器,生成器自动实现了iter和next方法. 生成器在使用中可以待变当前迭代的值而普通迭代器会发生异常.

具有yield关键字的函数都是生成器,yield类似于return,不同点是,return返回值后,函数会被释放掉,而yield不会, 在直接调用next方法或用for语句进行下一次迭代时, 生成器会从yield下一句开始执行, 直至遇到下一个yield。 

看个例子:

```python
def creatGeneratorOne():
    list1 = [1,2,3]
    for i in list1:
        yield i**2
def creatGeneratorTwo():
    list1 = [1,2,3]
    for i in list1:
        return i**2
print(creatGeneratorOne())
print(creatGeneratorTwo())

>>>	<generator object creatGeneratorOne at 0x02F380F0>
>>>	1
```

**yield返回了一个迭代器,而return返回了一个 1的平方 ,(也说明return运行出来就把函数释放掉了)**

```python
def creatGeneratorOne():
    list1 = [1,2,3]
    for i in list1:
        yield i**2
def creatGeneratorTwo():
    list1 = [1,2,3]
    for i in list1:
        return i**2
G1 = creatGeneratorOne()
G2 = creatGeneratorTwo()
for i in G1:
    print(i)
for i in G2:
    print(i)
    
>>>	C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\python.exe E:/python基础/1.py
>>>	1
>>>	4
>>>	9
>>>	Traceback (most recent call last):
>>>	  File "E:/python基础/1.py", line 13, in <module>
>>>	    for i in G2:
>>>	TypeError: 'int' object is not iterable

>>>	Process finished with exit code 1
```

上述代码表示了 yield生成的是一个迭代器,可以被for 循环遍历,而且yield没返回完毕不会释放函数,return返回了一个1,不是一个可迭代对象.