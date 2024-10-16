# Generated by Django 5.1.2 on 2024-10-15 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='retal_price',
            new_name='rental_price',
        ),
        migrations.AlterField(
            model_name='books',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='status',
            field=models.CharField(blank=True, choices=[('available', 'available'), ('rental', 'rental'), ('sold', 'sold')], max_length=64, null=True),
        ),
    ]
