# Generated by Django 4.1 on 2023-03-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvp', '0006_remove_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disponible',
            name='dia',
            field=models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sabado', 'Sabado')], max_length=9),
        ),
    ]