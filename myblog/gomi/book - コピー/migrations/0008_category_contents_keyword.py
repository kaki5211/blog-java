# Generated by Django 3.2 on 2021-05-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_publisher_publisher_eng'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='contents_keyword',
            field=models.TextField(blank=True, verbose_name='キーワード'),
        ),
    ]
