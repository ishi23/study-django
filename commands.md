# プロジェクトのスタート

### プロジェクトの作成
`$ django-admin startproject <project_name>`

```
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── basics.md
├── commands.md
└── project_name
    ├── db.sqlite3
    ├── project_name
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py
```

2 directories, 12 files

# 「アプリ」の作成
$ python manage.py startapp <app_name>
# app用のフォルダが作成されてデフォルトファイル群が作成される
```
.
├── db.sqlite3
├── helloworld
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── helloworldapp1
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── templates
    └── hello.html

4 directories, 16 files
```


# サーバーの起動(Webアプリを動かす)
`$ python manage.py runserver`

# make migration: models.py(DBテーブル設計ファイル)のチェックと履歴保存
`$ python manage.py makemigrations <app_name>  # <app_name>無しだと全アプリ`

# migration: テーブルを作成
`$ python manage.py `

# superuser作成
`$ python manage.py createsuperuser`
- ユーザー名、パスワードが要求されるので入力