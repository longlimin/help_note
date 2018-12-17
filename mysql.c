//启动mysql
d:/mysql/bin/mysqld 

//登录
mysql -u root -proot
mysql -uuser -ppasswd -e "show databases;"
// show
select USER(), version(),current_date();
SHOW DATABASES;
CREATE DATABASE mmm;
USE mmm
SHOW TABLES;
DESCRIBE mytable; 
desc student;
show table status like 'student';
//查看表create创建语句
show create table student;

//安全模式
safemode

//Backup 备份
mysqldump -uroot -proot student > student.sql;	//导出 导入
mysql -uroot -proot student < student.sql;	//~当前用户根root目录 /根目录
mysql -uroot -proot -e "show databases;"	

//Master/Slave  主备？ 数据库之间的同步 <异步处理>
grant file on *.* to 'root'@' 1222.122.1.1' identified by 'password';
grant replication master on *.* ....

相对路径定位到 自己的绝对路径


//mysql定位
/usr/local/Cellar/mysql/5.7.17	//mac
whereis mysql	//定位
locate mysql 
//授权登陆


//配置文件
my.cnf
	default_character=utf8
	[mysqld]
	long_query_time=2	//慢查询时间定义s 
	//5.5如下配置
	show-query-log=on
	show_uery_log_file="mysql_slow_query.log"

//主键自动索引pk > 数字索引index > 字符串索引index > 组合字段索引merge_index
explain select * from student where id = 12;	//explain sql-select
system > const > eq_ref > ref > fulltext > ref_or_null > index_merge > unique_subquery > index_subquery > range > index > all


	
//显示引擎 
//innorDB		行锁+表锁	事物  
//<MY>ISAM		表锁		
//表锁：开销小 加锁快 不会出现死锁
//行锁：开销大 加锁慢 会出现死锁 锁定力度小 发生锁冲突概率小
show engines;

set names utf8;
set character set utf8;
set collation_connection='utf8-general_ci';

//优化
slow query 慢查询统计
索引
缓存


//分页查询 oracle 采用rownum 而mysql使用limit 
select * from student limit 10;

NOT NULL auto_increment,


一.MYSQL的命令行模式的设置：
桌面->我的电脑->属性->环境变量->新建->
PATH="；path\mysql\bin;"其中path为MYSQL的安装路径。
二.简单的介绍一下命令行进入MYSQL的方法：
1.C:\>mysql -h hostname -u username -p
按ENTER键，等待然后输入密码。这里hostname为服务器的名称，如localhost，username为MYSQL的用户名，如root。
进入命令行后可以直接操作MYSQL了。
2.简单介绍一下MYSQL命令：
   mysql->CREATE DATABASE dbname;//创建数据库
   mysql->CREATE TABLE tablename;//创建表
   mysql->SHOW DATABASES;//显示数据库信息，有那些可用的数据库。
  mysql->USE dbname;//选择数据库
   mysql->SHOW TABLES;//显示表信息，有那些可用的表
   mysql->DESCRIBE tablename;//显示创建的表的信息
三.从数据库导出数据库文件：
1.将数据库mydb导出到e:\mysql\mydb.sql文件中：
打开开始->运行->输入cmd    进入命令行模式
c:\>mysqldump -h localhost -u root -p mydb >e:\mysql\mydb.sql
然后输入密码，等待一会导出就成功了，可以到目标文件中检查是否成功。
2.将数据库mydb中的mytable导出到e:\mysql\mytable.sql文件中：
c:\>mysqldump -h localhost -u root -p mydb mytable>e:\mysql\mytable.sql
3.将数据库mydb的结构导出到e:\mysql\mydb_stru.sql文件中：
c:\>mysqldump -h localhost -u root -p mydb --add-drop-table >e:\mysql\mydb_stru.sql
四.从外部文件导入数据到数据库中：
从e:\mysql\mydb2.sql中将文件中的SQL语句导入数据库中：
1.从命令行进入mysql，然后用命令CREATE DATABASE mydb2;创建数据库mydb2。
2.退出mysql 可以输入命令exit；或者quit；
3.在CMD中输入下列命令：
c:\>mysql -h localhost -u root -p mydb2 < e:\mysql\mydb2.sql
然后输入密码，就OK了。
五.下面谈一下关于导入文件大小限制问题的解决：
默认情况下：mysql 对导入文件大小有限制的，最大为2M，所以当文件很大时候，直接无法导入，下面就这个问题的解决列举如下：
1.在php.ini中修改相关参数：
影响mysql导入文件大小的参数有三个：
    memory_limit=128M,upload_max_filesize=2M,post_max_size=8M
修改upload_max_filesize=200 M  这里修改满足你需要的大小，
可以同时修改其他两项memory_limit=250M  post_max_size=200M
这样就可以导入200M以下的.sql文件了。


// 22、用重定向批处理方式使用MySQL:
首先建立一个批处理文件mytest.sql,内容如下：
use abccs;
select * from mytable;
select name,sex from mytable where name=‘abccs‘;
d:mysqlbin mysql < mytest.sql | more

//配置
mysql>show variables like 'max_connections';(查可以看当前的最大连接数)
msyql>set global max_connections=1000;(设置最大连接数为1000，可以再次查看是否设置成功)
mysql>exit(推出)
这种方式有个问题，就是设置的最大连接数只在mysql当前服务进程有效，一旦mysql重启，又会恢复到初始状态。因为mysql启动后的初始化工作是从其配置文件中读取数据的，而这种方式没有对其配置文件做更改。
第二种：修改配置文件。
这 种方式说来很简单，只要修改MySQL配置文件my.ini 或 my.cnf的参数max_connections，将其改为max_connections=1000，然后重启MySQL即可。但是有一点最难的就是my.ini这个文件在哪找。通常有两种可能，一个是在安装目录下（这是比较理想的情况），另一种是在数据文件的目录下，安装的时候如果没有人为改变目录的话，一般就在C:/ProgramData/MySQL往下的目录下。
