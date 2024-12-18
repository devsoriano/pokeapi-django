# Generated by Django 4.2.16 on 2024-11-28 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='sprites',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='image_back',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='image_front',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='types',
            field=models.CharField(max_length=200),
        ),
    ]
