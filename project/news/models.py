from django.db import models
from django.urls import reverse



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
    
    def __str__(self):
        return f'{self.title}: {self.description[:20]}:{self.date}'

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
    
