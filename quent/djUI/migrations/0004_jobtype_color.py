# Generated by Django 2.2.4 on 2019-08-31 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djUI', '0003_auto_20190831_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobtype',
            name='color',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
