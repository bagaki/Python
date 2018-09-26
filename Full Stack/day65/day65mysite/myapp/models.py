from django.db import models

# Create your models here.
class Classes():
    cid = models.BigAutoField(primary_key=True)
    caption = models.CharField(null=False, max_length=20)