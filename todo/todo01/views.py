from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel, TodoModel2
from django.urls import reverse_lazy

# Create your views here.

# ListView: リストで見るのに適したView
class TodoList(ListView):
    # template指定
    template_name = 'list.html'
    # モデル(テーブル)の指定
    model = TodoModel

class TodoList2(ListView):
    # template指定
    template_name = 'list_test.html'
    # モデル(テーブル)の指定
    model = TodoModel

class TodoDetail(DetailView):
    # template指定
    template_name = 'detail.html'
    # モデル(テーブル)の指定
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    # modelに規定したフィールド変数名をタプル
    # create.py内のformで呼び出される
    fields = ('title', 'memo', 'priority', 'duedate')
    # Createが成功した際にどのurlへ遷移させるかを規定
    # reverseではない: urlリクエスト > view > htmlやモデル
    # に対して、「逆に」内部の処理であるurlに飛ばす > view
    # 引数はurl.pyに設定したpathのname属性に対応する。
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    # modelに規定したフィールド変数名をタプル
    # create.py内のformで呼び出される
    #fields = ('title', 'memo', 'priority', 'duedate')
    # Createが成功した際にどのurlへ遷移させるかを規定
    # reverseではない: urlリクエスト > view > htmlやモデル
    # に対して、「逆に」内部の処理であるurlに飛ばす > view
    # 引数はurl.pyに設定したpathのname属性に対応する。
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')