# SQL语句操作补充
# create table tb11(
#     id int auto_increment primary key,
#     name varchar(32),
#     age int
# )engine=innodb default charset=utf8;

# 增
# insert into tb(name, age) values('alex',12);
# insert into tb(name, age) values('alex',12),('root',12);
# 把一个表的数据全部添加到另一个表
#    insert into tb12(name, age) select name,age from tb11;


# 删
# delete from tb12;
# delete from tb12 where id=2;
# delete from tb12 where id!=2;
# delete from tb12 where id>2;
# delete from tb12 where id>=2 or name='alex';


# 改
# update tb12 set name='alex' where id > 12 and name = 'xx';
# update tb12 set name='alex', age=19 where id>12 and name='xx';


# 查
# select * from tb12;
# select id,name from tb12;
# select id,name from tb12 where id > 10 or name = 'xxx';
# 取别名：select id,name as cname from tb12 where id > 10 or name = 'xxx';
# select name,age,11 from tb12;


# 其他：
# select * from tb12 where id != 1;
# select * from tb12 where id <> 1;

# select * from tb12 where id in (1,2, 12);
# select * from tb12 where id not in (1,2, 12);
# select * from tb12 where id in (select id from tb11);
# select * from tb12 where id between 5 and 12;

# 通配符
# select * from tb12 where name like "a%"  查找a，甚至a后还可以跟有其他字符
# select * from tb12 where name like "a_"  查找a，只找a，a后只能跟一个字符

# select * from tb12 limit 10;    取前多少个
# select * from tb12 limit 1,2;   从开始，往后取多少条
# select * from tb12 limit 1 offset 2;

# 分页
# page = input('请输入要查看的页码：')
# page = int(page)
# (page - 1) * 10
# select * from tb12 limit 0, 10;1
# select * from tb12 limit 10,10;2

# 排序
#     select * from tb12
#     select * from tb12 order by id desc;
#     select * from tb12 order by id asc;
#     select * from tb12 order by age desc, id desc;

#     取后10条数据
#     select * from tb12 order by id desc limit 10;

# 分组
#     select count(id), part_id from userinfo5 group by part_id;

#     如果对于聚合函数结果进行二次筛选时，必须使用having
#     select count(id), max(id), part_id from userinfo5 group by part_id having count(id) > 1;

#      计算有多少组
#      select count(id) from userinfo5;


# 连表操作：
#     select * from userinfo5. department5 where userinfo5.part_id = department5.id
#     select * from userinfo5 left join department5 on userinfo5.part_id = department5.id
#     userinfo5左边全部显示

#     select * from userinfo5 right join department5 on userinfo5.part_id = department5.id
#     department5右边全部显示

#     有null 就隐藏
#     select * from userinfo5 innder join department5 on userinfo5.part_id = department5.id

# select * from
#     department5
# left join userinfo5 on userinfo5.part_id = department.id
# left join userinfo6 on userinfo5.part_id = department.id

# select
#     score.sid
#     student.sid
#     from
# score
#     left join student on score.student_id = student.sid
#     left join course on score.course_id = course.cid
#     left join class on student.class_id = class.cid
#     left join teacher on course.teacher_id = teacher.tid


# 作业

# https://images2015.cnblogs.com/blog/425762/201608/425762-20160803224643778-2071849037.png

# 1、自行创建测试数据
#
# 2、查询“生物”课程比“物理”课程成绩高的所有学生的学号；
# 先合并连接score和course
# select * from score left join course on score.course_id = course.cid;
# 选出表中有生物课和物理课的学生
# select * from score left join course on score.course_id = course.cid where course.cname='生物';
# select score.sid,score.student_id,course.cname,score.num from score left join course on score.course_id = course.cid where course.cname='生物';
# select score.sid,score.student_id,course.cname,score.num from score left join course on score.course_id = course.cid where course.cname='物理';
# 把生物课表和物理课表写成临时表，并合并
# select * from (select score.sid,score.student_id,course.cname,score.num from score left join course on score.course_id = course.cid where course.cname='生物') as A inner join (select score.sid,score.student_id,course.cname,score.num from score left join course on score.course_id = course.cid where course.cname='物理') as B on A.student_id = B.student_id;
# 再做比较
# select * from (select score.sid,score.student_id,course.cname,score.num from score left join course on score.course_id = course.cid where course.cname='生物') as A inner join (select score.sid,score.student_id,course.cname,score.num from score left join course on score.course_id = course.cid where course.cname='物理') as B on A.student_id = B.student_id where A.num > B.num;
# 只取id
# select A.student_id from (select score.sid,score.student_id,course.cname,score.num from score left join course on score.course_id = course.cid where course.cname='生物') as A inner join (select score.sid,score.student_id,course.cname,score.num from score left join course on score.course_id = course.cid where course.cname='物理') as B on A.student_id = B.student_id where A.num > B.num;
#
# 3、查询平均成绩大于60分的同学的学号和平均成绩；
# select student_id,avg(num) from score group by student_id having avg(num) > 60;
# 附加：显示学生名字
# select * from (select student_id,avg(num) from score group by student_id having avg(num) > 60) as B left join student on B.student_id=student.sid;
# select B.student_id,student.sname, B.ccc from (select student_id,avg(num) as ccc from score group by student_id having avg(num) > 60) as B left join student on B.student_id=student.sid;
#
# 4、查询所有同学的学号、姓名、选课数、总成绩；
# 先链表，将score和student表连起来
#  select * from score left join student on score.student_id = student.sid;
# 选课数：从学生id中，计算出，count(student_id)
# 总成绩：sum(num)
# select score.student_id,student.sname,count(student_id),sum(num) from score left join student on score.student_id = student.sid group by score.student_id;
#
# 5、查询姓“李”的老师的个数；
#
# 6、查询没学过“叶平”老师课的同学的学号、姓名；
# 先查看李平老师的课程有哪些
# select cid from course left join teacher on course.teacher_id = teacher.tid where teacher.tname = '李平老师';
# 查看score表里有李平老师课程的id
# select * from score where course_id in (2, 4);
# select * from score where course_id in (select cid from course left join teacher on course.teacher_id = teacher.tid where teacher.tname = '李平老师');
# 展示出这些学生的id
# select student_id from score where course_id in (select cid from course left join teacher on course.teacher_id = teacher.tid where teacher.tname = '李平老师') group by student_id;
# 再将没选过李平老师的学生展示出来
# select student.sid,student.sname from student where sid not in (select student_id from score where course_id in (select cid from course left join teacher on course.teacher_id = teacher.tid where teacher.tname = '李平老师') group by student_id);
#
# 7、查询学过“001”并且也学过编号“002”课程的同学的学号、姓名；
# 将上过者两种课的id展示出来
# select student_id from score where course_id =1 or course_id=2 group by student_id having count(course_id) > 1;
# 联合名字
# select score.student_id,student.sname from score left join student on score.student_id=student.sid where course_id =1 or course_id=2 group by student_id having count(course_id) > 1;
#
# 8、查询学过“叶平”老师所教的所有课的同学的学号、姓名；
# 先找出学过任意一门课程的学生
# select * from score where course_id in (select cid from course left join teacher on course.teacher_id = teacher.tid where teacher.tname = '李平老师');
# 再找两门都学过的学生
# select student_id from score where course_id in (select cid from course left join teacher on course.teacher_id = teacher.tid where teacher.tname = '李平老师')group by student_id having count(course_id) = (select count(cid) from course left join teacher on course.teacher_id = teacher.tid where teacher.tname = '李平老师')
#
# 9、查询课程编号“002”的成绩比课程编号“001”课程低的所有同学的学号、姓名；
#
# 10、查询有课程成绩小于60分的同学的学号、姓名；
# select student_id from score where num < 60 group by student_id
# select DISTINCT student_id from score where num < 60
# 但是DISTINCT效率不高
#
# 11、查询没有学全所有课的同学的学号、姓名；
# 先找到学生学了多少门的id和数量
# select student_id,count(1) from score group by student_id;
# 再找出没有学全的学生id
# select student_id,count(1) from score group by student_id having count(1) < (select count(cid) from course);
#
# 12、查询至少有一门课与学号为“001”的同学所学相同的同学的学号和姓名；
# 找到'001'同学的课程
# select course_id from score where student_id =1;
# 除'001'同学以外，上过和'001'一样的课程的同学
# select * from score where student_id != 1 and course_id in (select course_id from score where student_id =1);
# 以student_id分组即可
# select student_id from score where student_id != 1 and course_id in (select course_id from score where student_id =1) group by student_id;
# 还可连student表，打印出student_id的名字
#
# 13、查询至少学过学号为“001”同学所选课程中任意一门课的其他同学学号和姓名；
#  select course_id from score where student_id =1;
# select student_id,count(1) from score where student_id != 1 and course_id in (select course_id from score where student_id =1) group by student_id having count(1) = (select count(course_id) from score where student_id =1);
#
# 14、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；
# 获取和'001'选课个数相同的同学
# '001'同学学科个数
# select count(1) from score where student_id = 1;
# select student_id,count(1) from score where student_id !=1 group by student_id having count(1) = (select count(1) from score where student_id = 1);
# 含有一样课程的同学
# select * from score where student_id in (select student_id from score where student_id !=1 group by student_id having count(1) = (select count(1) from score where student_id = 1));
# 找出一模一样的同学
# select student_id from score where student_id in (select student_id from score where student_id !=1 group by student_id having count(1) = (select count(1) from score where student_id = 1)) and course_id in (select course_id from score where student_id = 1) group by student_id having count(1) = (select count(1) from score where student_id = 1);
#
# 15、删除学习“叶平”老师课的SC表记录；
# delete from score where course_id in(select cid from course left join teacher on course.teacher_id = teacher.tid where teacher.tname='李平老师');
#
# 16、向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩；
# insert into score(student_id,course_id,num) select student_id,2,(select avg(num) from score where course_id = 2) from student where sid not in (select student_id from score where course_id = 2)
#
# 17、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；
#
# 18、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
#
# 19、按各科平均成绩从低到高和及格率的百分数从高到低顺序；
# select course_id,avg(num), sum(case when num < 60 then 0 else 1 end),sum(1), (sum(case when num < 60 then 0 else 1 end)/sum(1)) as d from score group by course_id order by avg(num) asc, d desc;
#
# 20、课程平均分从高到低显示（现实任课老师）；
# select score.course_id, course.cname,avg(num), teacher.tname from score left join course on score.course_id = course.cid left join teacher on teacher.tid = course.teacher_id group by score.course_id;
# 或
# select score.course_id, course.cname,avg(if(isnull(score.num),0,score.num)), teacher.tname from score left join course on score.course_id = course.cid left join teacher on teacher.tid = course.teacher_id group by score.course_id;
#
# 21、查询各科成绩前三名的记录:(不考虑成绩并列情况)
# select * from (select student_id, course_id,num,1,(select num from score as s2 where s2.course_id = s1.course_id group by s2.num order by s2.num desc limit 0,1),(select num from score as s2 where s2.course_id = s1.course_id group by s2.num order by s2.num desc limit 3,1) as cc from score as s1) as B where B.num > B.cc;
#
# 22、查询每门课程被选修的学生数；
#  select course_id, count(1) from score group by course_id;
# 热门：
# select course_id, count(1) from score group by course_id having count(1) > 5;
#
# 23、查询出只选修了一门课程的全部学生的学号和姓名；
# select student_id,count(1) from score group by student_id having count(1) = 1;
#
# 24、查询男生、女生的人数；
# select gender, count(1) from student group by gender;
#
# 25、查询姓“张”的学生名单；
# select sname from student where sname like '张%';
#
# 26、查询同名同姓学生名单，并统计同名人数；
# select sname,count(1) from student group by sname;
#
# 27、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
#
# 28、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；
#
# 29、查询课程名称为“数学”，且分数低于60的学生姓名和分数；
# select score.student_id,student.sname ,score.num from score left join course on score.course_id = course.cid left join student on score.student_id = student.sid  where score.num < 60 and course.cname = '生物';
#
# 30、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名；
#
# 31、求选了课程的学生人数
#
# 32、查询选修“杨艳”老师所授课程的学生中，成绩最高的学生姓名及其成绩；
#
# 33、查询各个课程及相应的选修人数；
#
# 34、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；
#
# 35、查询每门课程成绩最好的前两名；
#
# 36、检索至少选修两门课程的学生学号；
#
# 37、查询全部学生都选修的课程的课程号和课程名；
#
# 38、查询没学过“叶平”老师讲授的任一门课程的学生姓名；
#
# 39、查询两门以上不及格课程的同学的学号及其平均成绩；
#
# 40、检索“004”课程分数小于60，按分数降序排列的同学学号；
#
# 41、删除“002”同学的“001”课程的成绩；


# 答案：https://www.cnblogs.com/wupeiqi/articles/5748496.html