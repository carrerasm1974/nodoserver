# Generated by Django 5.1.1 on 2024-09-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_nodo_clasenodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='clasenodo',
            name='grupo',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='clasenodo',
            name='llave',
            field=models.CharField(default='llave1', max_length=50),
        ),
        migrations.AddField(
            model_name='clasenodo',
            name='model',
            field=models.CharField(default='modelo1', max_length=50),
        ),
    ]
