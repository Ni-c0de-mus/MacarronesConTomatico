from django.conf.urls import url
from recetas.views import HomeView, UserRecetasView, CategoriasListView, TopRecetas, RecetasDeListView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Photo urls
    url(r'^$', HomeView.as_view(), name='recetas_home'),
    url(r'^mis-recetas/$', login_required(UserRecetasView.as_view()), name='user_recetas'),
    url(r'^categorias/$', CategoriasListView.as_view(), name='categorias_list'),
    url(r'^top-recetas$', TopRecetas.as_view(), name='top_recetas'),
    url(r'^recetas-de/$', RecetasDeListView.as_view(), name='recetas_de'),
]
