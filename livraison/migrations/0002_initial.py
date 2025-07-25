# Generated by Django 4.1.7 on 2023-03-31 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('livraison', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='commande_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commande',
            name='commande_trajet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='livraison.trajet'),
        ),
    ]
