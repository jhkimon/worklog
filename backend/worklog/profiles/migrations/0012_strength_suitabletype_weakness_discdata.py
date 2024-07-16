# Generated by Django 5.0.6 on 2024-07-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_remove_feedback_long_questions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strength',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuitableType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('desciption', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Weakness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DISCData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disc_character', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('strength', models.ManyToManyField(to='profiles.strength')),
                ('suitable_type', models.ManyToManyField(to='profiles.suitabletype')),
                ('weakness', models.ManyToManyField(to='profiles.weakness')),
            ],
        ),
    ]
