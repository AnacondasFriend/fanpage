from django.forms import ModelForm
from .models import *
 
 
# Создаём модельную форму
class AdForm(ModelForm):
    # в класс мета, как обычно, надо написать модель, по которой будет строиться форма и нужные нам поля. 
    class Meta:
        model = Ad
        fields = ['header', 'text', 'mediaImg', 'category', 'author']

