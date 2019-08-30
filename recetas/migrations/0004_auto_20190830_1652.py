# Generated by Django 2.2.4 on 2019-08-30 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0003_comentariosreceta_detallelistausuario_ingredientes_listapersonalizadausuario_pasosreceta'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='costeReceta',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='receta',
            name='minustosTiempoPreparacion',
            field=models.IntegerField(blank=0, default=0),
        ),
        migrations.AlterField(
            model_name='receta',
            name='descripcion',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='receta',
            name='numMeGusta',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='receta',
            name='vecesCompartida',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='receta',
            name='vecesVista',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='receta',
            name='visible',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]