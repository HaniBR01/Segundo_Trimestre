# Generated by Django 4.0.4 on 2022-08-27 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Segundo_Trimestre', '0002_pessoa_habilitacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habilitacao',
            name='pessoa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Segundo_Trimestre.pessoa'),
        ),
    ]