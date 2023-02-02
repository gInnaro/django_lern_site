from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from todolist.views import todo
from todolist.views import category

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('main.urls')),
    re_path(r'^todo/', todo, name="TodoList"),
    re_path(r'^category/', category, name="Category"),
    re_path(r'^accounts/', include('django.contrib.auth.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
