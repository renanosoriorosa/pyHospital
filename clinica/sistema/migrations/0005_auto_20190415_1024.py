# Generated by Django 2.2 on 2019-04-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_auto_20190415_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='hora',
        ),
        migrations.AlterField(
            model_name='consulta',
            name='data',
            field=models.DateTimeField(unique=True),
        ),
    ]
