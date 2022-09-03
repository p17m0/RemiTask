# Generated by Django 4.1 on 2022-09-02 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='uploads/images')),
                ('specification', models.FileField(upload_to='uploads/specifications')),
                ('price', models.FloatField(max_length=4)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.catalog')),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share', models.IntegerField()),
                ('condition', models.CharField(max_length=40)),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.commodity')),
            ],
        ),
    ]
