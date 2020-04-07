# Generated by Django 3.0.1 on 2020-02-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TryOn', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipper',
            name='utype',
        ),
        migrations.AddField(
            model_name='product',
            name='vendor_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipper',
            name='request_status',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='request_status',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
