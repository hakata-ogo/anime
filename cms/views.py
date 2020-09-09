from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Category

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "post/list.html"



class CategoryListView(ListView):
    model = Category
    template_name = "post/list.html"


# {% for link in object_list %}
#     <a href="{% url 'home' link.id %}">{{link}}</a>
# {% endfor %}