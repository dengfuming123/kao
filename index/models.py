from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    Article_category = (
     ('科技', '科技'),
     ('游戏', '游戏'),
     ('影视', '影视'),
     ('其它', '其它'),
    )
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    goods_pic = models.ImageField(upload_to='article_pic/', default='upming/logo.png')
    category = models.CharField(max_length=20, choices=Article_category, default='QT')
    comment_number = models.IntegerField(default=0)
    class Meta:
        ordering = ('-pub_date', )

    def __str__(self):
        return self.title
class Commit(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    goods_pic = models.ImageField(upload_to='article_pic', default='upimg/logo.png')
    class Meta:
        ordering = ('-pub_date', )

    def __str__(self):
        return self.body