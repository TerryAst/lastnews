from celery import shared_task
from django.core.mail import send_mail
from news.models import Article
import datetime
from django.contrib.auth.models import User

@shared_task
def week_news():
    articles = Article.objects.filter(date__gte=datetime.date.today() - datetime.timedelta(days=7))
    users = User.objects.all()
    users_emails = [i.email for i in users]
    articles_titles = [i.title for i in articles]
    send_mail( 
        subject=f'Новые новости на сайте за неделю',  
        message=articles_titles,  
        from_email='newsportal22@yandex.com', 
        recipient_list=users_emails,
        ) 
      
    