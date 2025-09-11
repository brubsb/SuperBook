from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('lista/', PostListView.as_view(), name='lista_posts'),
    path('novo/', PostCreateView.as_view(), name='novo_post'),
]

urlpatterns += [
    path('posts/<int:pk>/editar/', PostUpdateView.as_view(), name='editar_post'),
    path('posts/<int:pk>/excluir/', PostDeleteView.as_view(), name='excluir_post'),
]