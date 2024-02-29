import logging
from django.shortcuts import render


logger = logging.getLogger(__name__)

def home(request):
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Здесь вы можете найти информацию о сайте и обо мне.</p>
    """
    logger.info('Посещена главная страница')
    return render(request, 'myapp/home.html', {'html': html})

def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Я - разработчик Django-приложений.</p>
    """
    logger.info('Посещена страница "О себе"')
    return render(request, 'myapp/about.html', {'html': html})
