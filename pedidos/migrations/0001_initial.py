# Generated by Django 4.1.7 on 2023-06-06 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('mesa', models.IntegerField()),
                ('lista_productos', models.JSONField()),
            ],
        ),
    ]
