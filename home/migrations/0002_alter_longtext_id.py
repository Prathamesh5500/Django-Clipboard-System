# Generated by Django 5.0.1 on 2024-01-15 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='longtext',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
