#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename: hello.py

import sys
sys.path.append("../opencv/")
from filename import classname

print( "////////////////////////\n" )
print( "start-------------------" )
print( "Base data types Numbers[int,long,float,complex], String, List, Tuple, Dictionary" )
dir()#访问域
dir(os)
#类属性self
a = Student()
print('the name of method is ## {} ##'.format(sys._getframe().f_code.co_name))
print('the name of class is ## {} ##'.format(self.__class__.__name__))
a.__name__
getattr(a,'__name__')
dir(time)#获取类所有方法
sys._getframe().f_code.co_name
#检查成员
ret = hasattr(obj,'func')#因为有func方法所以返回True
print(ret)
if(ret == True) :
	#获取成员
	ret = getattr(obj, 'func')#获取的是个对象
	r = ret()
	print(r)

a = b = c = 1;
count, cc, str = 1, 2, "string";

#定义
word = 'word';
sentence = "this is a sentence";
paragraph = """ this is a   paragraph  """;

print( "----test string split repeat print(" )
print( sentence[0:5] * 6 + "hhh" )
tr.replace(old, new[, max])
str.replace("is", "was", 3);
#多行注释"""   '''

#数组  list ####################################
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday'] ;

#len(days) 获取长度
#days[0] 获取第0个元素 -1尾元素
#days.append('surday') 添加元素
#days.insert(1, 'sunday') 插入元素
#days.pop() 删除尾元素
#days.pop(2) 删除指定元素

#元组 tuple ###################################
#数据指向不变！！！！
#没有append()，insert()这样的方法。其他获取元素的方法和list是一样
#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
tupletest = ()
tup2 = (1, 2, 3, 4)

#相互转换###########
#tuple(list)
#list(tuple)

#返回多值###########
#return 1,2 #
#返回值是一个tuple！
#但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，
#按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple


time = [1, 2];
print( days )
if ( 'Monday' in days):
    print('test in monday in days');
if('tu' not in days):
    print('tu not in days');

print( days[1:4] )
print( days + time )

#数据字典
print( "--test data directionary" )
dict = {};
dict['one'] = "this is one ";
dict[2] = 2;
dict2 = {'name':'Walker', 'age':18, 'dept': 'coder'};
print( dict['one'], dict[2], "   ", dict2 )
print( "keys:", )
print(  dict2.keys() )
print( " " + "values:", )
print( dict2.values() )
#遍历字典 编码utf unicode
for key in data:
        print(key+':'+data[key])
        print(type(key))

        kt = key.encode("utf-8")
        vt = data[key].encode("utf-8")
#数据类型转换
#str(object) -> string
#int(x[, base]) -> int 
strn = "100"
strn.index("0", beg=0, end=len(string)) #exception
strn.find("0", beg=0, end=len(string))  #-1
intn = 100 
if strn==intn:
    print( "strn==intn" )
elif int(strn)==intn:
    print( "int(strn)==intn" )
else :
    print( "what the ff" )

#JSON转换
# 使用 JSON 函数需要导入 json 库：import json。
# 函数  描述
string = json.dumps(obj) # 将 Python 对象编码成 JSON 字符串
obj = json.loads(string) # 将已编码的 JSON 字符串解码为 Python 对象
v = obj['key']

#数学运算
a,b,c = 2, 3, 5
c=a+b;
print( 'a = 2, b = 3' )
print( 'a + b = ',  c )
c = a ** b;
print( 'a ** b = ', c )
c = b // a;
print( 'a // b = ', c )
a = 60;
b = 13;
c = a & b;
print( 'a = 0011 1100' )
print( 'b = 0000 1101' )
print( 'a & b = ', hex(c) )
print( 'a ^ b = ', a^b )

print( 'is 用于判断两个变量引用对象是否相同 == 判断两个变量值是否相等' )
return map[name_value] if map.has_key(name_value) else '' #3目运算

#循环
print( '---- while for ---------' )
arr = [1, 2, 3, 4, 5, 6];
even = [];
odd = [];
print( 'arr=',  arr )
while (len(arr) > 0 ):
    num = arr.pop();
    if(num % 2 == 0) :
        even.append(num);
    else :
        odd.append(num);
else :
  print( 'while else' )
arr=odd.extend(even)  #合并
arr = range(10);
print( 'even=', even )
print( 'odd =', odd )
print( 'for ai in arr : for ll in "python" ' )
for ai in arr :
    print( ai,'-', )
print(  )
for ll in 'Python' :
    print( ll,"-", )
else :
  print( 'for else' )
  
print( 'range make a sequence ', range(len(arr)) )
print( range(10) )


#时间格式化
import time
# 格式化成2016-03-20 11:45:39形式
print( time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  )
# 格式化成Sat Mar 28 22:24:24 2016形式
print( time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())  )
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print( time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")) )
timestamp = time.mktime(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# 获取当前时间时间戳
int(time.time()*1000)

import calendar
cal = calendar.month(2016, 1)
print( "以下输出2016年1月份的日历:" )
print( cal )

"""
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
"""


#函数
#可写函数说明 用参数名匹配参数值 默认值
def printme( str , age = 35 ):
   print( "打印任何传入的字符串,", str )
   return;
 
#调用print(me函数 )
printme( str = "My string");

#全局变量
globvar = 1;
# 动态个数参数  
def info(arg1, *vartuple ) :
   global globvar    # 使用 global 声明全局变量
   print( "输出: " )
   print( arg1 )
   for var in vartuple:
      print( var )
   return;
#第二种动态参数 **a 两个星号，必须有一个key，一个vlue
def f(**a):
  print(a,type(a))
  f(k1=123,k2='gyc')

# 调用print(info 函数 )
print(info( 10 ) )
print(info( 70, 60, 50 ) )

# 可写函数说明 匿名函数
sum = lambda arg1, arg2: arg1 + arg2;

"""
import support
# 现在可以调用模块里包含的函数了
support.print(_func("Runoob") )
import fibonacci
#要导入模块 fib 的 fibonacci 函数，使用如下语句：
from fib import fibonacci
#这个声明不会把整个 fib 模块导入到当前的命名空间中，它只会将 fib 里的 fibonacci 单个引入到执行这个声明的模块的全局符号表。
#把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
from modname import *
from <filename> import <classname>

import template
te = template.Template

from template import *
te = Template

导入一个模块，Python 解析器对模块位置的搜索顺序是：
1、当前目录
2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。

1.如果导入的模块和主程序在同个目录下，直接import就行了

2.如果导入的模块是在主程序所在目录的子目录下，可以在子目录中增加一个空白的__init__.py文件，该文件使得python解释器将子目录整个也当成一个模块，然后直接通过“import 子目录.模块”导入即可。

3.如果导入的模块是在主程序所在目录的父目录下，则要通过修改path来解决，有两种方法：

(1)通过”import sys，sys.path.append('父目录的路径')“来改变，这种方法属于一次性的，只对当前的python解释器进程有效，关掉python重启后就失效了。

(2)直接修改环境变量：在windows中是 “ set 变量=‘路径’  ” 例如：set PYTHONPATH=‘C:\test\...’ 查看是否设置成功用echo %PYTHONPATH%,而且进到python解释器中查看sys.path,会发现已经有了新增加的路径了。这　种方式是永久的，一次设置以后一直都有效。在linux中是 "export 变量=‘路径’ “，查看是" echo $变量 "

通过修改path是通用的方法，因为python解释器就是通过sys.path去一个地方一个地方的寻找模块的。

"""
# 打印模块 所有函数和变量
import math
content = dir(math)
print( content )
"""
globals() 和 locals() 函数
根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。
如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。
两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。

当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。语法如下：
reload(module_name)

input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
"""

#文件处理
"""
# 打开一个文件
fo = open("foo.txt", "wb")
print( "文件名: ", fo.name )
print( "是否已关闭 : ", fo.closed )
print( "访问模式 : ", fo.mode )
print( "末尾是否强制加空格 : ", fo.softspace )

str = fo.read(10);
print( "读取的字符串是 : ", str )

# 查找当前位置
position = fo.tell();
print( "当前文件位置 : ", position )
 
# 把指针再次重新定位到文件开头
position = fo.seek(0, 0);

fo.write( "www.runoob.com!\nVery good site!\n");

fo.close();
#以上实例输出结果：
##文件名:  foo.txt
##是否已关闭 :  False
#访问模式 :  wb
#末尾是否强制加空格 :  0
"""

"""
import os
# 重命名文件test1.txt到test2.txt。
os.rename( "test1.txt", "test2.txt" )
os.remove(file_name)
os.mkdir("newdir")
os.rmdir('dirname')
# 将当前目录改为"/home/newdir"
os.chdir("/home/newdir")
#getcwd()方法显示当前的工作目录。
os.getcwd()
"""

#异常处理
"""
#抛出异常
raise Exception("Invalid level!", level)
        
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
try:
    return int(var)
except ValueError, Argument:
    print( "参数没有包含数字\n", Argument )
except Exception as e:
    print( '' )
else :
    print( '' )
"""

import sys;
x = ''''----test sys.stdout.write'''
sys.stdout.write(x + '\n');








# 输入 循环 随机数 猜数游戏
print( '----输入 循环 随机数 猜大小游戏' )
import random
m = -1;
s = int(random.uniform(1, 10));
while (m != s) :
  m = int ( input('input a unmber:'));
  if(m > s) :
    print('bigger');
  elif(m < s) :
    print('smaller');
  else :
    print('you win');
    break;





raw_input("\n\n Press the enter key to exit.");
print( "\nend----------------------" )
print( "////////////////////////" )





