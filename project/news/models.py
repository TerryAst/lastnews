from django.db import models



# Новости для нашего сайта
class Article(models.Model):
    title = models.CharField(
        max_length=50
        
        )
    description = models.TextField()
    date = models.DateField()
    

    def __str__(self):
        return f'{self.title}: {self.description[:20]}:{self.date}'


