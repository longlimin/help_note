asdf;a;
--dml dcl ddl
sqlplus / as sysdba;
sqlplus 
conn scott/tiger

---
---oracle
---

--system
select userenv('language') from dual;
select * from v$nls_parameters;
select value from nls_database_parameters where parameter='nls_characterset'


--session process
select count(*) from v$process; 
select * from v$process;
select count(*) from v$session; 
select * from v$session;
select * from v$session 
where status='active';  


--sysdba lock session process  kill 
select session_id from v$locked_object;
select sid, serial#, username, osuser from v$session;-- where sid=783;

select sid||','||serial# kill, sid, serial#, username, osuser from v$session where sid in (select session_id from v$locked_object)
alter system kill session '783,18455';



select b.owner, b.object_name, a.session_id, a.locked_mode 
from v$locked_object a, dba_objects b
where b.object_id = a.object_id;

select value from v$parameter where name = 'processes';  
show parameter processes; 
alter system set processes=500 scope=spfile;
alter system set sessions=500 scope=spfile;
shutdown immediate; --shutdown db now
startup;     --start db 

---
---db link
---
grant CREATE PUBLIC DATABASE LINK，DROP PUBLIC DATABASE LINK to scott;
create database link DBLINK_NAME connect to USER01 identified by PASSWORD using 'TNS_NAME';
DBLINK_NAME : DB_LINK的名字
USER01　　     : 远程数据库的账户
PASSWORD     : 远程数据库的账户
TNS_NAME      : 远程数据库服务名 122.2312.13/orcl
select owner,db_link,username from dba_db_links;
select * from scott.tb_test@DBLINK_NAME;

---
---user control
---

--unlock 
alter user scott account unlock; 

--show
select * from dba_users;
select * from all_users;
select * from user_users; 
--b.²é¿žóã»§»òœçé«ïµí³èšïþ(ö±œóž³öµžøóã»§»òœçé«µäïµí³èšïþ)£º
select * from dba_sys_privs;
select * from user_sys_privs;
--c.²é¿žœçé«(ö»äü²é¿žµçâœóã»§óµóðµäœçé«)ëù°üº¬µäèšïþ
select * from role_sys_privs;
--d.²é¿žóã»§¶ôïóèšïþ£º
select * from dba_tab_privs;
select * from all_tab_privs;
select * from user_tab_privs;
--show roles
select * from dba_roles;
--f.²é¿žóã»§»òœçé«ëùóµóðµäœçé«£º
select * from dba_role_privs; 
select * from user_role_privs;
--g.²é¿žääð©óã»§óðsysdba»òsysoperïµí³èšïþ(²éñ¯ê±ðèòªïàóšèšïþ)
select * from v$pwfile_users
--update user pwd
create user username identified by password;
create user username identified by password default tablespace users quota 10m on users;
--delete the user
drop user username;
drop user username cascade; --link to all 


---
-- table control
---

--show all table s
select count(*) from user_tables;

--create
create table test(id varchar(20), time date);
create table test ( id varchar(20) primary key, time date, num number(3, 1), test varchar(20) not null, value varchar(20) default 'about' );
--1.create
create table table_name_new as select * from table_name_old 
--2.create
create table table_name_new as select * from table_name_old where 1=2; 
create table table_name_new like table_name_old 

-- delete the table 
drop  table test  ;

--index
alter table tb_a add  foreign key(id ) references tb_b(id);

--alter table
alter table tb_group add( checked varchar(10) default 'true' );
alter table tb_group rename column checked to newname;
alter table tb_group modify column_name not null;
alter table tb_group add unique(user_token)

--show table column
select * from all_tab_columns where table_name = upper('student') order by column_id
--show index
select * from user_indexs where table_name = upper('student') order by column_id
--show table create sql (index column)
select dbms_metadata.get_ddl('TABLE', 'STUDENT') from dual;

---
-- table date control  dml
---
---insert 
insert into table_name_new select * from table_name_old 
insert into table_name_new(column1,column2...) select column1,column2... from table_name_old
insert into test(id, time, test, num) values ('1', sysdate, 'test', '12.1');
insert into test(id, time, test, num) values ('3', sysdate, 'test3', '12.2');
insert into test(id, time, test, num) 
values ('2', to_date('1000-12-12 22:22:22','yyyy-mm-dd hh24:mi:ss'), 'test', '12.1');
insert into test2 values('1212', '1', 'name1');
--update
update  test set pwd=md5('cc'||id||md5('cc'||id||'qwer')) where id='admin';
update test
set(id,test,value)=(select 'no.'||rownum newid,num,value from test where 1=1 and id='1')
where id='1';
select * from test;

--delete
delete from test where 1=1 and id = 'aaa';
--drop table 
truncate table test;
--time to_char
select t.*,to_char(t.time, 'yyyy-mm-dd hh24:mi:ss') tochar from test t;
--count group having 
select tid, count(tid)  from 
(
select t1.*,t2.id ttid,t2.tid,t2.name from test t1, test2 t2
where 1=1
and t1.id>0 
and t1.id=t2.tid(+)
) t 
where 1=1
group by tid
having count(tid) >= 0

--join
select t1.*,count(t2.tid) from test t1 
left join test2 t2
on t1.id=t2.tid
where 1=1
and t1.id>0  
group by t2.tid

--every row group one line
select * from (
select 
row_number() over ( partition by t.test order by time desc) rn
,t.* 
from test t ) tt
where 1=1
and rn=1;

--with temp table view?
with 
temptable as (select * from test),
temptable2 as (select * from test)
select * from temptable,temptable2 whre a=1;
 
--exists 
select * from t1 where exists(select 1 from t2 where t1.a=t2.a) ;




---
---  function  trigger  job  procedure seq  md5 
---

create or replace trigger tr_info 
   before insert  
   on info 
   for each row  
begin
   update  info set about='1' where id like '%'||to_number(to_char(sysdate,'ss'))||'%' ;  
   update  info set about='0' where id like '%'||to_number(to_char(sysdate,'mi'))||'%' ;  
end; 


--more in plsql.sql
create or replace procedure p_createroomtest(cc in integer) as
i integer;
begin
  i := cc;     
  while i > 0 loop
  begin
    insert into   kfgl_fj(id,roomnum,roomtype,curpeople,roomstat,stationid) values(seq_test.nextval, 't-' || seq_test1.nextval,'43eb189e-a2be-4538-8276-94bc27c2a2b1','0','0','5103211993' ) ;

    i:= i - 1;
  end;
  end loop;

end p_createroomtest; 


--do procedure
begin
  p_createroomtest(800);
  commit;
end;


create sequence seq_file_down_up
minvalue 1
maxvalue 99999999
start with 1
increment by 1
cache 20;

--sequece
insert into info(id,userid) values(seq_info.nextval, 'test1');
 


--job 
var job1 number; 
begin 
  dbms_job.submit(:job1,'p_job1_test;',sysdate,'sysdate+1/1440'); 
  commit; 
end; 

begin 
  dbms_job.run(:job1); 
end; 





---
---functions  of system 
---

--fill to length
select 'scjs' || lpad(seq_t_contract_three.nextval,3, '0') from dual 

-- nvl nvl2 case when
select 
 nvl(t.id,'id is null') idnull
,nvl2(t.id,'not null','id is null') idnull
,(case when t.id='1' then 'ê¡¹«ëÿ1' when t.id='2' then 'ê¡¹«ëÿ2' else '·ö¹«ëÿ' end) name
 from test t;

--self function 
create or replace function file_size(n in varchar2) return varchar2 is retval varchar2(32);
begin
 retval := '';
 select
(case
when n>1024*1024*1024*1024 then trunc(n*10/1024/1024/1024/1024)/10||'tb'
when n>1024*1024*1024 then trunc(n*10/1024/1024/1024)/10||'gb'
when n>1024*1024 then trunc(n*10/1024/1024)/10||'mb'
when n>1024 then trunc(n*10/1024)/10||'kb'
else n||'b' 
  end) res  into retval
from dual  ;
 return retval;
end;

-- dbms_obfuscation_toolkit.md5
create or replace function md5(passwd in varchar2) return varchar2 is retval varchar2(32);
begin
 retval := lower(utl_raw.cast_to_raw( dbms_obfuscation_toolkit.md5(input_string => passwd)) );
 return retval;
end;

select md5('123456') from  dual;


--0.5 -> 1
select * from round(100 / 200, 4) * 100 || '%' from dual;
--random
select  dbms_random.value(1,100) from dual;



--time date chat string 
insert into test values('0002', to_date('1000-12-12','yyyy-mm-dd hh24:mi:ss') );
select  to_char(time, 'yyyy-mm-dd hh24:mi:ss' ), id  from test;
select substr(to_char(systimestamp, 'yyyy-mm-dd hh24:mi:ss:ff'), 0, 23 ) from dual; --ºáãë œøè¡
select  to_char(  to_date('1000-12-12','yyyy-mm-dd hh24:mi:ss'), 'yyyy-mm-dd hh24:mi:ss') from dual
--month + 1
select to_char(add_months(trunc(sysdate),1),'yyyy-mm') from dual;
select  sysdate,sysdate - interval '7' minute  from dual
select  sysdate - interval '7' hour  from dual
select  sysdate - interval '7' day  from dual
select  sysdate,sysdate - interval '7' month from dual
select  sysdate,sysdate - interval '7' year   from dual
select  sysdate,sysdate - 8 *interval '2' hour   from dual



