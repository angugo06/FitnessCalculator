# Generated by Django 3.2.6 on 2021-10-06 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_alter_userfooditem_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfooditem',
            old_name='customer',
            new_name='users',
        ),
    ]