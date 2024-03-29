from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import Post, Commit, User
from django.db.models import Q
from .forms import SelectCategory
from django.db.models import Count
from index import  models
from datetime import datetime
from users.models import UserProfile  #扩展后的User
import math
# Create your views here.
def index(request):
  # # 获取当前请求的用户名
  # username = request.user.username
  # posts = Post.objects.all()
  # post_count = Post.objects.aggregate(Count('id'))
  # list_num = []
  # now = datetime.now
  # user_id = request.user.id
  # if username == 'qq792074582':
  #     superuser = 1
  # else:
  #     superuser = None
  user = request.user
  if user.id:
      try:
        user_profile = UserProfile.objects.get(user_id=user.id)
      except:
          UserProfile.objects.create(user_id=user.id)         #如果没有对User进行 扩展  创建
  else:
      pass
  return render(request, 'index.html', locals())
def pagechange(request, n):
    username = request.user.username
    current_page = int(n) #转化为 int类型
    posts_a = Post.objects.all()[10*(current_page-1):10*current_page]   #每一页是哪几条
    for co in posts_a:
        comment = Commit.objects.filter(post_id=co.id).aggregate(Count('id')) #计算评论数量
        Post.objects.filter(id=co.id).update(comment_number=comment['id__count'])
    post_count = Post.objects.aggregate(Count('id'))  #计算一共有多少篇文章
    numberpage = math.ceil(post_count['id__count']/10) #计算有多少页
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
    if request.user.id:
       user_id = request.user.id
       user_profile = UserProfile.objects.get(user_id=user_id)  #扩展后的user 需要用到其头像
    if username == '792074582':
        superuser = 1
    else:
        superuser = None
    #当页码总数量大于10：
    #目前页码小于等于5起始页码为1，结束页码为10；
    #目前页码大于5并且小于等于最大页码-9，起始页码为目前页码-4，结束页码为+5；
    #目前页码大于最大页码-9，起始页码为最大页码-9，结束页码为总共页码即countpage;
    #当页码数量小于10：
    #起始位1，结束页码为总页码数
    #tab键整体后移
    if numberpage > 10:
        if current_page <= 5:
            start_page = 1
            end_page = 10
            # print('a')
        elif (current_page <= countpage-9) & (current_page > 5):
            start_page = current_page-4
            end_page = current_page+5
            # print('b')
        elif current_page > countpage-9:
            start_page = countpage - 9
            end_page = countpage - 1
            # print('c')
    else:
        start_page = 1
        end_page = countpage-1
    # print(countpage)
    # print(start_page)
    # print(end_page)
    # for add in range(100):
    #     Post.objects.create(title=add, slug=add, body=add, user_id=user_id, category='其它')
    for i in range(start_page, end_page+1):
        list_num.append(i)
    return render(request, 'page.html', locals())
def showpost(request,id):
    # try:
    post = Post.objects.get(id=id)
    commit_body = request.POST.get('commit')
    commit_post = post.id
    commit_user = request.user.id
    commit_pic = request.FILES.get('pic')
    username = request.user.username
    user_id = commit_user
    if request.user.id:
        user_id = request.user.id
        user_profile = UserProfile.objects.get(user_id=user_id)  # 扩展后的user 需要用到其头像
    commits = Commit.objects.filter(post_id=id)
    if request.method == 'POST':
        if commit_body and commit_post and commit_user and commit_pic:
            Commit.objects.create(user_id=commit_user, body=commit_body, post_id=commit_post, goods_pic=commit_pic)
            return render(request, 'post.html', locals())
        elif commit_body and commit_post and commit_user:
            Commit.objects.create(user_id=commit_user, body=commit_body, post_id=commit_post)
            return render(request, 'post.html', locals())
        else:
            tips = '回复失败'
    return render(request, 'post.html', locals())
def writepost(request):
    user_id = request.user.id
    if user_id:
        user_id = request.user.id
        user_profile = UserProfile.objects.get(user_id=user_id)  # 扩展后的user 需要用到其头像
    username = request.user.username
    title = request.POST.get('title')
    slug = request.POST.get('slug')
    body = request.POST.get('body')
    pic = request.FILES.get('pic')
    select_form = SelectCategory()
    get_value = request.POST.get('sel_value', '')
    if request.method == 'POST':
        if title and body and pic and get_value:
            Post.objects.create(title=title, slug=slug, body=body, user_id=user_id, goods_pic=pic, category=get_value)
            return redirect('index')
        elif title and body and get_value:
            Post.objects.create(title=title, slug=slug, body=body, user_id=user_id, category=get_value)
            return redirect('index')
        else:
            tips = '发帖失败'
    return render(request, 'submit.html', locals())

def recordpost(request, user_id):
    user_id = request.user.id
    user_profile = UserProfile.objects.get(user_id=user_id)  # 扩展后的user 需要用到其头像
    records = Post.objects.filter(user=user_id)  #get只能查询一个，filter可以查询多个
    username = request.user.username
    #print(user_id)
    return render(request, 'record.html', locals())