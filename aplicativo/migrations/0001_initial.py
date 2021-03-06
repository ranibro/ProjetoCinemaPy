# Generated by Django 3.2.7 on 2021-10-05 21:32

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.CharField(max_length=4, verbose_name='Sigla')),
                ('livre', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cartaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataCartaz', models.DateTimeField(verbose_name='Data do Cartaz')),
                ('assentos', models.ManyToManyField(to='aplicativo.Assentos')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=32, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=32, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=32, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assento', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=16)),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=16, verbose_name='Nome')),
                ('sinopse', models.CharField(max_length=128, verbose_name='Sinopse')),
                ('categoria', models.CharField(choices=[('Action', 'A????o'), ('Adventure', 'Aventura'), ('Comedy', 'Com??dia'), ('Terror', 'Terror'), ('Drama', 'Drama'), ('Fantasy', 'Fantasia'), ('Sci-Fi', 'Fic????o'), ('Romance', 'Romance')], max_length=32)),
                ('classificacao', models.CharField(choices=[('Livre', 'Livre'), ('10', '10+'), ('12', '12+'), ('14', '14+'), ('16', '16+'), ('18', '18+')], max_length=32)),
                ('duracao', models.CharField(max_length=16, verbose_name='Dura????o')),
                ('capa', stdimage.models.StdImageField(upload_to='imagens', verbose_name='Capa do Filme')),
                ('cartaz', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aplicativo.cartaz')),
            ],
        ),
    ]
