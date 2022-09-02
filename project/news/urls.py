from django.urls import path
# Импортируем созданное нами представление
from .views import ArticleList, ArticleDetail, ArticleDetail, ArticleCreate, ArticleUpdate, ArticleDelete


urlpatterns = [
   path('', ArticleList.as_view()), 
   path('<int:pk>', ArticleDetail.as_view(), name='article_detail'),
   path('create/', ArticleCreate.as_view(), name='article_create'),
   path('<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
   path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]