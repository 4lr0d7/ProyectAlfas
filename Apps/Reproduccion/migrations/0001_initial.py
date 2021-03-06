# Generated by Django 3.0.3 on 2020-05-03 04:59

import Apps.Reproduccion.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('duracion', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('fecha', models.DateField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to=Apps.Reproduccion.models.images_path)),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albumes',
            },
        ),
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('duracion', models.DecimalField(decimal_places=2, max_digits=4)),
                ('autor', models.CharField(max_length=100)),
                ('calificacion', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reproduccion.Album')),
            ],
            options={
                'verbose_name': 'Cancion',
                'verbose_name_plural': 'Canciones',
            },
        ),
        migrations.CreateModel(
            name='Disquera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Disquera',
                'verbose_name_plural': 'Disqueras',
            },
        ),
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('is_public', models.BooleanField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Playlist',
                'verbose_name_plural': 'Playlists',
            },
        ),
        migrations.CreateModel(
            name='UsuarioCanciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cancion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reproduccion.Cancion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UsuarioCancion',
                'verbose_name_plural': 'UsuarioCanciones',
            },
        ),
        migrations.CreateModel(
            name='PlaylistCanciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cancion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reproduccion.Cancion')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reproduccion.Playlist')),
            ],
            options={
                'verbose_name': 'PlaylistCancion',
                'verbose_name_plural': 'PlaylistCanciones',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='disquera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reproduccion.Disquera'),
        ),
        migrations.AddField(
            model_name='album',
            name='generos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reproduccion.Generos'),
        ),
    ]
