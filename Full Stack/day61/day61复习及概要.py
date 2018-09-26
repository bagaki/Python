# 1、视图
#     100个SQL：
#         88： v1 as select * from tb1 where id>10
#             select .. from v1
#             select asd from v1
#      某个查询语句设置别名，日后方便使用
#      创建视图
#          create view 视图名称 as SQL
#       视图是虚拟的
#      修改
#          alter view 视图名称 as SQL
#      删除
#          drop view 视图名称;

# 2、触发器
#     当对某张表做：增删改操作时，可以使用触发器自定义关联行为

#     修改终止符
#     delimiter //
#     create trigger t1 before insert on  student for each row
#     begin
#         insert into teacher(tname) values('ssddd');
#     end //
#     delimiter ;
#
#     两个表都加入新插入数据
#     create trigger t1 before insert on  student for each row
#     begin
#         insert into teacher(tname) values(new.sname);
#     end
#

# 3、函数
#     内置函数：
#     select curdate();
#     select sum()
#     select char_length('asffs');
#     select concat('alex','BS')
#     时间格式化
#         select date_format()
#     blog
#     id      title     ctime
#      1       sdf      2018-08-16
#      2       sdf      2018-08-16
#      3       sdf      2018-08-16
#      4       sdf      2018-08-16

#     select ctime, count(1) from blog group ctime
#     select date_format(ctime, "%Y-%m"), count(1) from blog group date_format(ctime, "%Y-%m")

#     自定义函数(有返回值)：
#         delimiter \\
#             create function f1(
#                 i1 int,
#                 i2 int)
#             return int
#             begin
#                 declare num int default 0;
#                 set num = i1 + i2;
#                 return (num);
#             end \\
#          delimiter ;
#          select f1(1, 100);

# 4、存储过程
#     保存再MySQL上的一个别名 --->一堆SQL语句
#     别名()
#     用来替代程序员写SQL语句

#     方式一：
#         MySQL：存储过程
#         程序：调用存储过程
#     方式二：
#          MySQL：
#          程序：SQL语句
#     方式三：
#           MySQL：
# #          程序：类和对象（SQL语句）

#     1、简单
#         delimiter \\
#         create procedure p1()
#         begin
#             select * from student;
#             insert into teacher(tname) values('ct');
#         end \\
#         delimiter ;

#         call.p1()

#     2、传参数(in,out,inout)
#         delimiter \\
#         create procedure p2(
#             in n1 int,
#             in n2 int
#         )
#         begin
#             select * from student where sid > n1;;
#             insert into teacher(tname) values("ct");
#         end \\
#         delimiter ;

#         call p2(12,2)
#         cursor.callproc('p2',(12,2))

#     3、参数out
#         delimiter \\
#         create procedure p3(
#             in n1 int,
#             out n2 int
#         )
#         begin
#             set n2 = 123123;
#             select * from student where sid > n1;;
#             insert into teacher(tname) values("ct");
#         end \\
#         delimiter ;

#         set @v1 = 0;
#         call p3(12,@v1)
#         select @v1

# 特性：
#     a、可传参： in  out  inout
#     b、pymysql
#         cursor.callproc('p3',(12, 2))
#         result1 = cursor.fetchall()
#
#         cursor.execute('select @_p3_0, @_p3_1')
#         result2 = cursor.fetchall()

# 为什么又结果集又有out伪造的返回值

#     4、事务
#         delimiter \\
#         create procedure p4(
#             our status int
#         )
#         begin
#             1、声明如果出现异常执行{
#                  set status = 1;
#                  rollback;
#              }
#              开始事务
#                  账户减去100
#                  加90
#                  加10
#                  commit;
#              结束
#              set starts = 2
#         end \\
#         delimiter ;
#         ===============以上伪代码=====================
#         delimiter \\
#         create procedure p5(
#             out p_return_code tinyint
#         )
#         begin
#             declare exit handler for sqlexception
#             begin
#                 -- error
#                 set p_return_code = 1;
#                 rollback;
#             end;
#             stat transaction;
#                 delete from tb1;
#                 insert into tb2(name) values('seven');
#              commit;
#
#              -- success
#              set p_return_code = 2;
#              end \\
#         delimiter ;

#     5、游标
#     delimiter \\
#     create procedure p6()
#     begin
#         declare row_id int;  -- 自定义变量1
#         declare row_num varchar(50);  -- 自定义变量2
#         declare done int default false;
#         declare temp int;

#         declare my_cursor cursor for select id, num from A;
#         declare continue handler for not found set done = true;

#         open my_cursor;
#             xxoo: Loop
#                 fetch my_cursor into row_id, row_num;
#                 if done then
#                     leave xxoo;
#                 end if;
#                 set temp = row_id + row_num;
#                 insert into B(num) values(temp);
#             end loop xxoo;
#         close my_cursor;

#     end \\
#     delimiter ;

#     6、动态执行SQL(防止SQL注入)
#     delimiter \\
#     create procedure p7(
#         in tp1 varchar(255),
#         in arg int
#     )
#     begin
#         1、预检测某个东西，SQL语句合法性
#         2、SQL=格式化 tp1+arg
#         3、执行SQL语句

#         sete @xo = arg;
#         prepare xxx from 'select * from tb where id > ?';
#         execute xxx using @xo;
#         deallocate prepare prod;
#     end \\
#     delimiter ;

#     call p7("select * from tb where id > ?", 9)
#     ============================================
#     delimiter \\
#     create procedure p8(
#         in nid int
#     )
#     begin
#         set @nid = nid;
#         prepare prod from 'select * from student where sid > ?';
#         execute prod using @nid;
#         deallocate prepare prod;
#     end \\
#     delimiter ;


# 5、索引

# 6、ORM操作
#     类对象对数据进行操作


# 复习
# SQL语句
#      数据行
#          临时表：(select * from tb where id > 10)
#          指定映射：
#              select id,name,1,sum(x)/count()
#          条件
#              case when id > 8 then xx else xx end
#          三元运算
#              if(isnull(xx),0,1)
#          补充:
#              左右链表：join
#              上下链表：union
#                   自动去重
#                   select id, name from tb1
#                   union
#                   select num, snam from tb2
#                   不去重
#                   select id, name from tb1
#                   union all
#                   select num, snam from tb2



# 上节练习
# 参考表结构
#      用户信息
#      id  username  pwd
#      1     alex    123

#      权限
#      1   订单管理
#      2   用户券
#      3   bug管理
#      ...

#      用户类型&权限
#       1   1
#       1   2
#       1   3
#       程序
#           用户登录

#       基于角色权限管理
#          用户信息
#          id  username  pwd
#          1     alex    123

#          权限
#          1   订单管理
#          2   用户券
#          3   bug管理

#           角色表：
#           1、it部门员工
#           2、咨询员工
#           3、it主管
#           角色权限管理
#            1    1
#            1    2
#            3    1

# 基于角色的权限管理
# 需求分析