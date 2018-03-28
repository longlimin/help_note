D:\oracle\product\11.2.0\dbhome_1\NETWORK\ADMIN\SAMPLE
 

64位oracle安装，安装oracle xe，安装plsql，移动oci32 ，配置 oci dll 
E:\Oracle\instantclient_10_2
E:\oracle\instantclient_10_2\oci.dll 
localhost:1521/xe

sqlplus /nolog
登陆sysdba：conn  /  as sysdba;

//登录方式2
sqlplus /nolog
sys as sysdba


创建用户：create user walker identified by qwer; 
授予登陆和常用角色权限：grant connect, resource to walker
grant create view to walker ; //视图权限
查看所有用户：
select username from dba_users;
select * from all_users;
select * from user_users;
中文编码-环境变量
NLS_LANG
SIMPLIFIED CHINESE_CHINA.ZHS16GBK

加字段的语法：alter table tablename add (column datatype [default value][null/not null],….);
修改字段的语法：alter table tablename modify (column datatype [default value][null/not null],….);
删除字段的语法：alter table tablename drop (column); 
添加、修改、删除多列的话，用逗号隔开。
使用alter table 来增加、删除和修改一个列的例子。


exp walker/walker@XE file=F:\sql\daochu.dmp owner=(walker)

FOREIGN  KEY  (Sno)  REFERENCES  S(Sno) , FOREIGN  KEY  (Cno)  REFERENCES  C(Cno) )
ALTER TABLE  books ADD CONSTRAINT FK_Book_categoryid FOREIGN KEY(categoryId ) REFERENCES Category(id);

端口冲突问题
begin  
   dbms_xdb.sethttpport('8081');  
   dbms_xdb.setftpport('0');  
end;  
/   
 这样就把端口设置为8081了。



dbca  数据库管理
netca 监听管理

//删除数据库 报错 nt问题
权限管理员cmd执行dbca即可

//中文乱码问题
修改方法（以改成UTF8为例）
以系统DBA权限登录sqlplus

$ sqlplus / as sysdba;
select userenv('language') from dual;
　　　如果是：AMERICAN_AMERICA.WE8MSWIN1252  则需要调整编码格式为：AL32UTF8
SQL> shutdown immediate;
SQL> startup mount;
SQL> alter system enable restricted session;
SQL> alter system set job_queue_processes=0;
SQL> alter database open;
SQL> alter database character set internal_use AL32UTF8;
SQL> shutdown immediate;
SQL> startup
SQL>alter system disable restricted session;



1. 复制表结构及其数据： 
create table table_name_new as select * from table_name_old 
2. 只复制表结构： 
create table table_name_new as select * from table_name_old where 1=2; 
create table table_name_new like table_name_old 
3. 只复制表数据： 
如果两个表结构一样： 
insert into table_name_new select * from table_name_old 
如果两个表结构不一样： 
insert into table_name_new(column1,column2...) select column1,column2... from table_name_old
 

--定长位数补齐
 select 'SCJS' || lpad(SEQ_T_CONTRACT_THREE.nextval,3, '0') from dual 
 --序列创建
create sequence SEQ_T_CONTRACT_THREE
minvalue 1
maxvalue 999
start with 1
increment by 1
cache 20;
1、给用户解锁 
alter user scott account unlock; 
2、注销、断开、切换当前用户连接 
quit
conn scott/tiger
 3、用户权限查询
A .查看所有用户：
select * from dba_users;
select * from all_users;
select * from user_users;
B.查看用户或角色系统权限(直接赋值给用户或角色的系统权限)：
select * from dba_sys_privs;
select * from user_sys_privs;
C.查看角色(只能查看登陆用户拥有的角色)所包含的权限
select * from role_sys_privs;
D.查看用户对象权限：
select * from dba_tab_privs;
select * from all_tab_privs;
select * from user_tab_privs;
E.查看所有角色：
select * from dba_roles;
F.查看用户或角色所拥有的角色：
select * from dba_role_privs; s
elect * from user_role_privs;
G.查看哪些用户有sysdba或sysoper系统权限(查询时需要相应权限)
select * from V$PWFILE_USERS
4、用户管理
A、创建用户
create user username identified by password;
create user username identified by password default tablespace users quota 10M on users;
B、修改密码
alter user username identified by pass;
密码就从password改成pass了；同样登陆后输入password也可以修改密码
C、删除用户
drop user username;
drop user username cascade;

大多情况都可以用Oracle数据导入导出完成数据的备份和还原（不会造成数据的丢失）。
 Oracle有个好处，虽然你的电脑不是服务器，但是你装了oracle客户端，并建立了连接
 （通过Net Configuration Assistant添加正确的服务命名，其实你可以想成是客户端与服务器端 修了条路，然后数据就可以被拉过来了）
 这样你可以把数据导出到本地，虽然可能服务器离你很远。
 你同样可以把dmp文件从本地导入到远处的数据库服务器中。
 利用这个功能你可以构建俩个相同的数据库，一个用来测试，一个用来正式使用。
 
执行环境：可以在SQLPLUS.EXE或者DOS（命令行）中执行，
 DOS中可以执行时由于 在oracle 8i 中  安装目录\$ora10g\BIN被设置为全局路径，
 该目录下有EXP.EXE与IMP.EXE文件被用来执行导入导出。
 oracle用java编写，我想SQLPLUS.EXE、EXP.EXE、IMP.EXE这俩个文件是被包装后的类文件。
 SQLPLUS.EXE调用EXP.EXE、IMP.EXE他们所包裹的类，完成导入导出功能。
 
下面介绍的是导入导出的实例，向导入导出看实例基本上就可以完成，因为导入导出很简单。
数据导出：
 1 将数据库TEST完全导出,用户名system 密码manager 导出到D:\daochu.dmp中
   exp system/manager@TEST file=d:\daochu.dmp  
 2 将数据库中system用户与sys用户的表导出
   exp system/manager@TEST file=d:\daochu.dmp owner=(system,sys)
 3 将数据库中的表table1 、table2导出
   exp system/manager@TEST file=d:\daochu.dmp tables=(table1,table2) 
 4 将数据库中的表table1中的字段filed1以"00"打头的数据导出
   exp system/manager@TEST file=d:\daochu.dmp tables=(table1) query=\" where filed1 like  '00%'\"
       上面是常用的导出，对于压缩我不太在意，用winzip把dmp文件可以很好的压缩。
                     不过在上面命令后面 加上 compress=y  就可以了
数据的导入
 1 将D:\daochu.dmp 中的数据导入 TEST数据库中。
   imp system/manager@TEST  file=d:\daochu.dmp full=y
   上面可能有点问题，因为有的表已经存在，然后它就报错，对该表就不进行导入。
   在后面加上 ignore=y 就可以了。
 2 将d:\daochu.dmp中的表table1 导入
 imp system/manager@TEST  file=d:\daochu.dmp  tables=(table1) 
  基本上上面的导入导出够用了。不少情况我是将表彻底删除，然后导入。
 注意：
 你要有足够的权限，权限不够它会提示你。
 数据库时可以连上的。可以用tnsping TEST 来获得数据库TEST能否连上。
 
数据导出：
exp hkb/hkb@boss_14 full=y file=c:\orabackup\hkbfull.dmp log=c:\orabackup\hkbfull.log;

导出注意事项：导出的是当前用户的的数据，当前用户如果有DBA的权限，则导出所有数据！
同名用户之间的数据导入：
imp hkb/hkb@xe  file=c:\orabackup\hkbfull.dmp log=c:\orabackup\hkbimp.log full=y
不同名之间的数据导入：
imp system/test@xe fromuser=hkb touser=hkb_new file=c:\orabackup\hkbfull.dmp
log=c:\orabackup\hkbimp.log;

to_date("要转换的字符串","转换的格式")   两个参数的格式必须匹配，否则会报错。
即按照第二个参数的格式解释第一个参数。
to_char(日期,"转换格式" ) 即把给定的日期按照“转换格式”转换。
转换的格式：
表示year的：y 表示年的最后一位 yy 表示年的最后2位 yyy 表示年的最后3位 yyyy 用4位数表示年
表示month的：mm 用2位数字表示月；mon 用简写形式 比如11月或者nov ；month 用全称 比如11月或者november
表示day的：dd 表示当月第几天；ddd表示当年第几天；dy 当周第几天 简写 比如星期五或者fri；day当周第几天 全写
比如星期五或者friday。
表示hour的：hh 2位数表示小时 12进制； hh24 2位数表示小时 24小时
表示minute的：mi 2位数表示分钟
表示second的：ss 2位数表示秒 60进制
表示季度的：q 一位数 表示季度 （1-4）
另外还有ww 用来表示当年第几周 w用来表示当月第几周。
24小时制下的时间范围：00：00：00-23：59：59
12小时制下的时间范围：1：00：00-12：59：59
比如：
select to_char(sysdate,'yy-mm-dd hh24:mi:ss') from dual   //显示：08-11-07 13:22:42
select to_date('2005-12-25,13:25:59','yyyy-mm-dd,hh24:mi:ss') from dual //显示：2005-12-25 13:25:59
而如果把上式写作：select to_date('2005-12-25,13:25:59','yyyy-mm-dd,hh:mi:ss') from dual，则会报错，因为小时hh是12进制，13为非法输入，不能匹配。
补充：
当前时间减去7分钟的时间 
select sysdate,sysdate - interval '7' MINUTE from dual 
当前时间减去7小时的时间 
select sysdate - interval '7' hour from dual 
当前时间减去7天的时间 
select sysdate - interval ’7’ day from dual 
当前时间减去7月的时间 
select sysdate,sysdate - interval '7' month from dual 
当前时间减去7年的时间 
select sysdate,sysdate - interval '7' year from dual 
时间间隔乘以一个数字 
select sysdate,sysdate - 8*interval '7' hour from dual

Oracle Express Edition(XE)默认的http端口是8080，这跟JBoss/Tomcat的默认端口相同，导致Jboss启动冲突。
修改办法：
1. 以dba身份登录XE
2. 执行下列语句
1 begin
2   dbms_xdb.sethttpport('7000');
3   dbms_xdb.setftpport('0');
4 end;
5 /
这样就把默认的8080端口改成7000了，不用重启oracle服务，即时生效!
3.修改下面二个internet快捷方式(位于oraclexe安装目录的product\11.2.0\server下)
X:\oraclexe\app\oracle\product\11.2.0\server\Get_Started.url
X:\oraclexe\app\oracle\product\11.2.0\server\Database_homepage.url
用记事本打开这二个文件，把8080换成7000

grant select on Scott.dept to Bob ;
> revoke select on dept from Emi;
grant select on Scott.dept to Emi with grant option;Scott 的身份重新连接，并赋予 Emi 从 Scott 的 DEPT 表中进行选择的
能力。此外，使 Emi 能向其他用户赋予选择权限。 
alter user Bob quota unlimited on users;
select constraint_name from dba_constraints where owner=... and table_name=

3. 分别在 customers、orders 表上建立约束 
ALTER TABLE customers 
  ADD CONSTRAINT pk_cust PRIMARY KEY (cust_code); 
ALTER TABLE orders 
  ADD CONSTRAINT pk_ord PRIMARY KEY (ord_id); 
ALTER TABLE orders 
  ADD CONSTRAINT fk_ord_cust FOREIGN KEY (cust_code)  
  REFERENCES customers(cust_code) DISABLE NOVALIDATE; 


Oracle 创建用户 修改用户密码 授权命令
create user [username] identified by [password] 创建新的用户 
grant 权限1、权限2...to 用户  给创建用户权限 
ex:grant create session to [username] 此时只能连接到数据库 
grant connect,resource to [username] 此时权限能满足要求 
alter user [username] identified by [password] 修改用户密码 
alter user [username] password expire￥######### 下次登录时提示修改密码 
alter user [username] account lock  锁住用户 
alter user [username] account unlock  解锁锁用户 
grant select,delete on scott.emp to [username] 把scott下emp表的两个权限给用户 
revoke select ,delete on scott.emo from [username] 回收权限 
 
在进行procedure执行的时候，用的是PL/SQL工具中的test，调试方法进行执行，因为有输入参数，但是报了个错：
“note:debugging requires the debug connect session system privilege”.

原因是用户权限不够，使用以下命令授予权限：
GRANT debug any procedure, debug connect session TO username
其实只需要授予debug connect session 就可以了，已经过测试。
  
创建用户、表、表空间、权限  解决oracle更新时间问题.  alter session set nls_date_format = 'yyyy-mm-dd hh24:mi:ss';   oracle 创建用户,表空间  drop user ymsuser cascade;  --- 删除用户 
  创建临时表空间    CREATE TEMPORARY TABLESPACE test_temp   TEMPFILE 'D:\app\oradata\daheng\test_temp01.dbf'  SIZE 32M   AUTOEXTEND ON   NEXT 32M MAXSIZE 2048M  EXTENT MANAGEMENT LOCAL;
 创建用户表空间    CREATE TABLESPACE YMSDB  LOGGING   DATAFILE 'D:\app\oradata\daheng\YMSDB.dbf'  SIZE 32M   AUTOEXTEND ON   NEXT 32M MAXSIZE 2048M  EXTENT MANAGEMENT LOCAL;
 创建用户并制定表空间   
CREATE USER ymsuser IDENTIFIED BY ymsuser  DEFAULT TABLESPACE YMSDB   TEMPORARY TABLESPACE TEST_TEMP; 给用户授予权限
  GRANT     CREATE SESSION, CREATE ANY TABLE, CREATE ANY VIEW ,CREATE ANY INDEX, CREATE ANY PROCEDURE,     ALTER ANY TABLE, ALTER ANY PROCEDURE,     DROP ANY TABLE, DROP ANY VIEW, DROP ANY INDEX, DROP ANY PROCEDURE,     SELECT ANY TABLE, INSERT ANY TABLE, UPDATE ANY TABLE, DELETE ANY TABLE ,resource,connect    TO ymsuser;  将role这个角色授与ymsuser,也就是说，使ymsuser这个用户可以管理和使用role所拥有的资源   GRANT role TO ymsuser; 
  -----------------------------------------------查看用户权限---------------------------------------------------------   查看所有用户    SELECT * FROM DBA_USERS;  SELECT * FROM ALL_USERS;  SELECT * FROM USER_USERS; 查看用户系统权限    SELECT * FROM DBA_SYS_PRIVS;  SELECT * FROM USER_SYS_PRIVS; 查看用户对象或角色权限    SELECT * FROM DBA_TAB_PRIVS;  SELECT * FROM ALL_TAB_PRIVS;  SELECT * FROM USER_TAB_PRIVS; 查看所有角色    SELECT * FROM DBA_ROLES; 查看用户或角色所拥有的角色    SELECT * FROM DBA_ROLE_PRIVS;  SELECT * FROM USER_ROLE_PRIVS;
  1、用户 
            查看当前用户的缺省表空间 
            SQL>select username,default_tablespace from user_users; 
        查看当前用户的角色 
        SQL>select * from user_role_privs; 
        查看当前用户的系统权限和表级权限 
        SQL>select * from user_sys_privs; 
        SQL>select * from user_tab_privs; 
    2、表 
            查看用户下所有的表 
            SQL>select * from user_tables; 
            查看名称包含log字符的表 
            SQL>select object_name,object_id from user_objects 
                where instr(object_name,'LOG')>0; 
            查看某表的创建时间 
            SQL>select object_name,created from user_objects where object_name=upper('&table_name'); 
            查看某表的大小 
            SQL>select sum(bytes)/(1024*1024) as "size(M)" from user_segments 
                where segment_name=upper('&table_name'); 
            查看放在ORACLE的内存区里的表 
            SQL>select table_name,cache from user_tables where instr(cache,'Y')>0; 
 5、三种标准的角色（role）：CONNECT、RESOURCE和DBA。
I、Connect连接、登陆权限
II、Resource可以创建表、序列、过程（procedure）、触发器（trigger）、索引（index）和簇（cluster）。
III、Dba管理员
10、Sqlplus常用命令
A、set lineSize 120可以设置sqlplus的显示缓冲区大小；
B、set pageSize 20 可以设置每页显示大小
C、edit 可以编辑当前sql语句，保存后输入/回车运行
D、spool c:/temp.sql; 和 spool off 可以保存之间所有的显示内容；
E、start [filepath]可以批量执行sql语句；
F、desc tableName 可以查看指定表结构
G、 show user 可以查看当前用户
H、 set serveroutput on 运行dbms_output输出信息
I、 show error 查看编译错误信息
一、ORACLE的启动和关闭 
1、在单机环境下 
要想启动或关闭ORACLE系统必须首先切换到ORACLE用户，如下 
su - oracle 
a、启动ORACLE系统 
oracle>svrmgrl 
SVRMGR>connect internal 
SVRMGR>startup 
SVRMGR>quit 
b、关闭ORACLE系统 
oracle>svrmgrl 
SVRMGR>connect internal 
SVRMGR>shutdown 
SVRMGR>quit 
启动oracle9i数据库命令： 
$ sqlplus /nolog 
SQL*Plus: Release 9.2.0.1.0 - Production on Fri Oct 31 13:53:53 2003 
Copyright (c) 1982, 2002, Oracle Corporation.  All rights reserved. 

SQL> connect / as sysdba  
Connected to an idle instance. 
SQL> startup^C 

SQL> startup 
ORACLE instance started. 
2、在双机环境下 
要想启动或关闭ORACLE系统必须首先切换到root用户，如下 
su － root 
a、启动ORACLE系统 
hareg －y oracle 
b、关闭ORACLE系统 
hareg －n oracle 
Oracle数据库有哪几种启动方式 
三、查看数据库的SQL 
1、查看表空间的名称及大小 
    select t.tablespace_name, round(sum(bytes/(1024*1024)),0) ts_size 
    from dba_tablespaces t, dba_data_files d 
    where t.tablespace_name = d.tablespace_name 
    group by t.tablespace_name; 
2、查看表空间物理文件的名称及大小 
    select tablespace_name, file_id, file_name, 
    round(bytes/(1024*1024),0) total_space 
    from dba_data_files 
    order by tablespace_name; 
3、查看回滚段名称及大小 

    select segment_name, tablespace_name, r.status, 
    (initial_extent/1024) InitialExtent,(next_extent/1024) NextExtent, 
    max_extents, v.curext CurExtent 
    From dba_rollback_segs r, v$rollstat v 
    Where r.segment_id = v.usn(+) 
    order by segment_name ; 
4、查看控制文件 
    select name from v$controlfile; 
5、查看日志文件 
    select member from v$logfile; 
6、查看表空间的使用情况 
    select sum(bytes)/(1024*1024) as free_space,tablespace_name 
    from dba_free_space 
    group by tablespace_name; 

    SELECT A.TABLESPACE_NAME,A.BYTES TOTAL,B.BYTES USED, C.BYTES FREE, 
    (B.BYTES*100)/A.BYTES "% USED",(C.BYTES*100)/A.BYTES "% FREE" 
    FROM SYS.SM$TS_AVAIL A,SYS.SM$TS_USED B,SYS.SM$TS_FREE C 
    WHERE A.TABLESPACE_NAME=B.TABLESPACE_NAME AND A.TABLESPACE_NAME=C.TABLESPACE_NAME; 

7、查看数据库库对象 
    select owner, object_type, status, count(*) count# from all_objects group by owner, object_type, status; 
8、查看数据库的版本 
    Select version FROM Product_component_version 
    Where SUBSTR(PRODUCT,1,6)='Oracle'; 
9、查看数据库的创建日期和归档方式 
    Select Created, Log_Mode, Log_Mode From V$Database; 
四、ORACLE用户连接的管理 
用系统管理员，查看当前数据库有几个用户连接： 
SQL> select username,sid,serial# from v$session; 
如果要停某个连接用 
SQL> alter system kill session 'sid,serial#'; 
如果这命令不行,找它UNIX的进程数 
SQL> select pro.spid from v$session ses,v$process pro where ses.sid=21 and ses.paddr=pro.addr; 
说明：21是某个连接的sid数 
然后用 kill 命令杀此进程号。 
 
ALTER TABLE 表名 
MODIFY （列名 数据类型） 
例：将test表中的Count列宽度加长为10个字符 
    sql>alter atble test 
        modify （County char(10)）； 

b、将一张表删除语句的格式如下： 
DORP TABLE 表名； 
例：表删除将同时删除表的数据和表的定义 
sql>drop table test 
c、表空间的创建、删除 

六、ORACLE逻辑备份的SH文件 
完全备份的SH文件：exp_comp.sh 
rq=` date +"%m%d" ` 
su - oracle -c "exp system/manager full=y inctype=complete file=/oracle/export/db_comp$rq.dmp" 
累计备份的SH文件：exp_cumu.sh 
rq=` date +"%m%d" ` 
su - oracle -c "exp system/manager full=y inctype=cumulative file=/oracle/export/db_cumu$rq.dmp" 
增量备份的SH文件: exp_incr.sh 
rq=` date +"%m%d" ` 
su - oracle -c "exp system/manager full=y inctype=incremental file=/oracle/export/db_incr$rq.dmp" 
root用户crontab文件 
/var/spool/cron/crontabs/root增加以下内容 
0 2 1 * * /oracle/exp_comp.sh 
30 2 * * 0-5 /oracle/exp_incr.sh 
45 2 * * 6 /oracle/exp_cumu.sh 
当然这个时间表可以根据不同的需求来改变的，这只是一个例子。 

2.ALTER        (改变表, 索引, 视图等) 
改变表的名称 
ALTER TABLE 表名1  TO 表名2; 
在表的后面增加一个字段 
ALTER TABLE表名 ADD 字段名 字段名描述; 
修改表里字段的定义描述 
ALTER TABLE表名 MODIFY字段名 字段名描述; 
给表里的字段加上约束条件 
ALTER TABLE 表名 ADD CONSTRAINT 约束名 PRIMARY KEY (字段名); 
ALTER TABLE 表名 ADD CONSTRAINT 约束名 UNIQUE (字段名); 
把表放在或取出数据库的内存区 
ALTER TABLE 表名 CACHE; 
ALTER TABLE 表名 NOCACHE; 
4.TRUNCATE (清空表里的所有记录, 保留表的结构) 

TRUNCATE 表名; 
三.查询语句 (SELECT) 部分 
SELECT字段名1, 字段名2, …… FROM 表名1, [表名2, ……] WHERE 条件; 
字段名可以带入函数 
  例如:  COUNT(*), MIN(字段名),  MAX(字段名),  AVG(字段名), DISTINCT(字段名), 
           TO_CHAR(DATE字段名,'YYYY-MM-DD HH24:MI:SS') 
NVL(EXPR1, EXPR2)函数 
解释: 
IF EXPR1=NULL 
                RETURN EXPR2 
ELSE 
                       RETURN EXPR1 
DECODE(AA﹐V1﹐R1﹐V2﹐R2....)函数 
解释: 
IF AA=V1 THEN RETURN R1 
IF AA=V2 THEN RETURN R2 
..… 
ELSE 
RETURN NULL 
LPAD(char1,n,char2)函数 
解释: 
字符char1按制定的位数n显示，不足的位数用char2字符串替换左边的空位 

分组查询 
SELECT字段名1, 字段名2, …… FROM 表名1, [表名2, ……] GROUP BY字段名1 
[HAVING 条件] ; 
两个以上表之间的连接查询 
SELECT字段名1, 字段名2, …… FROM 表名1, [表名2, ……] WHERE 
                表名1.字段名 = 表名2. 字段名 [ AND ……] ; 
SELECT字段名1, 字段名2, …… FROM 表名1, [表名2, ……] WHERE 
                表名1.字段名 = 表名2. 字段名(+) [ AND ……] ; 
有(+)号的字段位置自动补空值 

查询结果集的排序操作, 默认的排序是升序ASC, 降序是DESC 
SELECT字段名1, 字段名2, …… FROM 表名1, [表名2, ……] 
ORDER BY字段名1, 字段名2 DESC; 
字符串模糊比较的方法 
INSTR(字段名, ‘字符串’)>0 
字段名 LIKE  ‘字符串%’  [‘%字符串%’] 
每个表都有一个隐含的字段ROWID, 它标记着记录的唯一性. 
四.ORACLE里常用的数据对象 (SCHEMA) 
1.索引 (INDEX) 
CREATE INDEX 索引名ON 表名 ( 字段1, [字段2, ……] ); 
ALTER INDEX 索引名 REBUILD; 
一个表的索引最好不要超过三个 (特殊的大表除外), 最好用单字段索引, 结合SQL语句的分析执行情况, 
也可以建立多字段的组合索引和基于函数的索引 
ORACLE8.1.7字符串可以索引的最大长度为1578 单字节 
ORACLE8.0.6字符串可以索引的最大长度为758 单字节 
2.视图 (VIEW) 
CREATE VIEW 视图名AS SELECT …. FROM …..; 
ALTER VIEW视图名 COMPILE; 
视图仅是一个SQL查询语句, 它可以把表之间复杂的关系简洁化. 
3.同义词 (SYNONMY) 
CREATE SYNONYM同义词名FOR 表名; 
CREATE SYNONYM同义词名FOR 表名@数据库链接名; 
4.数据库链接 (DATABASE LINK) 
CREATE DATABASE LINK数据库链接名CONNECT TO 用户名 IDENTIFIED BY 密码 USING ‘数据库连接字符串’; 
数据库连接字符串可以用NET8 EASY CONFIG或者直接修改TNSNAMES.ORA里定义. 
数据库参数global_name=true时要求数据库链接名称跟远端数据库名称一样 
数据库全局名称可以用以下命令查出 
SELECT * FROM GLOBAL_NAME; 
查询远端数据库里的表 
SELECT …… FROM 表名@数据库链接名; 
 
