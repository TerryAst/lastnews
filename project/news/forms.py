from django import forms
from .models import Article
from django.core.exceptions import ValidationError
class ArticleForm(forms.ModelForm):
    class Meta:
       model = Article
       fields = [
           'author',
           'title',
           'description',
           'date'
       ]
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")

        if title == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data