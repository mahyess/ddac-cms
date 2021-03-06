# Generated by Django 2.1.3 on 2018-12-04 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20181204_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='container',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.Container'),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='dept_country',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept_country', to='main.Country'),
        ),
    ]
