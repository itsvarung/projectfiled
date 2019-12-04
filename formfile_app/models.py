from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=130,null=False,default='N/A')
    last_name = models.CharField(max_length=130,null=False,default='N/A')
    gender = models.CharField(max_length=1,default='M')
    age = models.IntegerField(default=10)
    email = models.CharField(max_length=200)
    phone_no = models.IntegerField(default=00000000000)
