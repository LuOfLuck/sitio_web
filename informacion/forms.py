from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Comentario

class ComentarioFrom(forms.ModelForm):


    class Meta():

        model = Comentario

        fields = ['contenido', 'autor']