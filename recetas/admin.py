from django.contrib import admin
from recetas.models import *


class IngedienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_receta', 'ingrediente')

    def nombre_receta(self, obj):
        return obj.idReceta.titulo


class CategoriaRecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre_receta', 'nombre_categoria')

    def nombre_categoria(self, obj):
        return obj.idCategoria.nombreCategoria

    def nombre_receta(self, obj):
        return obj.idReceta.titulo


admin.site.register(TipoReceta)
admin.site.register(UnidadesMedida)
admin.site.register(Categorias)
admin.site.register(Receta)
admin.site.register(CategoriasReceta, CategoriaRecetaAdmin)
admin.site.register(PasosReceta)
admin.site.register(ComentariosReceta)
admin.site.register(ListaPersonalizadaUsuario)
admin.site.register(DetalleListaUsuario)
admin.site.register(Ingredientes, IngedienteAdmin)
