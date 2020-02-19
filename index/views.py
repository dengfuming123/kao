from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import Post, Commit
from   django.db.models    import   Q
from django.db.models import Count
from index import  models
from datetime import datetime
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
  return render(request, 'index.html', locals())
def pagechange(request, n):
    username = request.user.username
    max = int(n) #转化为 int类型
    posts = Post.objects.filter(Q(id__lte=max*10) & Q(id__gte=(max-1)*10+1))
    post_count = Post.objects.aggregate(Count('id'))
    numberpage = 1+post_count['id__count']//10
    countpage = numberpage+1
    list_num = []
    now = datetime.now
    user_id = request.user.id
    if username == 'qq792074582':
        superuser = 1
    else:
        superuser = None
    for i in range(1, countpage):
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
    username = request.user.username
    title = request.POST.get('title')
    slug = request.POST.get('slug')
    body = request.POST.get('body')
    pic = request.FILES.get('pic')
    if request.method == 'POST':
        if title and slug and body and pic:
            Post.objects.create(title=title, slug=slug, body=body, user_id=user_id, goods_pic=pic)
            return redirect('/')
        elif title and slug and body:
            Post.objects.create(title=title, slug=slug, body=body, user_id=user_id)
            return redirect('/')
        else:
            tips = '发帖失败'
    return render(request, 'submit.html', locals())

def recordpost(request, user_id):
    records = Post.objects.filter(user=user_id)  #get只能查询一个，filter可以查询多个
    username = request.user.username
    #print(user_id)
    return render(request, 'record.html', locals())