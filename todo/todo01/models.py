from django.db import models


# タプル[0]：html側で代入したい値＝色指定
# タプル[1]：ユーザー側の選択肢
CHOICE = (('danger', 'high'), ('warning', 'normal'), ('primary', 'low'))

# ここで言うモデルはDBのテーブルのこと。
# 各レコードはこのクラスから作成されたオブジェクトである
# クラス自体はテーブル自体のデザインである
class TodoModel(models.Model):
    # ユーザー入力フィールドの定義
    # 変数名 = フィールドの種類で定義（フィールドの種類は使いながら覚える）
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = CHOICE
        )
    duedate = models.DateField()

    def __str__(self):
        return self.title

class TodoModel2(models.Model):
    # ユーザー入力フィールドの定義
    # 変数名 = フィールドの種類で定義（フィールドの種類は使いながら覚える）
    title = models.CharField(max_length=100)
    memo = models.TextField()

    def __str__(self):
        return self.title