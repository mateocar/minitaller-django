# Generated by Django 5.1 on 2024-08-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.IntegerField(max_length=20)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('telefono', models.IntegerField(max_length=15)),
                ('correo', models.EmailField(max_length=100)),
            ],
        ),
    ]
