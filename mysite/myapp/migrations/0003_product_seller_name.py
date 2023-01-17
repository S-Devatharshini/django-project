# Generated by Django 4.0 on 2023-01-16 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('myapp', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
