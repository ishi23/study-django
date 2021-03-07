from django.urls import path
from .views import app1view

# 左：ベースURLについている文字列（コマンド）、右：処理
urlpatterns = [
    path('view1/', app1view),
]