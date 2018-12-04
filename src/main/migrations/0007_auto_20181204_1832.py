# Generated by Django 2.1.3 on 2018-12-04 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20181204_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipping',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
