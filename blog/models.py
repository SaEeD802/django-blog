from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام دسته بندی')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(status=True)


class Article(models.Model):
    slug = models.SlugField(max_length=100, blank=True, unique=True, verbose_name='عنوان در url')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name='نویسنده')
    category = models.ManyToManyField(Category, related_name='articles', verbose_name="دسته بندی")
    title = models.CharField(max_length=70, verbose_name='عنوان')
    body = models.TextField(verbose_name='متن')
    image = models.ImageField(upload_to='images/articles', blank=True, null=True, verbose_name='تصویر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    floatfield = models.FloatField(default=1, verbose_name='مقدار عددی')
    myfile = models.FileField(upload_to='files/articles', null=True, verbose_name='فایل')
    status = models.BooleanField(default=True, verbose_name='وضعیت')  # True: منتشر شده False: منتشر نشده
    published = models.BooleanField(default=True, verbose_name='وضعیت نمایش')  # مقاله منتشر شده یا نه
    pub_date = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    # custom manager
    objects = models.Manager()
    custom_manager = ArticleManager()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="70px" height="70px">')
        return format_html('<h3 style="color: red;">تصویری وجود ندارد</h3>')

    def __str__(self):
        return f"{self.title} - {self.body[:30]}..."

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ('-created',)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='کاربر')
    parent = models.ForeignKey('self', on_delete= models.CASCADE, null=True, blank=True, related_name='replies', verbose_name='والد')
    body = models.TextField(verbose_name='متن')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')

    def __str__(self):
        return self.body[:50]

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name='موضوع')
    text = models.TextField(verbose_name='متن')
    email = models.EmailField(verbose_name='ایمیل')
    age = models.IntegerField(default=0, verbose_name='سن')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ساعت پیام', null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="تاریخ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='کاربر')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes', verbose_name='مقاله')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="پسندیده شده در")

    def __str__(self):
        return f"{self.user.username} - {self.article.title}"

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'
        ordering = ('-created_at',)
