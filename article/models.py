from django.db import models
from django.db.models import ManyToManyField

from user.models import UserModel
from django.conf import settings


# Create your models here.

class post(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    img_des = models.CharField(max_length=200)
    like: ManyToManyField = models.ManyToManyField(UserModel, related_name='followee', blank=True)
    main_image = models.ImageField(upload_to='images/', blank=True, null=True)





class postcommant(models.Model):
    class Meta:
        db_table = "comment"

    article = models.ForeignKey(post, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class photo(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

