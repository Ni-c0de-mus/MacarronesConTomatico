from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View, ListView

from recetas.models import Receta


class RecetasQueryset(object):
    def get_recetas_queryset(self, request):
        recetas = Receta.objects.all()

        return recetas


class HomeView(View, RecetasQueryset):
    def get(self, request):
        context = {
            'claseInicio': 'active',
            'claseRecetasDe': '',
            'claseTopRecetas': '',
            'claseUserRecetas': '',
            'claseCategorias_list': '',
            'recetas_list': self.get_recetas_queryset(request)
        }

        return render(request, 'recetas/home.html', context)


class CategoriasListView(View):
    def get(self, request):
        context = {
            'claseInicio': '',
            'claseRecetasDe': '',
            'claseTopRecetas': '',
            'claseUserRecetas': '',
            'claseCategorias_list': 'active'
        }

        return render(request, 'recetas/categorias.html', context)


class RecetasDeListView(View):
    def get(self, request):
        context = {
            'claseInicio': '',
            'claseRecetasDe': 'active',
            'claseTopRecetas': '',
            'claseUserRecetas': '',
            'claseCategorias_list': ''
        }

        return render(request, 'recetas/recetasDe.html', context)


class UserRecetasView(View):
    def get(self, request):
        context = {
            'claseInicio': '',
            'claseRecetasDe': '',
            'claseTopRecetas': '',
            'claseUserRecetas': 'active',
            'claseCategorias_list': ''
        }

        return render(request, 'recetas/user_recetas.html', context)


class TopRecetas(View):
    def get(self, request):
        context = {
            'claseInicio': '',
            'claseRecetasDe': '',
            'claseTopRecetas': 'active',
            'claseUserRecetas': '',
            'claseCategorias_list': ''
        }

        return render(request, 'recetas/topRecetas.html', context)
