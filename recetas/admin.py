from django.contrib import admin
from recetas.models import *

admin.site.register(TipoReceta)
admin.site.register(UnidadesMedida)
admin.site.register(Categorias)
admin.site.register(Receta)
admin.site.register(RecetasCategorias)
admin.site.register(Ingredientes)
admin.site.register(PasosReceta)
admin.site.register(ComentariosReceta)
admin.site.register(ListaPersonalizadaUsuario)
admin.site.register(DetalleListaUsuario)
