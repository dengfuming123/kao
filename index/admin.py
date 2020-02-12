from django.contrib import admin
from .models import Post, Commit
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date', 'user', 'goods_pic')

admin.site.register(Post, PostAdmin)
class CommitAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'user', 'goods_pic', 'post', 'body')

admin.site.register(Commit, CommitAdmin)