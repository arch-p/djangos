# Generated by Django 4.0.2 on 2023-05-28 08:22

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('splatform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('caption', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='post_images')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('no_likes', models.IntegerField(default=0)),
            ],
        ),
    ]
