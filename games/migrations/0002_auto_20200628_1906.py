# Generated by Django 2.2.6 on 2020-06-28 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='eu_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='jp_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='na_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(to='games.Genre'),
        ),
        migrations.AlterField(
            model_name='game',
            name='platform',
            field=models.ManyToManyField(to='games.Platform'),
        ),
    ]