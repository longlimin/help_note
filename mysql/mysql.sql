

--Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column To disable safe mode, toggle the option in Preferences -> SQL Queries and reconnect.
--这是因为MySql运行在safe-updates模式下，该模式会导致非主键条件下无法执行update或者delete命令
--查看是否开启了安全模式
show variables like ‘SQL_SAFE_UPDATES‘;

--关闭
SET SQL_SAFE_UPDATES = 0;


 


