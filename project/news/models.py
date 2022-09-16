from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True, default='news') 
    subscribers= models.ManyToManyField(User)
    
    def __str__(self):
        return self.name.title()

# Новости для нашего сайта
class Article(models.Model):
    author =  models.CharField(
        max_length=30, default='anonim'        
        )
    title = models.CharField(
        max_length=50
        )
    description = models.TextField()
    date = models.DateField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        to_field='name',
        default='news'
    )
    
    def __str__(self):
        return f'{self.title}: {self.description[:20]}:{self.date}'

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])



    
