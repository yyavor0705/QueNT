# Generated by Django 2.2.4 on 2019-08-31 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djUI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobtype',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djUI.Company'),
        ),
    ]
