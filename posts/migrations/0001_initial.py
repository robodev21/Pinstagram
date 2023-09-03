# Generated by Django 4.2.3 on 2023-09-02 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='media/')),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('created_data', models.DateField(auto_now_add=True)),
                ('likes', models.ManyToManyField(related_name='likes', to='accounts.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('commenter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='posts.post')),
            ],
        ),
    ]
