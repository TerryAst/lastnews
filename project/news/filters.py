from django_filters import FilterSet
from .models import Article

class NewsFilter(FilterSet):
   class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Article
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           'title': ['icontains'],
           'author': ['icontains'],
           'date': ['gt'],
       }