from django.urls import path
from .views import lista_posts, HeroListView

urlpatterns = [
    path('lista/', lista_posts, name='lista_posts'),
    path('cbv-lista/', HeroListView.as_view(), name='cbv_lista_posts'),
]

