# Generated by Django 3.0.5 on 2020-05-25 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0002_auto_20200501_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='コメント')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog_app.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
