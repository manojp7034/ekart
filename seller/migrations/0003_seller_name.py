# Generated by Django 5.0.6 on 2024-06-14 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='name',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
