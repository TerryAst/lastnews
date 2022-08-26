from django.urls import path
# Импортируем созданное нами представление
from .views import ArticleList, ArticleDetail


urlpatterns = [
   path('', ArticleList.as_view()), 
   path('<int:pk>', ArticleDetail.as_view()),
]