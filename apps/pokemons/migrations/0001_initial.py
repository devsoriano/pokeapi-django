# Generated by Django 4.2.16 on 2024-11-28 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('abilities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('sprites', models.JSONField()),
                ('types', models.JSONField()),
                ('abilities', models.ManyToManyField(related_name='pokemons', to='abilities.ability')),
            ],
        ),
    ]
