from django.db import models

# Create your models here.
# 图书管理系统，书，作者，出版社
# 出版社
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False, unique=True)
    publish = models.ForeignKey(to="Publisher", on_delete=False)

    def __str__(self):
        return "<Book Object: {}>".format(self.title)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, null=False, unique=True)
    # 告诉ORM 这张表和book表是多对多的关联关系，ORM自动帮我生成了第三张表
    book = models.ManyToManyField(to="Book")

    def __str__(self):
        return "<Author Object: {}>".format(self.name)