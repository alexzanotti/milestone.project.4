# Generated by Django 3.2.19 on 2023-05-12 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20230512_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planorder',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lineitem', to='checkout.order'),
        ),
    ]