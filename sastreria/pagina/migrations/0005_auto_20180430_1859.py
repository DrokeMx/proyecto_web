# Generated by Django 2.0.1 on 2018-04-30 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0004_auto_20180429_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='resource',
        ),
        migrations.AddField(
            model_name='purchase',
            name='resource',
            field=models.ManyToManyField(to='pagina.Product'),
        ),
    ]
