from django.contrib.auth.models import User
from django.db import models


class TipoReceta(models.Model):
    idTipoReceta = models.AutoField(primary_key=True)
    nombreTipo = models.CharField(max_length=250)

    def __str__(self):
        return self.nombreTipo


class UnidadesMedida(models.Model):
    idUnidadesMedida = models.AutoField(primary_key=True)
    nombreUnidad = models.CharField(max_length=250)

    def __str__(self):
        return self.nombreUnidad


class Categorias(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=250)

    def __str__(self):
        return self.nombreCategoria


class Receta(models.Model):
    idReceta = models.AutoField(primary_key=True)
    idPropietario = models.ForeignKey(User, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField(blank=True)
    urlFoto = models.URLField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)
    vecesVista = models.IntegerField(default=0)
    vecesCompartida = models.IntegerField(default=0)
    numMeGusta = models.IntegerField(default=0)
    visible = models.BooleanField(default=True)
    tipoReceta = models.ForeignKey(TipoReceta, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo


class RecetasCategorias(models.Model):
    idReceta: models.ForeignKey(Receta, on_delete=models.PROTECT)
    idCategoria: models.ForeignKey(Categorias, on_delete=models.PROTECT)

    # TODO: controlar al insertar que no puedan repetirse recetas y categorías
    # class Meta:
        # unique_together = (("idReceta", "idCategoria"),)

    def __str__(self):
        return self.idReceta


class Ingredientes(models.Model):
    idReceta = models.ForeignKey(Receta, on_delete=models.PROTECT)
    ingrediente = models.CharField(max_length=250)
    cantidad = models.DecimalField(blank=True, default=0, decimal_places=2, max_digits=10)
    unidadMedida = models.ForeignKey(UnidadesMedida, on_delete=models.PROTECT)

    def __str__(self):
        return self.ingrediente


class PasosReceta(models.Model):
    idReceta = models.ForeignKey(Receta, on_delete=models.PROTECT)
    descPaso = models.TextField()
    urlImagenPaso = models.URLField()

    def __str__(self):
        return self.descPaso


class ComentariosReceta(models.Model):
    idReceta = models.ForeignKey(Receta, on_delete=models.PROTECT)
    usuarioComentario = models.ForeignKey(User, on_delete=models.PROTECT)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True, blank=True)
    comentario = models.TextField()

    def __str__(self):
        return self.comentario


class ListaPersonalizadaUsuario(models.Model):
    idUsuario = models.ForeignKey(User, on_delete=models.PROTECT)
    nombreLista = models.CharField(max_length=250)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("idUsuario", "id"),)

    def __str__(self):
        return self.nombreLista


class DetalleListaUsuario(models.Model):
    idUsuario = models.ForeignKey(User, on_delete=models.PROTECT)
    numLista = models.ForeignKey(ListaPersonalizadaUsuario, on_delete=models.PROTECT)
    numReceta = models.ForeignKey(Receta, on_delete=models.PROTECT)

    # TODO: Controlar al insertar que no puedarn repetirse recetas en la misma lista
    # class Meta:
        # unique_together = (("idUsuario", "numLista", "numReceta"),)

    def __str__(self):
        return self.numLista
