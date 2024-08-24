# Generated by Django 5.1 on 2024-08-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='forma_pago',
            fields=[
                ('id_forma_pago', models.AutoField(primary_key=True, serialize=False)),
                ('forma_pago', models.CharField(choices=[('EF', 'Efectivo'), ('TRANF', 'Transferencia')], max_length=25)),
            ],
        ),
    ]
