# Generated by Django 2.2.3 on 2019-08-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdata', '0008_auto_20190802_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bpoint',
            name='route',
            field=models.ManyToManyField(related_name='bpoints', to='bdata.Route'),
        ),
    ]
