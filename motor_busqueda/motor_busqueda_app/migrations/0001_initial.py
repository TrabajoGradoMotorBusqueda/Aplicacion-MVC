# Generated by Django 3.1.3 on 2020-11-27 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_investigacion', models.TextField(null=True)),
                ('titulo_investigacion', models.TextField(null=True)),
                ('resumen_investigacion', models.TextField(null=True)),
                ('estado_investigacion', models.TextField(null=True)),
                ('palabra_clave1', models.TextField(null=True)),
                ('palabra_clave2', models.TextField(null=True)),
                ('palabra_clave3', models.TextField(null=True)),
                ('palabra_clave4', models.TextField(null=True)),
                ('palabra_clave5', models.TextField(null=True)),
                ('convocatoria', models.TextField(null=True)),
                ('tipo_convocatoria', models.TextField(null=True)),
                ('anio_convocatoria', models.TextField(null=True)),
                ('codigo_autor1', models.TextField(null=True)),
                ('nombres_autor1', models.TextField(null=True)),
                ('apellidos_autor1', models.TextField(null=True)),
                ('programa_autor1', models.TextField(null=True)),
                ('facultad_autor1', models.TextField(null=True)),
                ('departamento_autor1', models.TextField(null=True)),
                ('grupo_investigacion1', models.TextField(null=True)),
                ('linea_investigacion1', models.TextField(null=True)),
                ('codigo_autor2', models.TextField(null=True)),
                ('nombres_autor2', models.TextField(null=True)),
                ('apellidos_autor2', models.TextField(null=True)),
                ('programa_autor2', models.TextField(null=True)),
                ('facultad_autor2', models.TextField(null=True)),
                ('departamento_autor2', models.TextField(null=True)),
                ('grupo_investigacion2', models.TextField(null=True)),
                ('linea_investigacion2', models.TextField(null=True)),
                ('codigo_autor3', models.TextField(null=True)),
                ('nombres_autor3', models.TextField(null=True)),
                ('apellidos_autor3', models.TextField(null=True)),
                ('programa_autor3', models.TextField(null=True)),
                ('facultad_autor3', models.TextField(null=True)),
                ('departamento_autor3', models.TextField(null=True)),
                ('grupo_investigacion3', models.TextField(null=True)),
                ('linea_investigacion3', models.TextField(null=True)),
                ('codigo_autor4', models.TextField(null=True)),
                ('nombres_autor4', models.TextField(null=True)),
                ('apellidos_autor4', models.TextField(null=True)),
                ('programa_autor4', models.TextField(null=True)),
                ('facultad_autor4', models.TextField(null=True)),
                ('departamento_autor4', models.TextField(null=True)),
                ('grupo_investigacion4', models.TextField(null=True)),
                ('linea_investigacion4', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_investigacion', models.TextField(null=True)),
                ('titulo_investigacion', models.TextField(null=True)),
                ('resumen_investigacion', models.TextField(null=True)),
                ('estado_investigacion', models.TextField(null=True)),
                ('palabra_clave1', models.TextField(null=True)),
                ('palabra_clave2', models.TextField(null=True)),
                ('palabra_clave3', models.TextField(null=True)),
                ('palabra_clave4', models.TextField(null=True)),
                ('palabra_clave5', models.TextField(null=True)),
                ('convocatoria', models.TextField(null=True)),
                ('tipo_convocatoria', models.TextField(null=True)),
                ('anio_convocatoria', models.TextField(null=True)),
                ('codigo_autor1', models.TextField(null=True)),
                ('nombres_autor1', models.TextField(null=True)),
                ('apellidos_autor1', models.TextField(null=True)),
                ('programa_autor1', models.TextField(null=True)),
                ('departamento_autor1', models.TextField(null=True)),
                ('facultad_autor1', models.TextField(null=True)),
                ('grupo_investigacion1', models.TextField(null=True)),
                ('linea_investigacion1', models.TextField(null=True)),
                ('codigo_autor2', models.TextField(null=True)),
                ('nombres_autor2', models.TextField(null=True)),
                ('apellidos_autor2', models.TextField(null=True)),
                ('programa_autor2', models.TextField(null=True)),
                ('departamento_autor2', models.TextField(null=True)),
                ('facultad_autor2', models.TextField(null=True)),
                ('grupo_investigacion2', models.TextField(null=True)),
                ('linea_investigacion2', models.TextField(null=True)),
                ('codigo_autor3', models.TextField(null=True)),
                ('nombres_autor3', models.TextField(null=True)),
                ('apellidos_autor3', models.TextField(null=True)),
                ('programa_autor3', models.TextField(null=True)),
                ('departamento_autor3', models.TextField(null=True)),
                ('facultad_autor3', models.TextField(null=True)),
                ('grupo_investigacion3', models.TextField(null=True)),
                ('linea_investigacion3', models.TextField(null=True)),
                ('codigo_autor4', models.TextField(null=True)),
                ('nombres_autor4', models.TextField(null=True)),
                ('apellidos_autor4', models.TextField(null=True)),
                ('programa_autor4', models.TextField(null=True)),
                ('departamento_autor4', models.TextField(null=True)),
                ('facultad_autor4', models.TextField(null=True)),
                ('grupo_investigacion4', models.TextField(null=True)),
                ('linea_investigacion4', models.TextField(null=True)),
                ('nombre_asesor', models.TextField(null=True)),
            ],
        ),
    ]
