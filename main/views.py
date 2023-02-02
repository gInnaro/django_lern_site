from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegisterUserForm
from .models import Info_index

def index(request):
    infos = Info_index.objects.all()  # запрашиваем все объекты todo через менеджер объектов
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', {"data": data, "infos": infos})

def about(request):
    return render(request, 'main/about.html')

def login(request):
    return render(request, 'registration/login.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')