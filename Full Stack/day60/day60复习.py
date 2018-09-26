# 1、MySQL：文件管理的软件

# 2、三部分
#      服务端
#      SQL语句
#      客户端

# 3、客户端
#     mysql
#     navicate

# 4、授权操作
#     用户操作
#     授权操作

# 5、sql语句
#     数据库操作
#         create database xx default charset utf8;
#         drop database xx;
#     数据表
#          列
#              varchar和char
#              数字
#                  整数
#                  小数
#              字符串
#              时间：datatime
#              二进制
#          其他：引擎 字符编码 起始值

#          主键索引：非空且唯一
#          唯一索引：可以为空
#          外键：约束省空间
#               一对多
#               一对一
#               多对多
#     数据行
#          增
#          删
#          改
#          查
#               in   not in
#               between  and
#               limit
#               group by  having
#               order by
#               like "%a" "a_"
#               left join   inner join   right join xx on 关系
#               临时表
#                   保存临时数据，供之后再用
#                   select * from (select * from tb where id < 10) as B;

#                    select
#                        id，
#                        name，
#                        1，
#                        (select count(1) from tb)
#                     from tb2

#     ps：数据放在硬盘上

