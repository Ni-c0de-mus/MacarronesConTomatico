from django.conf.urls import url
from recetas.views import HomeView


urlpatterns = [
    # Photo urls
    url(r'^$', HomeView.as_view(), name='recetas_home'),
]