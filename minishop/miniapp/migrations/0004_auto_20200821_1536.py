# Generated by Django 3.0.3 on 2020-08-21 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0003_auto_20200821_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
    ]