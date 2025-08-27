from django.views.generic import ListView
from django.shortcuts import render
from .models import Post

def lista_posts(request):
    posts = Post.objects.all()  # busca todos os heróis do banco
    return render(request, "posts/lista_posts.html", {"posts": posts})

class HeroListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"
    