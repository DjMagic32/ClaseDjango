# Generated by Django 4.0.6 on 2022-07-29 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmbre', models.CharField(max_length=100)),
                ('libros', models.CharField(max_length=100)),
            ],
        ),
    ]
