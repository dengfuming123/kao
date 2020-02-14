from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import random
from django.contrib.auth.hashers import make_password
def loginView(request):
    # 设置标题和另外两个URL链接
    title = '登录'
    unit_2 = '/user/register.html'
    unit_2_name = '立即注册'
    unit_1 = '/user/FindPassword.html'
    unit_1_name = '修改密码'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                return redirect('/')
            else:
                tips = '账号密码错误，请重新输入'
        else:
            tips = '用户不存在，请注册'
    return render(request, 'user.html', locals())

# 用户注册
def registerView(request):
    # 设置标题和另外两个URL链接
    title = '注册'
    unit_2 = '/user/login.html'
    unit_2_name = '立即登录'
    unit_1 = '/user/FindPassword.html'
    unit_1_name = '修改密码'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        if User.objects.filter(username=username):
            tips = '用户已存在'
        elif User.objects.filter(email=email):
            tips = '此邮箱不可用'
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            tips = '注册成功，请登录'
    return render(request, 'Register.html', locals())
from django.contrib.auth.hashers import make_password

def findPassword(request):
    button = '获取验证码'
    new_password = False
    if request.method == 'POST':
        username = request.POST.get('username', 'root')
        VerificationCode = request.POST.get('VerificationCode', '')
        password = request.POST.get('password', '')
        user = User.objects.filter(username=username)
        # 用户不存在
        if not user:
            tips = '用户' + username + '不存在'
        else:
            for u in user:
                # 判断验证码是否已发送
                if not request.session.get('VerificationCode', ''):
                    # 发送验证码并将验证码写入session
                    button = '重置密码'
                    tips = '验证码已发送'
                    new_password = True
                    VerificationCode = str(random.randint(1000, 9999))
                    request.session['VerificationCode'] = VerificationCode
                    u.email_user('找回密码', VerificationCode)
                # 匹配输入的验证码是否正确
                elif VerificationCode == request.session.get('VerificationCode'):
                    # 密码加密处理并保存到数据库
                    dj_ps = make_password(password, None, 'pbkdf2_sha256')
                    u.password = dj_ps
                    u.save()
                    del request.session['VerificationCode']
                    tips = '密码已重置'
            # 输入验证码错误
                else:
                    tips = '验证码错误，请重新获取'
                    new_password = False
                    del request.session['VerificationCode']
    return render(request, 'FindPassword.html', locals())
# 用户注销，退出登录
def logoutView(request):
    logout(request)
    return redirect('/')