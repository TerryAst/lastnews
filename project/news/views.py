# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView
from .models import Article


class ArticleList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Article
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-date'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    
class ArticleDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости
    model = Article
    template_name = 'article.html'
    # Название объекта, в котором будет выбранная пользователем новость
    context_object_name = 'article'
