# Generated by Django 4.1.5 on 2023-01-31 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedproduct',
            name='returned_state',
            field=models.CharField(blank=True, choices=[('O', 'Okay'), ('A', 'Abnormal'), ('D', 'Dead')], default='O', max_length=1, null=True),
        ),
    ]