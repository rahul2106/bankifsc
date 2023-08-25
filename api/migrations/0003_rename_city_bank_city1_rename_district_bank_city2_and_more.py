# Generated by Django 4.1.10 on 2023-08-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_bank_delete_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bank',
            old_name='city',
            new_name='city1',
        ),
        migrations.RenameField(
            model_name='bank',
            old_name='district',
            new_name='city2',
        ),
        migrations.RenameField(
            model_name='bank',
            old_name='bank_id',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='bank',
            name='std_code',
            field=models.CharField(default=12, max_length=50),
            preserve_default=False,
        ),
    ]