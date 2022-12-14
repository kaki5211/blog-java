# Generated by Django 3.2 on 2022-09-06 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20220904_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='contents_synopsis',
            field=models.TextField(blank=True, null=True, verbose_name='あらすじ'),
        ),
        migrations.AlterField(
            model_name='book',
            name='fin',
            field=models.BooleanField(blank=True, null=True, verbose_name='完読'),
        ),
        migrations.AlterField(
            model_name='book',
            name='update_day',
            field=models.DateField(blank=True, null=True, verbose_name='更新日'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_eng',
            field=models.CharField(blank=True, choices=[('action_eng', 'action'), ('adventure_eng', 'adventure'), ('youth_eng', 'youth'), ('love_eng', 'love'), ('sf_eng', 'sf'), ('history_eng', 'history'), ('mystery_eng', 'mystery'), ('comedy_eng', 'comedy'), ('horror_eng', 'horror')], max_length=20, null=True, verbose_name='カテゴリーeng'),
        ),
    ]
