from django.forms import ModelForm
from instagram.models import Article


class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'photo', 'contents']