# Generated by Django 2.2.6 on 2020-04-10 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TvShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Dizi Ad')),
                ('kind', models.CharField(max_length=100, verbose_name='Tür')),
                ('issue', models.CharField(max_length=800, verbose_name='Konu')),
                ('year', models.CharField(max_length=10, verbose_name='Yıl')),
                ('director', models.CharField(max_length=70, verbose_name='Yönetmen')),
                ('performer', models.CharField(max_length=250, verbose_name='Oyuncular')),
                ('season', models.CharField(max_length=30, verbose_name='Sezon Sayısı')),
                ('imdbPoint', models.CharField(max_length=5, verbose_name='IMDB Puanı')),
                ('link', models.CharField(max_length=200, verbose_name='Fragman')),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]