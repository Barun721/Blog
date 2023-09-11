from django import forms
from posts.models import Posts

class Post_form(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'

class Update_post(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'