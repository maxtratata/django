from django.shortcuts import render
from django.utils import timezone
from .models import Log


def home(request):
    # Сохранение данных о посещении главной страницы в логи
    log = Log(path="home", visited_at=timezone.now())
    log.save()

    html = """
    <h1>Главная страница</h1>
    <p>Добро пожаловать на мой первый Django-сайт!</p>
    """
    return render(request, 'home.html', {'html': html})

def about(request):
    # Сохранение данных о посещении страницы "О себе" в логи
    log = Log(path="about", visited_at=timezone.now())
    log.save()

    html = """
    <h1>О себе</h1>
    <p>Привет! Меня зовут Имя Фамилия и это мой первый Django-сайт.</p>
    """
    return render(request, 'about.html', {'html': html})