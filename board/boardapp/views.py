from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
# User model: https://docs.djangoproject.com/en/3.1/ref/contrib/auth/
# username, password, first_name, lastname, email, groups, user_permissions, is_staff, is_active, is_superuser, last_login, date_joined
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import redirect
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

def signupfunc_check(request):

    # Userモデルの全オブジェクト
    object_list = User.objects.all()
    print(f'object_list: {object_list}')

    # Userモデルのフィールド（カラム）値を出力してみる
    object = User.objects.get(username='yuya')
    print(f'''
    {object}
    {object.username} 
    {object.password}
    {object.first_name} 
    {object.last_name} 
    {object.email}
    {object.groups}
    {object.user_permissions}
    {object.is_staff}
    {object.is_active}
    {object.is_superuser}
    {object.last_login}
    {object.date_joined}
    ''')
    
    # signupのPOSTの中身を確認
    print(f'request.POST: {request.POST}')

    # リクエストがPOSTであることを確認
    if request.method == "POST":
        print('this is POST method')
    else:
        print('this is GET method')

    return render(request, 'signup.html', {})
    # render: リクエストを受け取ってhttpオブジェクトをresponseとして返す
    # request, template, dict(model)


def signupfunc(request):

    if request.method == "POST":
        username = request.POST['username']  # htmlのformの name="username" から取ってくる。
        password = request.POST['password']  # htmlのformの name="password" から取ってくる。
        
        try:
            user = User.objects.create_user(username,'', password)  # 一般ユーザー作成
            return render(request, 'signup.html', {})    
        except IntegrityError:
            return render(request, 'signup.html', {'errormessage':'this username is already used.'})


    return render(request, 'signup.html', {})


def loginfunc(request):
    
    if request.method == 'POST':

        username = request.POST['username']  # htmlのformの name="username" から取ってくる。
        password = request.POST['password']  # htmlのformの name="password" から取ってくる。
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('list')

        else:
            return render(request, 'login.html', {'context':'failed logging in.'})
    
    return render(request, 'login.html', {'context':'get method'})


def logoutfunc(request):
    logout(request)
    return redirect('login')




@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

@login_required
def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'detail.html', {'object':object})

def goodfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)  # = get_object_or_404(BoardModel, pk=pk)
    object.good += 1
    object.save()
    return redirect('list')

def readfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)  # = get_object_or_404(BoardModel, pk=pk)
    username = request.user.get_username()
    if username in object.readtext:
        return redirect('list')
    else:
        object.read += 1
        object.readtext += f', {username}'
        object.save()
        return redirect('list')

class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'snsimage')
    success_url = reverse_lazy('list')

def su_tmpfunc(request):
    return render(request, 'signup_temp.html', {})
