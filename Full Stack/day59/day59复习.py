# 增删改查
#     insert xx(name) value('xx'),('xxx');
#     insert xx(name) select id from tb1;

# 自增
#     起始值 engine=innodb
#     步长： session;  global

# unique
#     表明这一列同一个东西只能出现一次
#     id name(unique) email(unique)
#     id name email unique(name, email)

# 排序
#     order by desc; asc

# 通配符
#     select xx from bb where name like "%a"

# limit
#

# 链表查询
#     select * from a left join b on a.id = b.id;
#      select * from class left join student on class.cid = student.class_id


# 删除
#     delete from tb1;
#     truncate table tb1;
#     drop table tb1;


# 分组
#     select count(id) from tb group by name;
#     select count(id) from tb group by name having count(id) > 10;

# 筛选条件
#     in    not in    between and     !=    and   or

# 外键