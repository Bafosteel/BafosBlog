from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField('Name',max_length=50)
    slug = models.SlugField('Slug')

    def __str__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class PostManager(models.Manager):
    def published(self):
        return self.filter(draft=False)
    def drafted(self):
        return self.filter(draft=True)

class BlogPost(models.Model):
    title = models.CharField('Title',max_length=50)
    slug = models.SlugField('Slug')
    tease = models.TextField('Tease(summary)', blank=True)
    body = models.TextField('Content')
    draft = models.BooleanField('Is draft',default=True)
    created_date = models.DateTimeField('Date of creation',default=datetime.now)
    published_date = models.DateTimeField('Date of publication',default=datetime.now)
    category = models.ForeignKey(Category,related_name='entries')

    objects = PostManager()


    def __str__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        ordering = ('-published_date',)

    @models.permalink
    def get_absolute_url(self):
        return ('blog_details', (), {'year': self.published_date.year,
                                     'month': self.published_date.strftime('%m'),
                                     'day': self.published_date.strftime('%d'),
                                     'slug': self.slug})

