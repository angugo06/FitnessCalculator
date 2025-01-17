# Generated by Django 3.2.6 on 2021-09-20 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner'), ('snacks', 'snacks')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('carbohydrate', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('fat', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('protein', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('calories', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6)),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('category', models.ManyToManyField(to='calculator.Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserFoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ManyToManyField(blank=True, to='users.Costumer')),
                ('food_item', models.ManyToManyField(to='calculator.FoodItem')),
            ],
        ),
    ]
