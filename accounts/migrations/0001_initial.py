# Generated by Django 4.2.3 on 2023-09-02 19:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('firstname', models.CharField(blank=True, max_length=20, null=True)),
                ('lastname', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.DateField(blank=True, default=datetime.date(2023, 9, 3), null=True)),
                ('follows', models.ManyToManyField(blank=True, related_name='followed_by', to='accounts.profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
