# Generated by Django 2.2.4 on 2019-09-01 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0003_delete_recetascategorias'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriasReceta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
