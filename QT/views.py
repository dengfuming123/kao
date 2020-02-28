from django.shortcuts import render, redirect
from django.db.models import Count
# Create your views here.
from index.models import Post, Commit
import math
from datetime import datetime
from users.models import UserProfile  #扩展后的User
def pagetegy(request, n):
    username = request.user.username
    page = int(n)
    posts_a = Post.objects.filter(category='其它')[10*(page-1):10*page]
    for co in posts_a:
        comment = Commit.objects.filter(post_id=co.id).aggregate(Count('id')) #计算评论数量

        Post.objects.filter(id=co.id).update(comment_number=comment['id__count'])


    post_count = Post.objects.aggregate(Count('id'))  #计算一共有多少篇文章
    numberpage = math.ceil(post_count['id__count']/10) #计算有多少页
    #posts = Post.objects.filter(Q(id__lte=max * 10) & Q(id__gte=(max-1) * 10 + 1))  # 出现在这一页的文章范围
    countpage = numberpage+1
    list_num = []
    now = datetime.now
    user_id = request.user.id
    user_profile = UserProfile.objects.get(user_id=user_id)  # 扩展后的user 需要用到其头像
    if username == 'qq792074582':
        superuser = 1
    else:
        superuser = None
    for i in range(1, countpage):
        list_num.append(i)
    return render(request, 'page.html', locals())
