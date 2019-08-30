from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from recetas import urls as recetas_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # Recetas URLS
    url(r'', include(recetas_urls)),
]
