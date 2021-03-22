from django.contrib import admin
from .models import TodoModel
# Register your models here.

# admin画面に何を表示するか
admin.site.register(TodoModel)