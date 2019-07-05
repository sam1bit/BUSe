# Generated by Django 2.2.3 on 2019-07-03 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bno', models.CharField(max_length=10)),
                ('driver', models.TextField()),
                ('conducter', models.TextField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdata.Route')),
            ],
        ),
    ]
