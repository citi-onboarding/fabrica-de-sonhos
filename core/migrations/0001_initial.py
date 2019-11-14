# Generated by Django 2.2.7 on 2019-11-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SobreInstituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sobre', models.TextField(blank=True, null=True, verbose_name='Sobre a Instituição')),
            ],
            options={
                'verbose_name': 'Sobre a Instituição',
            },
        ),
        migrations.CreateModel(
            name='Valores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=100, verbose_name='Valor')),
                ('image', models.ImageField(null=True, upload_to='imagemValores/', verbose_name='Imagem do valor')),
                ('gif', models.ImageField(null=True, upload_to='gifValores/', verbose_name='Gif do valor')),
            ],
            options={
                'verbose_name': 'Valor',
                'verbose_name_plural': 'Valores',
            },
        ),
    ]
