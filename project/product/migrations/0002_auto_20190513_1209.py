# Generated by Django 2.2 on 2019-05-13 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subproducts',
            old_name='product',
            new_name='user_id',
        ),
    ]