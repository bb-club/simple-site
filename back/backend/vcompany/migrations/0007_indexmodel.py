# Generated by Django 3.1.3 on 2021-01-29 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcompany', '0006_auto_20201122_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(blank=True, max_length=255, verbose_name='англ')),
                ('title_ch', models.CharField(blank=True, max_length=255, verbose_name='китайский')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('image_src', models.ImageField(blank=True, upload_to='img/index', verbose_name='изображение')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Категория или продукт на главной',
                'verbose_name_plural': 'Категории на главной',
                'ordering': ('-created',),
            },
        ),
    ]
