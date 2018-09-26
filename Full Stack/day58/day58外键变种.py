# 唯一索引
#     索引，基本为了加速
#     create table t1(
#         id ine ..,
#         num int,
#         xx int,
#         unique uq1 (num, xx)
# )
#      约束不能重复，可以为空
#      主键不能重复，不能为空

# 外键变种
#    a.用户表和部门表  一对多
#        用户：
#        部门：


#    b.用户表和博客表
#       一对一
# create table userinfo1(
#     id int auto_increment primary key,
#     name char(10),
#     gender char(10),
#     email varchar(64)
# )engine=innodb default charset=utf8;

# create table admin(
#     id int not null auto_increment primary key,
#     username varchar(64) not null,
#     password varchar(64) not null,
#     user_id int not null,
#     unique uq_u1 (user_id),
#     CONSTRAINT fk_admin_u1 FOREIGN key (user_id) REFERENCES userinfo1(id)
# )engine=innodb default charset=utf8;


#    c.用户表
#      主机表
#      用户主机关系表
#       多对多
# create table userinfo2(
#     id int auto_increment primary key,
#     name char(10),
#     gender char(10),
#     email varchar(64)
# )engine=innodb default charset=utf8;

# create table host(
#     id int auto_increment primary key,
#     hostname char(64)
# )engine=innodb default charset=utf8;

# create table user2host(
#     id int auto_increment primary key,
#     userid int not null,
#     hostid int not null,
#     unique uq_user_host (userid, hostid),
#     CONSTRAINT fk_u2h_user FOREIGN key (userid) REFERENCES userinfo2(id),
#     CONSTRAINT fk_u2h_host FOREIGN key (hostid) REFERENCES host(id)
# )engine=innodb default charset=utf8;