from django.contrib import admin
from .models import Category, TodoList

admin.site.register(Category)
admin.site.register(TodoList)