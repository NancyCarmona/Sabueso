# Generated by Django 3.1.1 on 2021-01-19 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210118_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descarganotadof',
            name='existePDF',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
