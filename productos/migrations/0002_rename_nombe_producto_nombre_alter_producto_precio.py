# Generated by Django 4.1.7 on 2023-06-06 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nombre',
            new_name='nombre',
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=True),
        ),
    ]
