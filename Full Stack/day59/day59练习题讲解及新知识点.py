# 临时表
# select num, course_id from (select num,course_id from score where num > 60) as B


# 习题讲解请看day58

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
