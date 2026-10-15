from django.forms import ModelForm, Form
from daily_news.models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"

