# Generated by Django 3.1.7 on 2021-12-08 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20211208_2130'),
        ('ume', '0002_auto_20211208_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.serviceprovider', verbose_name='custom user'),
        ),
    ]
