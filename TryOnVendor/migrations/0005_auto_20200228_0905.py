# Generated by Django 3.0.3 on 2020-02-28 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TryOnVendor', '0004_auto_20200228_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TryOnVendor.Vendor'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='address_proof',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='permit_document',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]