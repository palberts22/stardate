# Generated by Django 4.0.4 on 2022-05-01 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starapp', '0003_rename_id_sdate_id_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sdate',
            name='aspects',
            field=models.CharField(max_length=2048),
        ),
    ]