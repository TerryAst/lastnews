# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from news.forms import ArticleForm
from .models import Article
from .filters import NewsFilter
from django.urls import reverse_lazy


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
    paginate_by = 10
    # Переопределяем функцию получения списка товаров
   
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context
        
class ArticleDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости
    model = Article
    template_name = 'article.html'
    # Название объекта, в котором будет выбранная пользователем новость
    context_object_name = 'article'
    
class ArticleCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = ArticleForm
    model = Article
    # и новый шаблон, в котором используется форма.
    template_name = 'article_edit.html'
    
    def form_valid(self, form):
            article = form.save(commit=False)
            return super().form_valid(form)
    
class ArticleUpdate(UpdateView):
    form_class = ArticleForm
    model = Article
    template_name = 'article_edit.html'
    
class ArticleDelete(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')