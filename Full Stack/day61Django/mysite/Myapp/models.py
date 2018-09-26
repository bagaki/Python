from django.db import models

# Create your models here.
# ORM相关的只能写在这个文件里，写到别的文件里Django找不到


class UserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=False, max_length=20)
    