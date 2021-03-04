from django.db import models
from tinymce import HTMLField


class SliderModel(models.Model):
    status_choices = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255, blank=True, verbose_name='англ')
    title_ch = models.CharField(max_length=255, blank=True, verbose_name='китайский')
    description = models.CharField(max_length=255, blank=True)
    image_src = models.ImageField(upload_to='img/sliders', verbose_name='слайд', blank=True)
    status = models.CharField(choices=status_choices, max_length=10, default='published')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Слайд'
        verbose_name_plural = 'Все слайды'

    def __str__(self):
        return self.title


class IndexModel(models.Model):
    status_choices = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255, blank=True, verbose_name='англ')
    title_ch = models.CharField(max_length=255, blank=True, verbose_name='китайский')
    description = models.CharField(max_length=255, blank=True)
    image_src = models.ImageField(upload_to='img/index', verbose_name='изображение', blank=True)
    status = models.CharField(choices=status_choices, max_length=10, default='published')
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Категория или продукт на главной'
        verbose_name_plural = 'Категории на главной'

    def __str__(self):
        return self.title


class Category(models.Model):
    status_choices = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    status = models.CharField(choices=status_choices, max_length=10, default='published')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    status_choices = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    name = models.CharField(max_length=255, db_index=True, verbose_name='название русский')
    name_en = models.CharField(max_length=255, db_index=True, blank=True, verbose_name='перевод англ')
    name_ch = models.CharField(max_length=255, db_index=True, blank=True, verbose_name='перевод китайский')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    image_src = models.ImageField(upload_to='img/products/%Y/%m', verbose_name='фото', blank=True)
    status = models.CharField(choices=status_choices, max_length=10, default='published')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class News(models.Model):
    status_choices = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=255, blank=True)
    text = HTMLField('Текст статьи')
    text_en = HTMLField('Текст статьи англ', blank=True)
    text_ch = HTMLField('Текст статьи китайский', blank=True)
    status = models.CharField(choices=status_choices, max_length=10, default='published')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class SinglePage(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=255, blank=True)
    text = HTMLField('Текст страницы')
    text_en = HTMLField('Текст страницы англ', blank=True)
    text_ch = HTMLField('Текст страницы китайский', blank=True)

    class Meta:
        verbose_name = 'Отдельная информационная страница'
        verbose_name_plural = 'Информационные страницы разделов'

    def __str__(self):
        return self.title
