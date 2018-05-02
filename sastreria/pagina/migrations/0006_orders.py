# Generated by Django 2.0.1 on 2018-05-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0005_auto_20180430_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(blank=True, max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cantitad', models.IntegerField()),
                ('precioTotal', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
