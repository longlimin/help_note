//登录
mysql -u root -proot
mysql -uuser -ppasswd -e "show databases;"

show databases;
user mysql;
show tables;
select * from User;	//数据库用户信息表 
update user set host = '%' where user = 'root';
update user set password<authentication_string> = pasword('ruaho1234") where user = 'root';
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

show databases;
use classdb;

create database classdb;
drop database classdb;

show tables;
select * frmo student;

//显示表字段
desc student;
show table status like 'student';
//查看表create创建语句
show create table student;


//优化
slow query 慢查询统计
索引
缓存


//分页查询 oracle 采用rownum 而mysql使用limit 
select * from student limit 10;



INSERT into person(p_id,p_name,p_sex,p_age) value("asdsadssdsadfff","addsdsa","dddd",113); 

NOT NULL auto_increment,
一.MYSQL的命令行模式的设置：
桌面->我的电脑->属性->环境变量->新建->
PATH=“；path\mysql\bin;”其中path为MYSQL的安装路径。
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

使用MySQL数据库的时候，经常会遇到这么一个问题，就是“Can not connect to MySQL server. Too many connections”-mysql 1040错误，这是因为访问MySQL且还未释放的连接数目已经达到MySQL的上限。通常，mysql的最大连接数默认是100, 最大可以达到16384。

     在Windows下常用的有两种方式修改最大连接数。

     第一种：命令行修改。

    >mysql -uuser -ppassword(命令行登录MySQL)

    mysql>show variables like 'max_connections';(查可以看当前的最大连接数)

    msyql>set global max_connections=1000;(设置最大连接数为1000，可以再次查看是否设置成功)

    mysql>exit(推出)

    这种方式有个问题，就是设置的最大连接数只在mysql当前服务进程有效，一旦mysql重启，又会恢复到初始状态。因为mysql启动后的初始化工作是从其配置文件中读取数据的，而这种方式没有对其配置文件做更改。

    第二种：修改配置文件。

   这 种方式说来很简单，只要修改MySQL配置文件my.ini 或 my.cnf的参数max_connections，将其改为max_connections=1000，然后重启MySQL即可。但是有一点最难的就是my.ini这个文件在哪找。通常有两种可能，一个是在安装目录下（这是比较理想的情况），另一种是在数据文件的目录下，安装的时候如果没有人为改变目录的话，一般就在C:/ProgramData/MySQL往下的目录下。

 

与连接数相关的几个参数：

     在修改最大连接数的时候会有这样一个疑问—这个值是不是越大越好，或者设置为多大才合适？这个参数的大小要综合很多因素来考虑，比如使用的平台所支持的线程库数量（windows只能支持到2048）、服务器的配置（特别是内存大小）、每个连接占用资源（内存和负载）的多少、系统需要的响应时间等。可以在global或session范围内修改这个参数。连接数的增加会带来很多连锁反应，需要在实际中避免由此引发的负面影响。 




/statement语句执行 只支持静态sql语句 如此
//	Statement s = c.createStatement(); 
//	s.executeUpdate( "create database if not exists " + this.DBName + " default charset=gbk;");
//而preparedStatement支持动态sql语句 如此先添加静态sql 再填充参数数据
//	pstmt = (PreparedStatement) conn.prepareStatement
//	("insert into "+ TName+ " (name, type,  timeIn, timeChange, timeLength, singer, ablum)
//	values(?,?,?,?,?,?,?)"); 每个问好对应一个数据必须设置
//	 之后再必须设置每一个列的所需数据 缺一不可
//	pstmt.setString(1, "" + data.name); // 设置数据
//	pstmt.setString(2, "" + data.type); // 设置数据



1、启动MySQL服务器
实际上上篇已讲到如何启动MySQL。两种方法：
一是用winmysqladmin，如果机器启动时已自动运行，则可直接进入下一步操作。
二是在DOS方式下运行
?d:/mysql/bin/mysqld

2、进入mysql交互操作界面
在DOS方式下，运行：
d:/mysql/bin/mysql -u root -p
?出现提示符，此时已进入mysql的交互操作方式。
如果出现 "ERROR 2003: Can‘t connect to MySQL server on ‘localhost‘ (10061)“，说明你的MySQL还没有启动。

3、退出MySQL操作界面
?在mysql>提示符下输入quit可以随时退出交互操作界面：
mysql> quit
Bye
你也可以用control-D退出。

4、第一条命令
mysql> select version(),current_date();
+----------------+-----------------+
| version() ? | current_date() |
+----------------+-----------------+
| 3.23.25a-debug | 2001-05-17 ? |
+----------------+-----------------+
1 row in set (0.01 sec)

此命令要求mysql服务器告诉你它的版本号和当前日期。尝试用不同大小写操作上述命令，看结果如何。
结果说明mysql命令的大小写结果是一致的。
练习如下操作：
mysql>Select (20+5)*4;
mysql>Select (20+5)*4,sin(pi()/3);
mysql>Select (20+5)*4 AS Result,sin(pi()/3); (AS: 指定假名为Result)

5、多行语句
一条命令可以分成多行输入，直到出现分号“；”为止：
mysql> select
? -> USER()
? -> ,
? -> now()
? ->;
+--------------------+-----------------------------+
| USER() ? ? ???????? ?| now() ?????????? ? ? ?????????? |
+--------------------+-----------------------------+
| ODBC@localhost| 2001-05-17 22:59:15? |
+--------------------+-----------------------------+

6、使用SHOW语句找出在服务器上当前存在什么数据库：

mysql> SHOW DATABASES;
+----------+
| Database |
+----------+
| mysql ?|
| test ? |
+----------+
3 rows in set (0.00 sec)

7、创建一个数据库abccs
mysql> CREATE DATABASE abccs;
注意不同操作系统对大小写的敏感。

8、选择你所创建的数据库
mysql> USE abccs
Database changed
此时你已经进入你刚才所建立的数据库abccs.

9、 创建一个数据库表
首先看现在你的数据库中存在什么表：
mysql> SHOW TABLES;
Empty set (0.00 sec)
说明刚才建立的数据库中还没有数据库表。下面来创建一个数据库表mytable:

我们要建立一个你公司员工的生日表，表的内容包含员工姓名、性别、出生日期、出生城市。
mysql> CREATE TABLE mytable (name VARCHAR(20), sex CHAR(1),
-> birth DATE, birthaddr VARCHAR(20));
Query OK, 0 rows affected (0.00 sec)

由于name、birthadd的列值是变化的，因此选择VARCHAR，其长度不一定是20。可以选择从
1到255的任何长度，如果以后需要改变它的字长，可以使用ALTER TABLE语句。）;
性别只需一个字符就可以表示："m"或"f"，因此选用CHAR(1);
birth列则使用DATE数据类型。

创建了一个表后，我们可以看看刚才做的结果，用SHOW TABLES显示数据库中有哪些表：
mysql> SHOW TABLES;
+---------------------+
| Tables in menagerie |
+---------------------+
| mytables ? ? ?|
+---------------------+

10、显示表的结构：
mysql> DESCRIBE mytable;
+-------------+-------------+------+-----+---------+-------+
| Field ? ?| Type ? ?| Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| name ? ?| varchar(20) | YES | ? | NULL ?| ? ?|
| sex ? ? | char(1) ? | YES | ? | NULL ?| ? ?|
| birth ? ?| date ? ?| YES | ? | NULL ?| ? ?|
| deathaddr ?| varchar(20) | YES | ? | NULL ?| ? ?|
+-------------+-------------+------+-----+---------+-------+

11、查询所有数据：
mysql> select * from mytable;
+----------+------+------------+----------+
| name ? | sex | birth ? | birthaddr |
+----------+------+------------+--------+
| abccs ?|f ?| 1977-07-07 | china ? |
| mary ? |f ?| 1978-12-12 | usa ? ?|
| tom ? |m ?| 1970-09-02 | usa ? ?|
+----------+------+------------+----------+
3 row in set (0.00 sec)

12、修正错误记录：
假如tom的出生日期有错误，应该是1973－09－02，则可以用update语句来修正：
mysql> update mytable set birth = "1973-09-02" where name = "tom";
再用2中的语句看看是否已更正过来。

13、选择特定行
上面修改了tom的出生日期，我们可以选择tom这一行来看看是否已经有了变化：
mysql> select * from mytable where name = "tom";
+--------+------+------------+------------+
| name ?|sex | birth ? | birthaddr ? ? |
+--------+------+------------+------------+
| tom ?|m ?| 1973-09-02 | usa ? ?|
+--------+------+------------+------------+
1 row in set (0.06 sec)

上面WHERE的参数指定了检索条件。我们还可以用组合条件来进行查询：
mysql> SELECT * FROM mytable WHERE sex = "f" AND birthaddr = "china";
+--------+------+------------+------------+
| name ?|sex | birth ? | birthaddr ? ? |
+--------+------+------------+------------+
| abccs |f ?| 1977-07-07 | china ? |
+--------+------+------------+------------+
1 row in set (0.06 sec)

14、?多表操作

前面我们熟悉了数据库和数据库表的基本操作，现在我们再来看看如何操作多个表。

在一个数据库中，可能存在多个表，这些表都是相互关联的。我们继续使用前面的例子。前面建立的表中包含了员工的一些基本信息，如姓名、性别、出生日期、出生地。我们再创建一个表，该表用于描述员工所发表的文章，内容包括作者姓名、文章标题、发表日期。

1、查看第一个表mytable的内容：
mysql> select * from mytable;
+----------+------+------------+-----------+
| name ? | sex | birth ? | birthaddr |
+----------+------+------------+-----------+
| abccs ?|f ? | 1977-07-07 | china ? |
| mary ? |f ? | 1978-12-12 | usa ? ?|
| tom ? |m ? | 1970-09-02 | usa ? ?|
+----------+------+------------+-----------+

2、创建第二个表title（包括作者、文章标题、发表日期）:
mysql> create table title(writer varchar(20) not null,
-> title varchar(40) not null,
-> senddate date);

向该表中填加记录，最后表的内容如下：
mysql> select * from title;
+--------+-------+------------+
| writer | title | senddate ?|
+--------+-------+------------+
| abccs | a1 ?| 2000-01-23 |
| mary ?| b1 ?| 1998-03-21 |
| abccs | a2 ?| 2000-12-04 |
| tom ?| c1 ?| 1992-05-16 |
| tom ?| c2 ?| 1999-12-12 |
+--------+-------+------------+
5 rows in set (0.00sec)

3、多表查询
现在我们有了两个表: mytable 和 title。利用这两个表我们可以进行组合查询：
例如我们要查询作者abccs的姓名、性别、文章：
mysql> SELECT name,sex,title FROM mytable,title
-> WHERE name=writer AND name=‘abccs‘;
+-------+------+-------+
| name | sex | title |
+-------+------+-------+
| abccs | f ?| a1 ?|
| abccs | f ?| a2 ?|
+-------+------+-------+

上面例子中，由于作者姓名、性别、文章记录在两个不同表内，因此必须使用组合来进行查询。必须要指定一个表中的记录如何与其它表中的记录进行匹配。

注意：如果第二个表title中的writer列也取名为name（与mytable表中的name列相同）而不是writer时，就必须用mytable.name和title.name表示，以示区别。

再举一个例子，用于查询文章a2的作者、出生地和出生日期：
mysql> select title,writer,birthaddr,birth from mytable,title
-> where mytable.name=title.writer and title=‘a2‘;
+-------+--------+-----------+------------+
| title | writer | birthaddr | birth ? |
+-------+--------+-----------+------------+
| a2 ?| abccs | china ? | 1977-07-07 |
+-------+--------+-----------+------------+

15、增加一列：
如在前面例子中的mytable表中增加一列表示是否单身single:
mysql> alter table mytable add column single char(1);

16、修改记录
将abccs的single记录修改为“y”：
mysql> update mytable set single=‘y‘ where name=‘abccs‘;

现在来看看发生了什么：
mysql> select * from mytable;
+----------+------+------------+-----------+--------+
| name ? | sex | birth ? | birthaddr | single |
+----------+------+------------+-----------+--------+
| abccs ?|f ? | 1977-07-07 | china ? | y ? |
| mary ? |f ? | 1978-12-12 | usa ? ?| NULL ?|
| tom ? |m ? | 1970-09-02 | usa ? ?| NULL ?|
+----------+------+------------+-----------+--------+

17、增加记录
前面已经讲过如何增加一条记录，为便于查看，重复与此：
mysql> insert into mytable
-> values (‘abc‘,‘f‘,‘1966-08-17‘,‘china‘,‘n‘);
Query OK, 1 row affected (0.05 sec)
查看一下：
mysql> select * from mytable;
+----------+------+------------+-----------+--------+
| name ? | sex | birth ? | birthaddr | single |
+----------+------+------------+-----------+--------+
| abccs ?|f ? | 1977-07-07 | china ? | y ? |
| mary ? |f ? | 1978-12-12 | usa ? ?| NULL ?|
| tom ? |m ? | 1970-09-02 | usa ? ?| NULL ?|
| abc ? |f ? | 1966-08-17 | china ? | n ? |
+----------+------+------------+-----------+--------+

18、删除记录
用如下命令删除表中的一条记录：
mysql> delete from mytable where name=‘abc‘;
DELETE从表中删除满足由where给出的条件的一条记录。

再显示一下结果：
mysql> select * from mytable;
+----------+------+------------+-----------+--------+
| name ? | sex | birth ? | birthaddr | single |
+----------+------+------------+-----------+--------+
| abccs ?|f ? | 1977-07-07 | china ? | y ? |
| mary ? |f ? | 1978-12-12 | usa ? ?| NULL ?|
| tom ? |m ? | 1970-09-02 | usa ? ?| NULL ?|
+----------+------+------------+-----------+--------+

19、删除表：
mysql> drop table ****(表1的名字)，***表2的名字;
可以删除一个或多个表，小心使用。

20、数据库的删除：
mysql> drop database 数据库名;
小心使用。

21、数据库的备份：
退回到DOS：
mysql> quit
d:mysqlbin
使用如下命令对数据库abccs进行备份：
mysqldump --opt abccs>abccs.dbb
abccs.dbb就是你的数据库abccs的备份文件。

22、用批处理方式使用MySQL:

首先建立一个批处理文件mytest.sql,内容如下：
use abccs;
select * from mytable;
select name,sex from mytable where name=‘abccs‘;

在DOS下运行如下命令：
d:mysqlbin mysql < mytest.sql
在屏幕上会显示执行结果。

如果想看结果，而输出结果很多，则可以用这样的命令：
mysql < mytest.sql | more

我们还可以将结果输出到一个文件中：
mysql < mytest.sql > mytest.out

23. 请先用root登录到mysql,方法：
?c:/mysql/bin/mysql -u root -p ?
24.创建一个用户
?mysql> GRANT ALL PRIVILEGES ON javatest.* TO javauser@"%" ?
? ? ?-> ? IDENTIFIED BY "javadude" ;


