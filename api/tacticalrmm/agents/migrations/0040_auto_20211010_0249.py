# Generated by Django 3.2.6 on 2021-10-10 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0039_auto_20210714_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='agent_id',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='created_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='modified_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]