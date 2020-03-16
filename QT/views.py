from django.shortcuts import render, redirect
from django.db.models import Count
# Create your views here.
from index.models import Post, Commit
import math
from datetime import datetime
from users.models import UserProfile  #扩展后的User
def pagetegy(request, n):
    username = request.user.username
    category = 'qt'  # 页面分类
    current_page = int(n)
    posts_a = Post.objects.filter(category='其它')[10*(current_page-1):10*current_page]
    for co in posts_a:
        comment = Commit.objects.filter(post_id=co.id).aggregate(Count('id')) #计算评论数量

        Post.objects.filter(id=co.id).update(comment_number=comment['id__count'])


    post_count = Post.objects.filter(category='其它').aggregate(Count('id'))  #计算一共有多少篇文章
    numberpage = math.ceil(post_count['id__count']/10) #计算有多少页
    #posts = Post.objects.filter(Q(id__lte=max * 10) & Q(id__gte=(max-1) * 10 + 1))  # 出现在这一页的文章范围
    if current_page > 1:    #大于一页 前一页为-1
        last_page = current_page - 1
    else:
        last_page = 1
    if current_page < numberpage:
        next_page = current_page + 1
    else:
        next_page = numberpage
    countpage = numberpage+1
    list_num = []
    now = datetime.now
    user_id = request.user.id
    user_profile = UserProfile.objects.get(user_id=user_id)  # 扩展后的user 需要用到其头像
    if username == 'qq792074582':
        superuser = 1
    else:
        superuser = None
        # 目前页码小于等于5起始页码为1，结束页码为10；
        # 目前页码大于5并且小于等于最大页码-9，起始页码为目前页码-4，结束页码为+5；
        # 目前页码大于最大页码-9，起始页码为最大页码-9，结束页码为总共页码即countpage;
    if numberpage > 10:
        if current_page <= 5:
            start_page = 1
            end_page = 10
            # print('a')
        elif (current_page <= countpage - 9) & (current_page > 5):
            start_page = current_page - 4
            end_page = current_page + 5
            # print('b')
        elif current_page > countpage - 9:
            start_page = countpage - 9
            end_page = countpage - 1
    else:
        start_page = 1
        end_page = countpage-1
    for i in range(start_page, end_page+1):
        list_num.append(i)
    return render(request, 'page.html', locals())
