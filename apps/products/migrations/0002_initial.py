# Generated by Django 4.2.6 on 2023-10-09 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='subsidiary',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.subsidiary'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='product_brand',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.productbrand'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_brand',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.productbrand'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_model',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.productmodel'),
        ),
        migrations.AlterUniqueTogether(
            name='store',
            unique_together={('product', 'subsidiary')},
        ),
    ]
